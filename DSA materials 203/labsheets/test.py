def dijkstra(adjlist):
    cost = {'A': 0, 'B': None, 'C': None, 'D': None, 'E': None, 'S': None}
    min_ = {'A': 0, 'B': None, 'C': None, 'D': None, 'E': None, 'S': None}
    Node = 'A'

    print(' Node | B C D E S')
    print('   A  | ∞ ∞ ∞ ∞ ∞')

    while True:
        child = adjlist[Node]
        for i in child:
            if cost[Node] is None or cost[Node] == '-':
                continue
            if cost[i] is None or cost[Node] + child[i] < cost[i]:
                cost[i] = cost[Node] + child[i]

        minNode = ['-', float('inf')]
        for i in cost:
            if cost[i] is None or cost[i] == '-':
                continue
            if cost[i] <= minNode[1]:
                minNode[1] = cost[i]
                minNode[0] = i

        Node = minNode[0]
        min_[Node] = minNode[1]
        cost[Node] = '-'

        # Display logic
        display_values = ['∞' if c is None or c == '-' else str(c) for c in cost.values()]
        print(' {:^4} | {} {} {} {} {}'.format(Node, *display_values))

        if all(c == '-' for c in cost.values()):
            break

    print("The Minimum cost to travel to Nodes from A:")
    for i in min_:
        print(f"{i} : {min_[i]}")

    return min_

# Example usage
adjacency_list = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'D': 5, 'E': 2},
    'D': {'B': 2, 'C': 5, 'E': 1, 'S': 3},
    'E': {'C': 2, 'D': 1, 'S': 4},
    'S': {'D': 3, 'E': 4}
}

dijkstra_result = dijkstra(adjacency_list)
