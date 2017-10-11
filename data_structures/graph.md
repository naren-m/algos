# Graphs

Graph data structure consists of a fineate set of vertices.
Set of ordered, unordered vertices to make a directed and
an undirected graph respectively.

[Wiki page on graphs](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))

## Vocabulary for graphs

### Vertex/Node

Vertex is a building block of a graph abstract abstract_data_type.abc
An undirected graph consists of a set of vertices and a set of edges
(unordered pairs of vertices), while a directed graph consists of a
set of vertices and a set of arcs (ordered pairs of vertices)

[Wiki page on vertex](https://en.wikipedia.org/wiki/Vertex_(graph_theory))

### Edge

Edge is another fundamental part of the graph which connects 2 or more vertices.
An edge could be directed or undirected.
If the edge is directed, undirected we call the directed graph as directed,
undirected graph respectively.

### Weight

Edges can be associated with weights representing the cost to traverse
from one vertex to another.

### Path

Path in a graph is finite/infinite sequence of vertices connected by edges.

### Cycle

Cycle is a closed walk consisting of sequence of vertices and starting and
ending at the same vertex.

### Degree

Degree is the number of vertices adjacent to a vertex.

#### Degree in directed graphs

**Indegree:** The number of inward directed graph edges from a given vertex in a directed graph.

**Outdegree:** The number of outward directed graph edges from a given vertex in a directed graph.
Also called as "branching factor" in trees

## Operations

### Operations on vertex

- [x] get_key() to get key(id) of the vertex.
- [x] get_weight(neighbor) to get weight of the edge joining vertex and it's neighbor.
- [x] add_neighbor(vertex) to add neighbor to the vertex.
- [x] set_vertex_data(data) to set data for a vertex.
- [x] get_vertex_data() to get data for a vertex.
- [x] get_neighbors() gets the list of vertices that are adjacent to the given vertex.

### Operations on graph

- [x] add_vertex(vertex) or addNode(node) to add an instance of vertex to graph.
- [ ] remove_vertex(vertex) to remove vertex from the graph.
- [x] add_edge(from_vertex, to_vertex, weight) to add new directed edge with weight to graph.
- [ ] remove_edge(from_vertex, to_vertex) to remove an edge from graph.
- [x] get_vertex(vertexKey) get specified vertex from the graph.
- [x] vertices() get all vertices of a graph.
- [x] edges get all edges of a graph.
- [x] get_edge_weight(from_vertex, to_vertex) gets the weight of the edge between vertices.
- [ ] get_indegree(vertex) gets the number of edges inbound to vertex.
- [x] get_degree(vertex) gets the number of edges outbound to vertex.

## Graph Traversal

## BFS

![Alt text](images/graphs/BFS_undirected_graph.gif "BFS on undirected graph")
[Source for above gif](https://www.cs.usfca.edu/~galles/visualization/BFS.html)

## References

- [Problem Solving with Algorithms and Data Structures](https://interactivepython.org/runestone/static/pythonds/Graphs/toctree.html)
- [Wiki page on graphs](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))
- [Wiki page on vertex](https://en.wikipedia.org/wiki/Vertex_(graph_theory))
- [Graph theory tutorials point](https://www.tutorialspoint.com/graph_theory/graph_theory_fundamentals.htm)