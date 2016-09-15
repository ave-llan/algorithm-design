from sys import argv
from random import choice as randomChoice

class Graph (object):

    def __init__(self):
        self.vertices = {}
        self.edges = []

    def addVertex(self, name):
        self.vertices[name] = []

    def addEdge(self, a, b):
        self.vertices[a].append(b)
        self.vertices[b].append(a)
        self.edges.append((a, b) if a < b else (b, a))

    def adjacent(self, vertex):
        return self.vertices[vertex]

    def contract(self, a, b):
        for c in self.vertices.pop(b):
            self.vertices[c].remove(b)
            edge = (b, c) if b < c else (c, b)

            self.edges.remove(edge)
            if c is not a:
                self.vertices[c].append(a)
                self.vertices[a].append(c)
                self.edges.append((a, c) if a < c else (c, a))
        self.vertices[a] = [v for v in self.vertices[a] if v != a]


def karger_min_cut(g):
    while len(g.vertices) > 2:
        a, b = randomChoice(g.edges)
        g.contract(a, b)
    return len(g.edges)


def graph_from_file(file):
    components = {}
    for line in file:
        pieces = line.split("\t")
        pieces = map(int, pieces[:len(pieces) - 1])
        components[pieces[0]] = pieces[1:]

    while True:
        g = Graph()
        for key in components:
            g.addVertex(key)
        for tail, connections in components.iteritems():
            for connection in connections:
                if connection not in g.adjacent(tail):
                    g.addEdge(tail, connection)
        yield g

script, filename = argv

manygraphs = graph_from_file(open(filename))
min_cut = float("inf")
for _ in range(1):
    min_found = karger_min_cut(manygraphs.next())
    print(min_found)
    min_cut = min(min_cut, min_found)

g = manygraphs.next()
min_degree = float("inf")
for v, c in g.vertices.iteritems():
    min_degree = min(min_degree, len(c))
print("min_degree: {0}".format(min_degree))