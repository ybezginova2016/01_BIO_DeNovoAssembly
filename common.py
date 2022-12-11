class Node:
    """ Class Node to represent a vertex in the de bruijn graph """

    def __init__(self, lab):
        self.label = lab
        self.indegree = 0
        self.outdegree = 0

    def __str__(self) -> str:
        return f'{self.label}'


class Edge:
    def __init__(self, lab):
        self.label = lab

    def __str__(self) -> str:
        return f'{self.label}'