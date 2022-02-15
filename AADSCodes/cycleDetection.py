from typing import Dict, Hashable, List,Set
import collections


class DirectedGraph(object):
    def __init__(self, adjacency_list:Dict[Hashable,Set]=None):
        if adjacency_list is None:
            adjacency_list = []
        self.vertex_dict = adjacency_list

    def getVertices(self)->List:
        """return all vertex labels

        Returns:
            List: list of all vertex-labels in the graph
        """
        return list(self.vertex_dict.keys())

    def getNeighbors(self, vertex:Hashable)->Set:
        """returns a list of vertex neighbors

        Args:
            vertex (Hashable): Vertex label

        Raises:
            ValueError: if there is no vertex with a given label
            in the graph

        Returns:
            Set: set of neighbors
        """
        if vertex not in self.vertex_dict.keys():
            raise ValueError(f'Vertex {vertex} does not exist in this graph')
        return self.vertex_dict[vertex]


def detect_cycle(graph: DirectedGraph)->bool:
    """Detects if there exists a cycle in directed graph that might be consisting
    of disconnected components

    Args:
        graph (DirectedGraph): input graph

    Returns:
        bool: True if there is cycle in a graph, else False
    """
    visited = []
    stack = collections.deque()
    for source in graph.getVertices():
        if source not in visited:
            if detect_cycle_recursive(graph, source, visited, stack):
                return True
    return False


def detect_cycle_recursive(graph:DirectedGraph, current_vertex:Hashable, visited: List, stack:collections.deque)->bool:
    """recursively searches for any cycle in connected components

    Args:
        graph (DirectedGraph): input graph
        current_vertex (Hashable): search goes from this vertex
        visited (List): mark visited vertices
        stack (collections.deque): current DFS track

    Returns:
        bool: True if found cycle, False
    """
    visited.append(current_vertex)
    stack.append(current_vertex)
    for v in graph.getNeighbors(current_vertex):
        if v not in visited:
            if detect_cycle_recursive(graph, v, visited, stack):
                return True
        elif v in stack:
            return True
    stack.pop()
    return False


# for (int w : g.getAdjacentNodes(v)) {
#             if(!marked[w]) {
#                 marked[w] = true;
#                 findCycle(g,w,v);
#             } else if (v != u) {
#                 hasCycle = true;
#                 return;
#             }
#         }


def construct_deterministic1():
    graph_adjacency = {}
    graph_adjacency['a'] = {'b'}
    graph_adjacency['b'] = {'c'}
    graph_adjacency['c'] = {'d', 'e', 'f'}
    graph_adjacency['d'] = set()
    graph_adjacency['e'] = {'b'}
    graph_adjacency['f'] = {'b'}
    return DirectedGraph(graph_adjacency)


def construct_deterministic2():
    graph_adjacency = {}
    graph_adjacency['a'] = {'b'}
    graph_adjacency['b'] = {'c'}
    graph_adjacency['c'] = set()
    graph_adjacency['d'] = set()
    graph_adjacency['e'] = {'b'}
    graph_adjacency['f'] = {'b'}
    return DirectedGraph(graph_adjacency)


def test_detect_cycle(constructor):
    is_cyclical = detect_cycle(constructor())
    print(is_cyclical)


# ako Vam kod ne radi na ova dva primjera ispod, dobivate automatski 0 bodova

test_detect_cycle(construct_deterministic1)  # prints True

test_detect_cycle(construct_deterministic2)  # prints False