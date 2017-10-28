"""
    Sample usage for graph data data_structures
"""

from data_structures import graph
from data_structures import queue


def q():
    q = queue.Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    q.print_queue()
    while not q.is_empty():
        data = q.dequeue()
        print("Dequeued", data)
        q.print_queue()


def main():

    g = graph.Graph()

    v1 = g.add_vertex(1, 1)
    v2 = g.add_vertex(2, 2)
    v3 = g.add_vertex(3, 3)
    v4 = g.add_vertex(4, 4)
    v5 = g.add_vertex(5, 5)
    v6 = g.add_vertex(6, 6)
    v7 = g.add_vertex(7, 7)
    v8 = g.add_vertex(8, 8)

    g.add_edge(v1, v2)
    g.add_edge(v1, v4)
    g.add_edge(v1, v5)

    g.add_edge(v2, v1)
    g.add_edge(v2, v3)
    g.add_edge(v2, v5)

    g.add_edge(v3, v2)
    g.add_edge(v3, v5)
    g.add_edge(v3, v6)

    g.add_edge(v4, v1)
    g.add_edge(v4, v7)

    g.add_edge(v5, v1)
    g.add_edge(v5, v2)
    g.add_edge(v5, v3)
    g.add_edge(v5, v7)

    g.add_edge(v6, v3)
    g.add_edge(v6, v7)
    g.add_edge(v6, v8)

    g.add_edge(v7, v4)
    g.add_edge(v7, v5)
    g.add_edge(v7, v6)
    g.add_edge(v7, v8)

    g.add_edge(v8, v6)
    g.add_edge(v8, v7)

    print("Edges:")
    for e in g.edges():
        print(e)

    print("Vertex count:", g.get_vertex_count())

    print("outdegree:")
    for v in g.vertices():
        print("vertex:", v, "outdegree:", g.get_degree(g.get_vertex(v)))

    print("Adjacent vertices")
    for v in g.vertices():
        print("vertex", v, "adjacent",
              g.get_adjacent_vertices(g.get_vertex(v)))
    # q()

    bfs(g, v1)


def bfs(g, v):
    q = queue.Queue()
    q.enqueue(v)
    visited = dict()

    while not q.is_empty():
        v = q.dequeue()

        if visited.get(v.key, False):
            continue

        print("vertex", str(v))
        visited[v.key] = True

        for adjacent_key in g.get_adjacent_vertices(v):
            if not visited.get(adjacent_key, False):
                q.enqueue(g.get_vertex(adjacent_key))


def buildBuckets():
    word = "pope"
    words = ["pope", "nope", "rope"]
    line = "pope rope nope"
    print(line[:-1])
    d = dict()
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i + 1:]
            print(bucket)
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    print(d)


if __name__ == '__main__':
    main()
    # buildBuckets()
