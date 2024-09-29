from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)


def shortes_path_bfs(adj, src, dest, vertex_size):
    bfs_result = []
    shortest_path = []

    visited = [False] * vertex_size

    # dist[0, 1, …., v-1] such that dist[i] stores the distance of vertex i from
    # the source vertex
    dist = [-1] * vertex_size

    # pred[0, 1, ….., v-1] such that pred[i] represents the immediate predecessor
    # of the vertex i in the breadth-first search starting from the source
    pred = [-1] * vertex_size

    queue = []
    queue.append(src)

    distance_from_source = 0
    pred[src] = src
    dist[src] = distance_from_source

    # run BFS
    while queue:
        current_vertex = queue.pop(0)
        bfs_result.append(current_vertex)

        visited[current_vertex] = True
        distance_from_source += 1

        for next_vertex in adj[current_vertex]:
            if not visited[next_vertex]:
                visited[next_vertex] = True
                queue.append(next_vertex)

                if next_vertex in pred:
                    assert False

                pred[next_vertex] = current_vertex
                dist[next_vertex] = distance_from_source

    crawl_back = dest
    # not, this doesn't work if there is no path between src and dest
    while True:
        if crawl_back == src:
            shortest_path.append(src)
            break
        shortest_path.append(crawl_back)
        crawl_back = pred[crawl_back]

    shortest_path.reverse()
    return shortest_path


def main():
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(3, 4)
    graph.addEdge(3, 7)
    graph.addEdge(4, 5)
    graph.addEdge(4, 6)
    graph.addEdge(4, 7)
    graph.addEdge(5, 6)
    graph.addEdge(6, 7)

    vertex_size = len(graph.graph)

    print(shortes_path_bfs(graph.graph, 2, 6, vertex_size, [], []))


if __name__ == "__main__":
    main()
