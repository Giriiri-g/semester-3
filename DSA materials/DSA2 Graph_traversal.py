## [ Graph Traversal ]


# Adjacency Matrix -> Input
graph = [
[0, 1, 0, 1, 1, 0, 0],
[1, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 0],
[1, 1, 1, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1],
[0, 0, 1, 0, 0, 1, 0]]




def dfs(adj_matrix):
     letter_cipher ={0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G"}
     stack = []
     node = 0
     marked = [0]
     stack.append(node)
     print("['A']")
     while True:
          junc_found = -1
          for i in range(7):
               if adj_matrix[node][i] == 1:
                    if i in marked:
                         continue
                    junc_found = i
                    break
          if junc_found == -1:
               stack.pop()
               if stack == []:
                    print([])
                    return
               node = stack[-1]
          else:
               marked.append(junc_found)
               stack.append(junc_found)
               node = junc_found
          print([letter_cipher[value] for value in stack])



def bfs(adj_matrix):
     queue = []
     letter_cipher ={0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G"}
     node = 0  # current_Node = starting node = A
     marked = [0]   # mark A
     queue.append(0) # enqueue(A)
     print("['A']")
     while True:
          for i in range(7):
               if (adj_matrix[node][i] == 1) and (i not in marked):
                    queue.append(i) # enqueue(i)
                    marked.append(i) # mark the junction i
          queue.remove(node) # dequeue()
          print([letter_cipher[value] for value in queue])
          if queue == []:
               break
          node = queue[0] # current_node = queue.front_peek()


bfs(graph)


print("\n\n")
dfs(graph)

## [ Dijkstra's Algorithm ]


graph = {
'A':{'B':2, 'C':3, 'D':1},
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

dijkstra(graph)
