## [Graph]

class Graph:
     def __init__(self, adj_dic):
          self.adj_dic = adj_dic

     def Edge(self, u, v):
          if v in self.adj_dic[u]:
               return self.adj_dic[u][v]
          return None

     def child(self, parent):
          return list(self.adj_dic[parent])

     def vertices(self):
          return list(self.adj_dic)

     def Edges(self):
          edges = []
          for i in self.vertices():
               for j in self.child(i):
                    edges.append((i, j))
          return edges

     def PathWeight(self, u, v):
          return self.adj_dic[u][v]



dic = {
'A':{'B':6, 'C':4, 'D':5},
'B':{'E':-1},
'C':{'E':3, 'B':-2},
'D':{'E':-2, 'F':-1},
'E':{'F':3},
'F':{},
}

graph = Graph(dic)



## [ Bellman-Ford ]

def Bellman(Graph, source):
     dist={}
     for vertex in Graph.vertices():
          dist[vertex] = float('inf')
     dist[source] = 0

     iter_ = len(Graph.vertices())
     

     for i in range(iter_-1):
          dist_dup = dist
          for path in Graph.Edges():
               if dist[path[0]] + Graph.PathWeight(path[0], path[1]) < dist[path[1]]:
                    dist[path[1]] = dist[path[0]] + Graph.PathWeight(path[0], path[1])


                    
          if dist_dup == dist:
               return dist
     return dist
