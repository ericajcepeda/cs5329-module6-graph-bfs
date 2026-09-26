from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def bfs(self, start):
        if start not in self.adjacency_list:
            raise ValueError(f"Vertex {start} is not in the graph.")

        visited = {start}
        queue = deque([start])
        order = []

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order
def main():
    # Test 1: Connected graph
    connected = Graph()
    for vertex1, vertex2 in [
        ("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")
    ]:
        connected.add_edge(vertex1, vertex2)

    print("Test 1: Connected graph")
    print("Adjacency list:", connected.adjacency_list)
    print("BFS from A:", connected.bfs("A"))
    print("BFS from C:", connected.bfs("C"))
    print()

    # Test 2: Disconnected graph, including an isolated vertex
    disconnected = Graph()
    for vertex1, vertex2 in [
        ("A", "B"), ("B", "C"), ("D", "E")
    ]:
        disconnected.add_edge(vertex1, vertex2)
    disconnected.add_vertex("F")

    print("Test 2: Disconnected graph")
    print("Adjacency list:", disconnected.adjacency_list)
    print("BFS from A:", disconnected.bfs("A"))
    print("BFS from D:", disconnected.bfs("D"))
    print("BFS from F:", disconnected.bfs("F"))
    print()

    # Test 3: Graph with seven vertices
    larger = Graph()
    for vertex1, vertex2 in [
        ("A", "B"), ("A", "C"), ("B", "D"),
        ("B", "E"), ("C", "F"), ("E", "G")
    ]:
        larger.add_edge(vertex1, vertex2)

    print("Test 3: Seven-vertex graph")
    print("Adjacency list:", larger.adjacency_list)
    print("BFS from A:", larger.bfs("A"))
    print("BFS from G:", larger.bfs("G"))


if __name__ == "__main__":
    main()
