"""
    Implementation of Graph.
"""

import abc
import numpy as np


class Vertex():
    """
    Vertex is a building block of a graph abstract abstract_data_type.abc
    An undirected graph consists of a set of vertices and a set of edges
    (unordered pairs of vertices), while a directed graph consists of a
    set of vertices and a set of arcs (ordered pairs of vertices)

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
        return vertex.get_neighbors()


class GraphOld(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight=1):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

# Implementation of Adjacency Matrix


class AdjacencyMatrixGraph(GraphOld):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((self.numVertices, self.numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("Edge weight is < than 1")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        degree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                degree += 1

        return degree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.matrix[i][j] > 0:
                    print("%d ==> %d" % (i, j))


# Implementation of Adjacency Set


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if v == self.vertex_id:
            raise ValueError("Vertex %d is same as vertex id %d" %
                             (v, self.vertex_id))
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return self.adjacency_set


class AdjacencySetGraph(GraphOld):
    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for i in range(self.numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight != 1:
            raise ValueError(
                "Currently not supporting any weights other than 1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for j in self.get_adjacent_vertices(i):
                print("%d ==> %d" % (i, j))
