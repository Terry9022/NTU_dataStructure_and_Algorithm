from typing import List
import sys 
sys.setrecursionlimit(100001)

# Class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
 
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
 
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
        
# Perform DFS on graph starting from vertex v
def DFS(graph, v, discovered, color):
 
    # do for every edge (v -> u)
    for u in graph.adjList[v]:
 
        # if vertex u is explored for first time
        if not discovered[u]:
 
            # mark current node as discovered
            discovered[u] = True
 
            # set color as opposite color of parent node
            color[u] = not color[v]
 
            # if DFS on any subtree rooted at v we return False
            if not DFS(graph, u, discovered, color):
                return False
 
        # if the vertex is already been discovered and color of
        # vertex u and v are same, then the graph is not Bipartite
        elif color[v] == color[u]:
            return False
 
    return True

class Teams:
    def teams(self, idols: int, teetee: List[List[int]]) -> bool:
        
        # create a graph from edges
        graph = Graph(teetee, idols)
        
        # stores vertex is discovered or not
        discovered = [False] * idols

        # stores color 0 or 1 of each vertex in DFS
        color = [False] * idols

        # mark source vertex as discovered and
        # set its color to 0
        discovered[0] = True
        color[0] = False

        # start DFS traversal from any node as graph
        # is connected and undirected
   
        
        return DFS(graph, 0, discovered, color)


