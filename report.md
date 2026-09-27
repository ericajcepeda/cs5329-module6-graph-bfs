# Programming Assignment 6: Graph Representation and BFS Traversal

Name: Erica Cepeda  
Course: CS 5329

## 1. Graph Representation
I represent my undirected graph as an adjacency list using a Python dictionary. The dictionary keys are the vertices, and the associated lists are the vertices to which they are connected. So, for example, if vertex A is connected to vertices B and C, then the dictionary item for A is ["B", "C"]. Since this is an undirected graph, the edge connecting A and B also makes A an entry in the neighbor list for B.
The vertices might represent any number of entities, such as people, places, or network devices. The edges represent the connections or relationships between these objects. Using an adjacency list means storing the neighbors of each vertex. BFS will be able to access the neighbors without having to check all possible pairs of vertices. My program also allows for an isolated vertex, which has an empty neighbor list.

## 2. How BFS Works
Breadth-first search begins at a selected vertex and explores the neighbors before continuing to other vertices. The `bfs` method starts by inserting the starting vertex into the queue and a `visited` set. It continually takes the vertex off the front of the queue, records it in the traversal order list, and inserts all the unvisited neighbors into the back of the queue.
The queue follows a first-in-first-out order, which ensures that BFS will visit the vertices level-by-level. The vertex is considered visited the moment it is inserted into the queue since it prevents multiple insertions of the same vertex. The final order tells which vertices can be reached from the starting point and the order in which BFS visits each level of vertices. The vertices within the same level are ordered in the order in which they appeared in the adjacency list.

## 3. Test Results

I tested my program successfully with Python 3. The results are presented below.The repository includes a screenshot of the output in `bfs_tests.png`.

| Test | Graph structure | Start | BFS traversal order |
|---|---|---|---|
| Connected | A–B, A-C, B-D, C–E | A | A, B, C, D, E |
| Connected | A-B, A-C, B-D, C-E | C | C, A, E, B, D |
| Disconnected | A-B, B-C, D-E; isolated F | A | A, B, C |
| Disconnected | A-B, B-C, D-E; isolated F | D | D, E |
| Disconnected | A-B, B-C, D-E; isolated F | F | F |
| Seven-vertex | A-B, A-C, B-D, B-E, C-F, E-G | A | A, B, C, D, E, F, G |
| Seven-vertex | A-B, A-C, B-D, B-E, C-F, E-G | G | G, E, B, A, D, C, F |

As we see above, my program can run BFS on both connected and disconnected graphs. With connected graphs, BFS finds all the vertices. However, for the disconnected graphs, the BFS call only explores the component with the starting vertex. Isolated F results only in F. Also, changing the start vertex changes the order of traversal as seen in the connected and seven-vertex graphs.

## 4. Runtime and Space Complexity
Let V be the number of vertices and E the number of edges. Given an adjacency list representation of a graph, BFS takes O(V + E) time in the worst case. BFS marks each reachable vertex visited once and examines all the entries in the list of its neighbors. In the undirected graph, each edge is in two neighbor lists. However, it is still O(E).
At most, the queue can have O(V) elements, and the visited set can also have O(V) elements. The traversal order list will use another O(V) elements. This means that the BFS uses O(V) additional space. Taking into account the storage of the graph representation, the adjacency list uses O(V + E) space.
For BFS in a disconnected graph, the time required depends on the number of vertices and edges reachable from the starting point. As the number of reachable vertices or edges increases, the BFS visits and examines more items.

## 5. BFS vs. DFS
Breadth-First Search explores the graph level by level, starting with the closest vertices. It usually uses a queue. Depth-First Search (DFS) traverses one path as far as possible and backtracks from there. DFS usually uses a stack or recursion.
BFS would be useful for finding the shortest path between two vertices in an unweighted graph. For example, BFS could be used to determine the minimum number of connections between two people in a network. DFS might be useful for exploring the whole path or checking the structure of the graph. However, the first path to the destination vertex found by DFS is not necessarily the shortest.

## 6. Reflection
Completing this assignment made me realize that the representation of a graph influences the way an algorithm works with it. Before creating an adjacency list, I thought about the graph mostly in terms of its diagram, consisting of circles and lines. The adjacency list represented the vertices as a dictionary keys, and now BFS could just lookup a vertex and examine its neighbors immediately. I also understood why the isolated vertex should still have its dictionary entry even though it does not have any edges.
The implementation of the queue made me understand the difference between visiting a vertex and discovering it. Inserting the vertex as visited right after putting it into the queue prevented the program from inserting that vertex multiple times. The disconnected graph really helped me understand this concept, since BFS from A did not visit D, E, or F; the starting point determines which part of the graph is reachable. Finally, the O(V + E) analysis helped to connect the code with efficiency. The program visits reachable vertices once and examines their neighbor lists.
