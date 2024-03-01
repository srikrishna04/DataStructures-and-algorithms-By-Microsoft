# normal graph
no_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
# weighted graph
no_nodes2 = 9
edges2 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
# directed graph
no_nodes3 = 5
edges3 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
# weighted directed graph
no_nodes4 = 6
edges4 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
class graph():
    def __init__(self, no_nodes, edges):
        self.data  = [[] for _ in range(no_nodes)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
    def __repr__(self):
        return '\n'.join(["{}: {}".format(i, neighbours) for (i, neighbours) in enumerate(self.data)])
    def __str__(self):
        return repr(self)
g1 = graph(no_nodes1, edges1)
print(g1)
    
def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []
    visited[source] = True
    queue.append(source)
    i = 0
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v]= True
                queue.append(v)
        i += 1
    return queue

print(bfs(g1, 3))