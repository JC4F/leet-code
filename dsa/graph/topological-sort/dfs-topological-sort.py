'''
Here’s a step-by-step algorithm for topological sorting using Depth First Search (DFS):

Create a graph with n vertices and m-directed edges.
Initialize a stack and a visited array of size n.
For each unvisited vertex in the graph, do the following:
    Call the DFS function with the vertex as the parameter.
    In the DFS function, mark the vertex as visited and recursively call the DFS function for all unvisited neighbors of the vertex.
    Once all the neighbors have been visited, push the vertex onto the stack.
After all, vertices have been visited, pop elements from the stack and append them to the output list until the stack is empty.
The resulting list is the topologically sorted order of the graph.

'''
def topologicalSortUtil(v, adj, visited, stack):
    # Mark the current node as visited
    visited[v] = True

    # Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Push current vertex to stack which stores the result
    stack.append(v)


# Function to perform Topological Sort
def topologicalSort(adj, V):
    # Stack to store the result
    stack = []

    visited = [False] * V

    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by
    # one
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Print contents of stack
    print("Topological sorting of the graph:", end=" ")
    while stack:
        print(stack.pop(), end=" ")


# Driver code
if __name__ == "__main__":
    # Number of nodes
    V = 4

    # Edges
    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])

    topologicalSort(adj, V)
