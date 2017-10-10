#! /usr/local/bin/python3
"""
    Implementation of Graph.
"""

import abc
import numpy as np


class GraphBase(abc.ABC):
    """
    Graph data structure consists of a fineate set of vertices.
    Set of ordered, unordered vertices to make a directed and
    an undirected graph respectively.

    Base class for graph implementation.

    Reference: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
    """

    @abc.abstractmethod
    def add_vertex(self, vertex):
        """
        To add an instance of vertex to graph
        """
        pass

    @abc.abstractmethod
    def add_edge(self, from_vertex, to_vertex, weight=None):
        """
        to add new directed edge with weight(optional) to graph.
        """
        pass

    @abc.abstractmethod
    def get_vertex(self, vertexKey):
        """
        get specified vertex from the graph.
        """
        pass

    @abc.abstractmethod
    def get_vertices(self):
        """
        get all vertices of a graph.
        """
        pass

    @abc.abstractmethod
    def get_edge_weight(self, from_vertex, to_vertex):
        """
        gets the weight of the edge between vertices.
        """
        pass

    @abc.abstractmethod
    def get_indegree(self, vertex):
        """
        gets the number of edges inbound to vertex.
        """
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, vertex):
        """
        gets the list of vertices that are adjacent to the given vertex.
        """
        pass


class Graph(GraphBase):
    """
    Graph data structure consists of a fineate set of vertices.
    Set of ordered, unordered vertices to make a directed and
    an undirected graph respectively.

    Reference: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
    """

    def add_vertex(self, vertex):
        """
        To add an instance of vertex to graph
        """
        pass

    def add_edge(self, from_vertex, to_vertex, weight=None):
        """
        to add new directed edge with weight(optional) to graph.
        """
        pass

    def get_vertex(self, vertexKey):
        """
        get specified vertex from the graph.
        """
        pass

    def get_vertices(self, ):
        """
        get all vertices of a graph.
        """
        pass

    def get_edge_weight(self, from_vertex, to_vertex):
        """
        gets the weight of the edge between vertices. 
        """
        pass

    def get_indegree(self, vertex):
        """
        gets the number of edges inbound to vertex. 
        """
        pass

    def get_adjacent_vertices(self, vertex):
        """
        gets the list of vertices that are adjacent to the given vertex. 
        """
        pass


g = Graph()
g.get_vertices()


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
