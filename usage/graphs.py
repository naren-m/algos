from data_structures import graph


def main():
    # g = graph.AdjacencySetGraph(4)

    # g.add_edge(0, 1)
    # g.add_edge(0, 2)
    # g.add_edge(0, 3)
    # g.add_edge(2, 1)

    # for i in range(4):
    #     print(i, "is adjacent to", g.get_adjacent_vertices(i))

    # for i in range(4):
    #     print("Indegree of ", i, "is ", g.get_indegree(i))

    # for i in range(4):
    #     for j in g.get_adjacent_vertices(i):
    # print("Edge weight between", i, j, "is ", g.get_edge_weight(i, j))

    # g.display()

    v1 = graph.Vertex(1, "data1")
    v2 = graph.Vertex(2, "data2")
    v3 = graph.Vertex(3, "data3")
    v4 = graph.Vertex(4, "data4")

    v1.add_neighbor(v2, 10)
    v1.add_neighbor(v3, 20)
    v1.add_neighbor(v4, 30)
    v2.add_neighbor(v4, 60)
    v3.add_neighbor(v4, 50)
    v4.add_neighbor(v3, 40)

    print("v1", str(v1))
    print("v1 weight", v1.get_weight(v2))
    print("v1 neighbors", [str(n) for n in v1.get_neighbors()])
    print("v1 get vertex data", v1.get_vertex_data())
    v1.set_vertex_data("data1111")
    print("v1 get vertex data", v1.get_vertex_data())

    print("-------------------------------------")

    g = graph.Graph()

    v1 = g.add_vertex(1, "data1")
    v2 = g.add_vertex(2, "data2")
    v3 = g.add_vertex(3, "data3")
    v4 = g.add_vertex(4, "data4")
    v5 = g.add_vertex(5, "data5")

    print("g get_vertices", [str(v) for v in g.get_vertices().iteritems()])
    print("v1", str(v1))

    # g.add_edge(0, 1)
    # g.add_edge(0, 2)
    # g.add_edge(0, 3)
    # g.add_edge(2, 1)

    # for i in range(4):
    #     print(i, "is adjacent to", g.get_adjacent_vertices(i))

    # for i in range(4):
    #     print("Indegree of ", i, "is ", g.get_indegree(i))

    # for i in range(4):
    #     for j in g.get_adjacent_vertices(i):
    # print("Edge weight between", i, j, "is ", g.get_edge_weight(i, j))


if __name__ == '__main__':
    main()
