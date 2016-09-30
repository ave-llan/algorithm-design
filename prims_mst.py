import sys
from index_min_pq import IndexMinPQ
infinity = float("inf")

class Edge(object):
    def __init__(self, tail, head, weight):
        self.tail = tail
        self.head = head
        self.weight = weight


class EdgeWeightedGraph(object):
    def __init__(self):
        self.adj = {}

    def add_edge(self, a, b, weight):
        if a not in self.adj:
            self.adj[a] = []
        self.adj[a] += [Edge(a, b, weight)]
        if b not in self.adj:
            self.adj[b] = []
        self.adj[b] += [Edge(b, a, weight)]

    def outgoing_edges(self, v):
        return self.adj[v]

    def vertices(self):
        return self.adj.keys()


class Min_Spanning_Tree(object):

    def __init__(self, weightedGraph):
        self.cost = 0
        self.pq = IndexMinPQ()
        self.g = weightedGraph
        self.tree = set()      # vertices spanned so far

        for v in self.g.vertices():
            self.pq.insert(v, infinity)

        # get a source
        source = self.pq.pop_min()
        self.tree.add(source)
        for neighbor in self.g.outgoing_edges(source):
            self.pq.update_priority(neighbor.head, neighbor.weight)

        while self.pq.count:
            self.cost += self.pq.min_key

            v = self.pq.pop_min()
            self.tree.add(v)
            for neighbor in self.g.outgoing_edges(v):
                if neighbor.head not in self.tree:
                    self.pq.update_priority(neighbor.head,
                                            min(neighbor.weight, self.pq.priority(neighbor.head)))


def unit_test_graph():
    g = EdgeWeightedGraph()
    assert g.vertices() == []
    g.add_edge(0, 10, 5)
    assert sorted(g.vertices()) == [0, 10]

def unit_test():
    unit_test_graph()
    wg = EdgeWeightedGraph()
    for tail, head, weight in [(0, 1, 4), (0, 2, 1), (0, 3, 9), (1, 2, 10), (1, 3, 12), (3, 2, 8)]:
        wg.add_edge(tail, head, weight)
    mst = Min_Spanning_Tree(wg)
    assert mst.cost == 13

    wg2 = EdgeWeightedGraph()
    for tail, head, weight in [(0, 1, 4), (0, 2, 1), (0, 3, 9), (1, 2, 10), (1, 3, 2), (3, 2, 8)]:
        wg2.add_edge(tail, head, weight)
    mst2 = Min_Spanning_Tree(wg2)
    assert mst2.cost == 7

    wg3 = EdgeWeightedGraph()
    for tail, head, weight in [(0, 1, 4), (0, 2, 100), (0, 3, -9), (1, 2, 10), (1, 3, 12), (3, 2, 8)]:
        wg3.add_edge(tail, head, weight)
    mst = Min_Spanning_Tree(wg3)
    assert mst.cost == 3

    return "unit_test pass"

def run_on_file(filename):
    with open(filename) as f:
        edges = [map(int, line.rstrip('\n').split()) for line in f.readlines()]
        print("finding MST of graph with {} vertices and {} edges".format(edges[0][0], edges[0][1]))
        g = EdgeWeightedGraph()
        for tail, head, weight in edges[1:]:
            g.add_edge(tail, head, weight)
        mst = Min_Spanning_Tree(g)
        return mst.cost

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(unit_test())
    elif len(sys.argv) == 2:
        print(run_on_file(sys.argv[1]))
