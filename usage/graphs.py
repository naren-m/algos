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
    #         print("Edge weight between", i, j, "is ", g.get_edge_weight(i, j))

    # g.display()

    g = graph.Graph()

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(2, 1)

    for i in range(4):
        print(i, "is adjacent to", g.get_adjacent_vertices(i))

    for i in range(4):
        print("Indegree of ", i, "is ", g.get_indegree(i))

    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge weight between", i, j, "is ", g.get_edge_weight(i, j))


if __name__ == '__main__':
    main()
