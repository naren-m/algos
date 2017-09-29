import abc

import numpy as np


class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def addEdge(self, v1, v2, weight=1):
        pass

    @abc.abstractmethod
    def getAdjacentVertices(self, v):
        pass

    @abc.abstractmethod
    def getIndegree(self, v):
        pass

    @abc.abstractmethod
    def getEdgeWeight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((self.numVertices, self.numVertices))

    def addEdge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("Edge weight is < than 1")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def getAdjacentVertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def getIndegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        degree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                degree += 1

    def getEdgeWeight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.matrix[i][j] > 0:
                    print("%d ==> %d" % (i, j))


def main():
    g = AdjacencyMatrixGraph(3)

    g.addEdge(0, 2)
    g.addEdge(0, 1)
    g.addEdge(2, 1)

    g.display()


if __name__ == '__main__':
    main()
