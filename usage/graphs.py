"""
    Sample usage for graph data data_structures
"""

from data_structures import graph


def main():

    g = graph.Graph()

    v1 = g.add_vertex(1, "data1")
    v2 = g.add_vertex(2, "data2")
    v3 = g.add_vertex(3, "data3")
    v4 = g.add_vertex(4, "data4")
    v5 = g.add_vertex(5, "data5")

    g.add_edge(v1, v2)
    g.add_edge(v1, v3)

    g.add_edge(v2, v4)
    g.add_edge(v3, v4)

    g.add_edge(v5, v4)

    print("Vertices:", g.vertices())
    print("Edges:", g.edges())
    print("Vertex count:", g.get_vertex_count())

    print("outdegree:")
    print("vertex:", v4.key, "outdegree:", g.get_degree(v4))
    print("vertex:", v1.key, "outdegree:", g.get_degree(v1))


if __name__ == '__main__':
    main()
