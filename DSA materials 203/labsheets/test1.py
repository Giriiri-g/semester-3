

def bfs(graph, source):
     visited = set()
     traversal = []
     queue = [source]
     
     while queue:
          node = queue.pop(0)
          if node not in visited:
               traversal.append(node)
               visited.add(node)
               queue.extend([i for i in graph[node] if i not in visited])
     return traversal

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print(bfs(graph, "A"))

## [subcode]


def dfs(graph, source):
     visited = set(source)
     traversal = [source]
     stack = [source]

     while stack:
          if [i for i in graph[stack[-1]] if i not in visited] == []:
               stack.pop(-1)
               if stack:
                    traversal.append(stack[-1])
          else:
               unvisited = [i for i in graph[stack[-1]] if i not in visited]
               visited.add(unvisited[0])
               traversal.append(unvisited[0])
               stack.append(unvisited[0])
               
     return traversal


graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print(dfs(graph, "A"))
## [subcode]



def dijkstra(graph, source):
     visited = set()
     dist = {node:float('inf') for node in graph}
     dist[source] = 0

     while len(visited)<len(graph):
          unvisited = [i for i in graph if i not in visited]
          node = min(unvisited, key=dist.get)
          visited.add(node)

          for child in graph[node]:
               if dist[node] + graph[node][child] < dist[child]:
                    dist[child] = dist[node] + graph[node][child]
     return dist

graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'D': 2},
    'C': {'E': 1, 'D': 3},
    'D': {'E': 2},
    'E': {},
    'S': {'A': 1, 'B': 5},
}

print(dijkstra(graph, 'S'))

## [subcode]


def bellmanford(graph, source):
     dist = {node:float('inf') for node in graph}
     dist[source] = 0

     for i in range(len(graph)-1):
          for n1 in graph:
               for n2 in graph[n1]:
                    if dist[n1] + graph[n1][n2] < dist[n2]:
                         dist[n2] = dist[n1] + graph[n1][n2]
     return dist


graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'D': 2},
    'C': {'E': 1, 'D': 3},
    'D': {'E': 2},
    'E': {},
    'S': {'A': 1, 'B': 5},
}

print(bellmanford(graph, 'S'))


dic = {
'A':{'B':6, 'C':4, 'D':5},
'B':{'E':-1},
'C':{'E':3, 'B':-2},
'D':{'C':-2, 'F':-1},
'E':{'F':3},
'F':{},
}
print(bellmanford(dic, 'A'))

## [subcode]

def prim(graph, source):
    mst = []
    visited = set()
    cost = 0
    heap = [(0, source)]
    while heap:
        weight, node = heap.pop(0)
        if node not in visited:
            visited.add(node)
            cost += weight
            mst.append((node, weight))
            for i in graph[node]:
                if i not in visited:
                    heap.append((graph[node][i], i))
                    heap.sort()
    return mst, cost

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
print(prim(dic, 'A'))
