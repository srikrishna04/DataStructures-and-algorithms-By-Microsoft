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


class Graph:
    def __init__(self, no_nodes, edges, directed=False):
        self.data = [[] for _ in range(no_nodes)]
        self.weight = [[] for _ in range(no_nodes)]
        self.directed = directed
        self.weighted = len(edges)>0 and len(edges[0])==3
        for e in edges:
            self.data[e[0]].append(e[1])
            if self.weighted:
                self.weight[e[0]].append(e[2])
            if not self.directed:
                self.data[e[1]].append(e[0])
                if self.weighted:
                    self.weight[e[1]].append(e[2])
    def __repr__(self):
        result = ' '
        for i in range(len(self.data)):
            pairs = list(zip(self.data[i], self.weight[i]))
            result += '{}: {}\n'.format(i, pairs)
        return result
    def __str__(self):
        return repr(self)
G2 = Graph(no_nodes2, edges2)

def shortest_path(Graph, source, dest):
    visited = [False] * len(Graph.data)
    distance = [float('inf')] * len(Graph.data)
    parent = [None] * len(Graph.data)
    queue = []
    idx = 0 
    queue.append(source)
    distance[source] = 0
    visited[source] = True
    while len(queue) > idx and not visited[dest]:
        current = queue[idx]
        update_distances(Graph, current, distance, parent)
        next_node = pick_next_node(visited, distance)
        if next_node is not None:
            visited[next_node] = True
            queue.append(next_node)
        idx += 1
    return distance[dest], distance, parent
def update_distances(Graph, current, distance, parent=None):
    neighbours = Graph.data[current]
    weights = Graph.weight[current]
    for i, node in enumerate(neighbours):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current
def pick_next_node(visited, distance):
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
print(shortest_path(G2, 2, 6))




    





        

        



    


        

