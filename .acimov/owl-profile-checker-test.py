import atexit
import subprocess
from time import sleep

from py4j.java_gateway import JavaGateway

# Start java gateway
java_process = subprocess.Popen(
    ['java', '-jar', '-Dfile.encoding=UTF-8', 'corese-library-python-4.3.1.jar'])
sleep(1)
gateway = JavaGateway()


def exit_handler():
    # Stop java gateway at the enf od script
    gateway.shutdown()
    # print('\n' * 2)
    # print('Gateway Server Stop!')


atexit.register(exit_handler)

# Import of class
OWLProfile = gateway.jvm.fr.inria.corese.core.logic.OWLProfile
Graph = gateway.jvm.fr.inria.corese.core.Graph
Load = gateway.jvm.fr.inria.corese.core.load.Load


#################
# Load / Export #
#################


def exportToFile(graph, format, path):
    """Export a graph to a file

    :param graph: graph to export
    :param format: format of export
    :param path: path of the exported file
    """
    transformer = Transformer.create(graph, format)
    transformer.write(path)


def load(path):
    """Load a graph from a local file or a URL

    :param path: local path or a URL
    :returns: the graph load
    """
    graph = Graph()

    ld = Load.create(graph)
    ld.parse(path)

    return graph


########
# Main #
########


def printTitle(title):
    title = "== " + title + " =="
    border = "=" * len(title)
    print("\n" * 2)
    print(border)
    print(title)
    print(border)


###
# Load graph
###
# printTitle("Load Graph")

graph = load("https://raw.githubusercontent.com/stardog-union/stardog-tutorials/master/music/beatles.ttl")
# print("Graph load ! (" + str(graph.size()) + " triplets)")


###
# Test OWL_RL
###
printTitle("Test OWL_RL")
engine = OWLProfile(graph)
owl_rl = engine.process(OWLProfile.OWL_RL)
print(owl_rl)
