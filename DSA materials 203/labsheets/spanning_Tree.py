## [ Minimum Spanning Tree ]

class Graph:
     def __init__(self, adj_dic=None):
          self.adj_dic = adj_dic

     def child(self, parent):
          return list(self.adj_dic[parent])

     def vertices(self):
          return list(self.adj_dic)

     def Edges(self):
          edges = {(i, j): self.adj_dic[i][j] for i in self.vertices() for j in self.child(i)}
          return edges

     def PathWeight(self, u, v):
          return self.adj_dic[u][v]



dic = {
'A':{'B':6, 'C':4, 'D':5},
'B':{'E':-1},
'C':{'E':3, 'B':-2},
'D':{'C':-2, 'F':-1},
'E':{'F':3},
'F':{},
}

graph = Graph(dic)

# d = dict(sorted(Edges.items(), key=lambda item: item[1])) # to sort down the Edges dictionary in ascending order
def spanningTree(graph):
     """
     Modules:
     1. Edges in order
     2. Add Edges to the tree in order
     3. Cycle detection
     """
     spanTree = Graph()
     Edges = graph.Edges()
     Edges = dict(sorted(Edges.items(), key=lambda item: item[1]))
     
     return spanTree


