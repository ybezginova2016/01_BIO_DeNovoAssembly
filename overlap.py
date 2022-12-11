# Overlap Graphs (Overlap-Layout-Consensus)
from common import Node, Edge
def get_overlap_graph(reads, n):
    vertices: dict[str, Node] = dict()
    edges: dict[str, list[Edge]] = dict()
    for k1 in reads:
        for k2 in reads:
            if k1 != k2 and k1.endswith(k2[:n]):
                if k1 in vertices:
                    vertices[k1].outdegree += 1
                    if k1 in edges:
                        edges[k1] += [Edge(k2)]
                    else:
                        edges[k1] = [Edge(k2)]
                    if k2 in vertices:
                        vertices[k2].indegree += 1
                    else:
                        vertices[k2] = Node(k2)
                        vertices[k2].indegree += 1
                        edges[k2] = []
                else:
                    vertices[k1] = Node(k1)
                    edges[k1] = [Edge(k2)]
                    vertices[k1].outdegree += 1
                    vertices[k2] = Node(k2)
                    vertices[k2].indegree += 1
                    edges[k2] = []
    return (vertices, edges)

def hamilton(graph, start_v):
    edges: dict[str, list[Edge]] = graph[1]
    size = len(graph[0])
    to_visit = [None, start_v]
    path = []
    visited = set([])
    while (to_visit):
        v = to_visit.pop()
        if v:
            path.append(v)
            if len(path) == size:
                break
            visited.add(v)
            for x in edges[v]:
                if x.label not in to_visit:
                    to_visit.append(None)  # out
                    to_visit.append(x.label)  # in
        else:  # if None we are comming back and pop v
            visited.remove(path.pop())
    return path

def get_contig(contigs: list[str], n):
    res = ''
    for i, contig in enumerate(contigs):
        if i == 0:
            res += contig
        else:
            res+= contig.removeprefix(contigs[i-1][len(contigs[i-1])-n:])
    return res

def get_start(graph):
    vertexes: dict[str, Node] = graph[0]
    start = list(vertexes.keys())[0]
    for k in vertexes:
        if vertexes[k].indegree < vertexes[start].indegree:
            start = k
    return start