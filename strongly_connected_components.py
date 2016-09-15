import sys


class Graph (object):

    # edges [] forward -> , [] backwards

    def __init__(self, num_vertices):
        self.V = num_vertices
        self.edges = [[[], []] for _ in range(num_vertices)]

    def add_edge(self, tail, head):
        FORWARD, BACK = 0, 1
        self.edges[tail][FORWARD].append(head)
        self.edges[head][BACK].append(tail)

    def head_edges(self, vertex):
        return self.edges[vertex][0]

    def tail_edges(self, vertex):
        return self.edges[vertex][1]

class SCC (object):
    
    def __init__(self, graph):
        self.G = graph
        self.leaders = {}
        self.components = self.dfs_to_find_components(reversed(self.post_order()))

    def dfs_to_find_components(self, reverse_post_order):
        components = []
        visited = [False] * self.G.V
        edges_visited = [False] * self.G.V

        for vertex in reverse_post_order:
            if not visited[vertex]:
                source, count = vertex, 0
                dfs_stack = [vertex]
                visited[vertex] = True
                while len(dfs_stack) > 0:
                    v = dfs_stack[-1]
                    if edges_visited[v]:
                        count += 1
                        dfs_stack.pop()
                    else:
                        for head in self.G.head_edges(v):
                            if not visited[head]:
                                dfs_stack.append(head)
                                visited[head] = True
                        edges_visited[v] = True
                components.append(count)
        return components

    def post_order(self):
        visited = [False] * self.G.V
        edges_visited = [False] * self.G.V
        finished = []

        for vertex in range(self.G.V):
            if not visited[vertex]:
                dfs_stack = [vertex]
                visited[vertex] = True
                while len(dfs_stack) > 0:
                    v = dfs_stack[-1]
                    if edges_visited[v]:       # this is the end of the 'recursive' call for this v
                        finished.append(dfs_stack.pop())
                    else:
                        for tail in self.G.tail_edges(v):
                            if not visited[tail]:
                                dfs_stack.append(tail)
                                visited[tail] = True
                        edges_visited[v] = True
        return finished

# g = Graph(7)
# edges = [
#     (1, 2),
#     (2, 1),
#     (2, 3),
#     (3, 4),
#     (4, 0),
#     (0, 5),
#     (5, 6),
#     (6, 0),
#     (5, 0),
#     (4, 2)
# ]
# for (tail, head) in edges:
#     g.add_edge(tail, head)

# scc = SCC(g)
# print(scc.components)


filepath = sys.argv[1]
g = Graph(875714)
with open(filepath) as f:
    for line in f.readlines():
        edge = [int(a) - 1 for a in line.rstrip('\n').split()]
        g.add_edge(edge[0], edge[1])
    scc = SCC(g)
    print(sorted(scc.components, reverse=True))

