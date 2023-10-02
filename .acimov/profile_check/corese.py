from queue import Queue, Empty
from py4j.java_gateway import JavaGateway
from sys import builtin_module_names
from threading  import Thread
from atexit import register
from subprocess import Popen, PIPE, DEVNULL
from time import sleep
from os.path import exists
from requests import get
from constants import (
    AST_ERROR_FORMAT,
    CORESE_PYTHON_URL,
    CORESE_JAR_NAME
)

def printTitle(title):
    title = "== " + title + " =="
    border = "=" * len(title)
    print("\n" * 2)
    print(border)
    print(title)
    print(border)

#####################################################
# Start the java server & capture the stderr output #
#####################################################

# Capturing the stderr in an OS-agnostic way
# From https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python

if not exists(CORESE_JAR_NAME):
    printTitle("Downloading Corese")
    response = get(CORESE_PYTHON_URL)
    with open(CORESE_JAR_NAME, "wb") as jar:
        jar.write(response.content)

def enqueue_output(out, queue):
    """Get an element of the queue containing the java console output
    ... Without blocking in Windows OS

    :param out: The output to capture
    :param queue: The queue capturing the output
    :returns: An element of the queue
    """
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


ON_POSIX = 'posix' in builtin_module_names
error_queue = Queue()

def get_error_line():
    """Get an output line of the java console without blocking (OS-agnotstic)

    :returns: The first line of the java console output
    """
    # read line without blocking
    try:
        return error_queue.get_nowait()
    except Empty:
        return ""


def get_error_output():
    """Returns The total output of the java console without blocking (OS-agnotstic)

    :returns: The total output
    """
    total_output = []
    current_line = "a"

    while len(current_line) > 0:
        current_line = get_error_line()
        if isinstance(current_line, bytes):
            current_line = current_line.decode('utf-8')
        total_output.append(current_line)

    return "\n".join(total_output).strip()    

# Start java gateway
java_process = Popen(
    ['java', '-jar', '-Dfile.encoding=UTF-8', 'corese-library-python-4.4.1.jar'],
    stdout=PIPE,
    stderr=DEVNULL,
    close_fds=ON_POSIX
)
reader_thread = Thread(target=enqueue_output, args=(java_process.stdout, error_queue))
reader_thread.daemon = True # thread dies with the program
reader_thread.start()

# Waiting for the java server to start up
sleep(1)
gateway = JavaGateway()
register(gateway.shutdown)

# Import of class
OWLProfile = gateway.jvm.fr.inria.corese.core.logic.OWLProfile
Graph = gateway.jvm.fr.inria.corese.core.Graph
Load = gateway.jvm.fr.inria.corese.core.load.Load
QueryProcess = gateway.jvm.fr.inria.corese.core.query.QueryProcess
ResultFormat = gateway.jvm.fr.inria.corese.core.print.ResultFormat
NSManager = gateway.jvm.fr.inria.corese.sparql.triple.parser.NSManager
TEXT_CSV = 14
TEXT_TSV = 15
TURTLE = 2

# A java object resolving prefixes into URIs and the other way
prefix_manager = NSManager.create()

def load(path, extras=""):
    """Load a graph from a local file or a URL

    :param path: local path or a URL or a list of these
    :param extras: raw string in n3 notation containing extra triples
    :returns: the graph load
    """
    if isinstance(path, str):
        path = [path]

    graph = Graph()

    ld = Load.create(graph)

    for file in path:
        if not exists(file):
            continue
        ld.parse(file)
    
    if isinstance(extras, str):
        extras = [extras]
    
    for extra in extras:
        if len(extra) == 0:
            continue
        ld.loadString(extra, TURTLE)

    return graph

def capture_syntax_errors():
    """Captures the syntax errors that are not raised from the java console output

    :returns: A raw string containing the syntax errors
    """
    output = get_error_output()
    output_lines = output.split("\n")
    final_report = []

    for line in output_lines:
        syntax_error = AST_ERROR_FORMAT.search(line)

        if not syntax_error:
            continue

        syntax_error = syntax_error.span()
        line = line[syntax_error[1] + 3:]
        final_report.append(line)
    
    return "\n".join(final_report).strip()

def safe_load(path, extras=""):
    """Safe method to load a graph and eventually catch the error if there is one

    :param path: local path or a URL or a list of these
    :param extras: raw string in n3 notation containing extra triples
    :returns: A graph if it succeeds, an error report if it doesn't
    """
    syntax_errors = ""
    try:
        get_error_output()
        graph = load(path, extras)
        syntax_errors = capture_syntax_errors()

        if len(syntax_errors) > 0:
                return {
                    "file": path,
                    "test_run": False,
                    "syntax_errors": syntax_errors
                }

        return graph

    except Exception as e:
        return {
            "file": path,
            "test_run": False,
            "syntax_errors": syntax_errors,
            "message": str(e).strip()
        }
    
def query_graph(graph, query):
    """Query the given graph and return the result in TSV notation

    :param graph: The Corese graph to query
    :param query: The SparQL query
    :returns: A string containing the result in TSV notation
    """
    query_process = QueryProcess.create(graph)

    abstract_syntax_tree = query_process.ast(query)
    mappings = query_process.query(abstract_syntax_tree)

    resultFormater = ResultFormat.create(mappings)
    resultFormater.setSelectFormat(TEXT_TSV)
    resultFormater.setConstructFormat(TEXT_TSV)
    
    result = resultFormater.toString().split("\n")[1:-1]

    return result