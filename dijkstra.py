import sys
from index_min_pq import IndexMinPQ

MAX_PATH = 1000000

class Edge(object):
    def __init__(self, tail, head, weight):
        self.tail = tail
        self.head = head
        self.weight = weight


class EdgeWeightedDigraph(object):
    def __init__(self):
        self.adj = {}

    def add_edge(self, tail, head, weight):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail] += [Edge(tail, head, weight)]

    def outgoing_edges(self, v):
        return self.adj[v]

    def vertices(self):
        return self.adj.keys()


class ShortestPaths(object):
    def __init__(self, weightedDigraph, source):
        self.s = source
        self.g = weightedDigraph
        self.pq = IndexMinPQ()
        self.dist = {source: 0}

        for edge in self.g.outgoing_edges(self.s):
            self.pq.insert(edge.head, edge.weight)

        for v in self.g.vertices():
            if v is not source and v not in self.pq:
                self.pq.insert(v, MAX_PATH)

        while self.pq.count > 0:
            dist, w = self.pq.min_key, self.pq.pop_min()
            self.dist[w] = dist
            for edge in self.g.outgoing_edges(w):
                if edge.head in self.pq:
                    self.pq.update_priority(edge.head, 
                        min(self.pq.priority(edge.head), self.dist[w] + edge.weight))


filepath = sys.argv[1]
g = EdgeWeightedDigraph()

with open(filepath) as f:
    for line in f.readlines():
        parts = line.rstrip('\n').split()
        tail = int(parts[0])
        for outgoing in parts[1:]:
            head, weight = map(int, outgoing.split(',')) 
            g.add_edge(tail, head, weight)
    paths = ShortestPaths(g, 1)

    for vertex, dist in sorted(paths.dist.iteritems(), key=lambda(_, d): d):
        print vertex, dist