## [Graph]

class Graph:
     def __init__(self, adj_dic):
          self.adj_dic = adj_dic

     def Edge(self, u, v):
          if v in self.adj_dic[u]:
               return self.adj_dic[u][v]
          return None

     def child(self, s):
          return self.adj_dic[s]

     def vertices(self):
          return list(self.adj_dic.keys())



dic = {
'A':{'B':2, 'C':2, 'D':1},
'B':{'D':2},
'C':{'E':1, 'D':3},
'D':{'E':2},
'E':{},
'S':{'A':1, 'B':5},
}

graph = Graph(dic)



## [ Bellman-Ford ]

def Bellman(graph, source):
     min_dist={source:0}
     dist = {}
     for vertex in Graph.vertices():
          dist[vertex] = float('inf')
     dist.pop(source)

     iter_ = len(graph.vertices())

     vertices=[]

     for i in range(1, iter_+1):
          

     return min_dist
