"""
    Implementation of Graph.
"""

import abc


class Vertex():
    """
    Vertex is a building block of a graph abstract abstract_data_type.abc
    An undirected graph consists of a set of vertices and a set of edges
    (unordered pairs of vertices), while a directed graph consists of a
    set of vertices and a set of edges (ordered pairs of vertices)

    Reference: https://en.wikipedia.org/wiki/Vertex_(graph_theory)
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self._neighbors = dict()

    def __str__(self):
        return 'key: ' + str(self.key) + ', data: ' + str(self.data) + \
            ', neighbors : ' + str([x.key for x in self._neighbors])

    def __iter__(self):
        return iter(self._neighbors.items())

    def get_key(self):
        """
        To get key of the vertex.
        """
        return self.key

    def add_neighbor(self, neighbor, weight=0):
        """
        To add neighbor to the vertex.
        """
        self._neighbors[neighbor] = weight

    def get_weight(self, neighbor):
        """
        To get weight of the edge joining vertex and it's neighbor.
        """
        return self._neighbors[neighbor]

    def set_vertex_data(self, data):
        """
        To set data for a vertex.
        """
        self.data = data

    def get_vertex_data(self):
        """
        To get data for a vertex.
        """
        return self.data

    def neighbors(self):
        """
        Gets the list of vertices that are adjacent to the given vertex.
        """
        return [x.key for x in self._neighbors]


class Graph():
    """
    Graph data structure consists of a fineate set of vertices.
    Set of ordered, unordered vertices to make a directed and
    an undirected graph respectively.

    Reference: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
    """

    def __init__(self, directed=False):
        self.directed = directed
        self.num_vertices = 0
        self._vertices = dict()

    def __iter__(self):
        return iter(self._vertices.items())

    def get_vertex_count(self):
        """
        Returns number of vertices in graph
        """
        return self.num_vertices

    def add_vertex(self, key, data=None):
        """
        To add an instance of vertex to graph
        """
        v = Vertex(key, data)
        self._vertices[key] = v
        self.num_vertices += 1
        return v

    def add_edge(self, f_vertex, t_vertex, weight=0):
        """
        To add new edge with weight(optional) to graph.
        """
        try:
            fv = self._vertices[f_vertex.key]
        except KeyError:
            raise KeyError("Vertex key not found", f_vertex)

        try:
            tv = self._vertices[t_vertex.key]
        except KeyError:
            raise KeyError("Vertex key not found", t_vertex)

        self._vertices[fv.key].add_neighbor(
            self._vertices[tv.key], weight)

        if self.directed:
            self._vertices[tv.key].add_neighbor(
                self._vertices[fv.key], weight)

    def get_vertex(self, key):
        """
        Get specified vertex from the graph.
        """
        return self._vertices[key]

    def vertices(self):
        """
        Get keys of all vertices of a graph.
        """
        return [k for k, _ in self]

    def edges(self):
        """
        Get all edges of a graph.
        """
        return [(k, v.neighbors()) for k, v in self]

    def get_edge_weight(self, from_vertex, to_vertex):
        """
        Gets the weight of the edge between vertices.
        """
        # : TODO: Raise key not found exception if not exists
        return self._vertices[from_vertex.key].get_weight(
            self._vertices[to_vertex])

    def get_degree(self, vertex):
        """
        The number of outward directed graph edges from a given graph vertex
        in a directed graph.

        Gets the number of edges outbound to vertex.
        """
        return len(vertex.neighbors())

    def get_adjacent_vertices(self, vertex):
        """
        Gets the list of vertices that are adjacent to the given vertex.
        """
        return vertex.neighbors()
