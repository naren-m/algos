# Graphs

## Vocabulary for graphs

### Vertex/Node

Vertex is a fundamental part of a graph.
Vertex comprises a key, and some additional information.

### Edge

Edge is another fundamental part of the graph which connects 2 or more vertices.
An edge could be directed or undirected.
If the edge is directed, undirected we call the directed graph as directed, undirected graph respectively.

### Weight

Edges can be associated with weights representing the cost to traverse from one vertex to another.

### Path

Path in a graph is finite/infinite sequence of vertices connected by edges.

### Cycle

Cycle is a closed walk consisting of sequence of vertices and starting and ending at the same vertex.

## Operations

- add_vertex(vertex) or addNode(node) to add an instance of vertex to graph
- add_edge(from_vertex, to_vertex) to add new directed edge to graph
- add_edge(from_vertex, to_vertex, weight) to add new directed edge with weight to graph
- get_vertex(vertexKey) get specified vertex from the graph
- get_vertices() get all vertices of a graph
- get_edge_weight(from_vertex, to_vertex) gets the weight of the edge between vertices
- get_indegree(vertex) gets the number of edges inbound to vertex
- get_adjacent_vertices(vertex) gets the list of vertices that are adjacent to the given vertex
