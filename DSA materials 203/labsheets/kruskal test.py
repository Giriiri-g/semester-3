## [ Minimum Spanning Tree ]

class Graph:
     def __init__(self, adj_dic={}):
          self.adj_dic = adj_dic

     def child(self, parent):
          return self.adj_dic[parent]

     def vertices(self):
          return list(self.adj_dic)

     def Edges(self):
          edges = {(i, j): self.adj_dic[i][j] for i in self.vertices() for j in self.child(i)}
          return edges

     def PathWeight(self, u, v):
          return self.adj_dic[u][v]

     def addVertices(self, *v):
          for i in v:
               self.adj_dic[i] = {}
     def addEdges(self, d={}):# addEdges({("A", "B"):2})
          for i in d:
               if i[0] not in self.adj_dic and i[1] not in self.adj_dic:
                    self.adj_dic[i[0]] = {i[1]:d[i]}
                    self.adj_dic[i[1]] = {i[0]:d[i]}
               elif i[0] not in self.adj_dic and i[1] in self.adj_dic:
                    self.adj_dic[i[0]] = {i[1]:d[i]}
                    self.adj_dic[i[1]][i[0]] = d[i]
               elif i[1] not in self.adj_dic and i[0] in self.adj_dic:
                    self.adj_dic[i[1]] = {i[0]:d[i]}
                    self.adj_dic[i[0]][i[1]] = d[i]
               else:
                    self.adj_dic[i[1]][i[0]] = d[i]
                    self.adj_dic[i[0]][i[1]] = d[i]
     def __str__(self):
          return str(self.adj_dic).replace("}, ", "}\n")[1:-1].replace("'", "")



dic = {
     'A': {'B': 5, 'D': 2},
     'B': {'A': 5, 'C': 4, 'D': 3, 'E': 5, 'F': 6},
     'C': {'B': 4, 'F': 3},
     'D': {'A': 2, 'B': 3, 'E': 7, 'G': 6, 'H':8},
     'E': {'B': 5, 'D': 7, 'F': 1, 'H': 3},
     'F': {'B': 6, 'C': 3, 'E': 1, 'H': 4, 'I': 4},
     'G': {'D': 6, 'H': 4},
     'H': {'D': 8, 'E': 3, 'F': 4, 'G': 4, 'I': 2},
     'I': {'F': 4, 'H': 2}
}

graph = Graph(dic)

def find_set(parent, sets):
     if sets[parent] != parent:
          sets[parent] = find_set(sets[parent], sets)
     return sets[parent]

def union_sets(u, v, sets):
     root_u = find_set(u, sets)
     root_v = find_set(v, sets)
     sets[root_u] = root_v

def kruskal(graph):
     spanTree = Graph()
     sets = {v: v for v in graph.vertices()}
     Edges = sorted(graph.Edges().items(), key=lambda x: x[1])
     pathCost = 0
     for (u, v), weight in Edges:
          if find_set(u, sets) != find_set(v, sets):
               spanTree.addEdges({(u, v):weight})
               pathCost+=weight
               union_sets(u, v, sets)
     print(spanTree)
     print(f"Path Cost : {pathCost}")
     return spanTree, pathCost


kruskal(graph)
