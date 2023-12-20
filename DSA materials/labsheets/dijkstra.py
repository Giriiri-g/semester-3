## [ Dijkstra's Algorithm ]


dic = {
'A':{'B':2, 'C':2, 'D':1},
'B':{'D':2},
'C':{'E':1, 'D':3},
'D':{'E':2},
'E':{},
'S':{'A':1, 'B':5},
}



def dijkstra(adjlist):
     cost = {'A':0, 'B':None, 'C':None, 'D':None, 'E':None, 'S':None}
     min_ = {'A':0, 'B':None, 'C':None, 'D':None, 'E':None, 'S':None}
     Node = 'A'
     print(' Node | B C D E S')
     print('   A  | ∞ ∞ ∞ ∞ ∞')
     while True:
          child = adjlist[Node]
          for i in child:
               if cost[Node] in [None, '-']:
                    continue
               if cost[i] is None or cost[Node]+ child[i] < cost[i]:
                    cost[i] = cost[Node] + child[i]
          # Node = min(cost, key=lambda k: float('inf') if cost[k] is None or cost[k] == '_' else cost[k])
          minNode = ['-', 0]
          for i in cost:
               if cost[i] in [None, '-']:
                    continue
               if cost[i]<=minNode[1]:
                    minNode[1] = cost[i]
                    minNode[0] = i
                    
          Node = minNode[0]
          min_[Node] = minNode[1]
          cost[Node] = '-'
          print(' {:^4} | {} {} {} {} {}'.format(Node, cost['B'], cost['C'], cost['D'], cost['E'], cost['S']))
          if all(c == '-' for c in cost.values()):
               break
     print("The Minimum cost to travel to Nodes from A:")
     for i in min_:
          print(f"{i} : {min_[i]}")
     return min_

#dijkstra(dic)


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


## [Dijkstra 2]
     
def Dijkstra(Graph, source):
     min_dist = {source:0}
     dist = {}
     for vertex in Graph.vertices():
          dist[vertex] = float('inf')
     dist.pop(source)

     Node=source
     while dist!={}:
          for vertex in Graph.child(Node):
               if vertex in min_dist:
                    continue
               if min_dist[Node] + Graph.Edge(Node, vertex) < dist[vertex]:
                    dist[vertex] = min_dist[Node] + Graph.Edge(Node, vertex)
          Node = min(dist, key= lambda k: dist[k])
          min_dist[Node] = dist.pop(Node)


     return min_dist

print(Dijkstra(graph, 'S'))
     
