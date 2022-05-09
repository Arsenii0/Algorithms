from collections import defaultdict


class GraphAdjMatrix:
    def __init__(self, vertex_size):
        self.vertex_size = vertex_size
        self.adj_matrix = [[0] * vertex_size] * vertex_size

    def addEdge(self, v1, v2):
        if v1 >= self.vertex_size or v2 >= self.vertex_size:
            return

        self.adj_matrix[v1][v2] = 1

        # because graph is not directed
        self.adj_matrix[v2][v1] = 1


def dfs_adj_matrix(adj_matrix, curr_vertex, visited):
    visited[curr_vertex] = True

    print(curr_vertex)

    vertex_size = len(adj_matrix[0])
    for next_vertex in range(vertex_size):
        if adj_matrix[curr_vertex][next_vertex] == 1 and not visited[next_vertex]:
            dfs_adj_matrix(adj_matrix, next_vertex, visited)


def test_dfs_with_adj_matrix():
    graph = GraphAdjMatrix(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(0, 4)

    visited = [False] * 5

    dfs_adj_matrix(graph.adj_matrix, 0, visited)


class GraphAdjList:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)


def dfs_adj_list(adj_list, start_vertex, vertices_size):

    traversal_result = []

    def dfs_recursive(adj_list, start_vertex, visited):

        if not adj_list[start_vertex]:
            return

        visited[start_vertex] = True
        traversal_result.append(start_vertex)

        for next_vertex in adj_list[start_vertex]:
            if not visited[next_vertex]:
                dfs_recursive(adj_list, next_vertex, visited)

    visited = [False] * vertices_size
    dfs_recursive(adj_list, start_vertex, visited)

    # Handle the case if the graph has disconnected components (Disconnected grapgh)
    for vertex in range(0, vertices_size):
        if not visited[vertex]:
            dfs_recursive(adj_list, vertex, visited)

    return traversal_result


def dfs_using_stack(adj_list, start_vertex, vertices_size):
    traversal_result = []
    visited = [False] * vertices_size

    stack = []
    stack.append(start_vertex)
    visited[start_vertex] = True

    while stack:
        current_vertex = stack.pop()
        traversal_result.append(current_vertex)

        for connected_vertex in adj_list[current_vertex]:
            if not visited[connected_vertex]:
                visited[connected_vertex] = True
                stack.append(connected_vertex)

    return traversal_result


def test_dfs_with_adj_list():
    g = GraphAdjList()

    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)

    print(dfs_using_stack(g.graph, start_vertex=0, vertices_size=5))


def bfs_adj_list(adj_list, start_vertex, vertices_size):
    traversal_result = []
    visited = [False] * vertices_size

    queue = []
    queue.append(start_vertex)
    visited[start_vertex] = True

    while queue:

        current_vertex = queue.pop(0)
        traversal_result.append(current_vertex)

        for connected_vertex in adj_list[current_vertex]:
            if not visited[connected_vertex]:
                visited[connected_vertex] = True
                queue.append(connected_vertex)

    return traversal_result


def test_bfs():
    g = GraphAdjList()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print(bfs_adj_list(g.graph, 2, len(g.graph)))


def main():
    test_dfs_with_adj_list()


if __name__ == "__main__":
    main()
