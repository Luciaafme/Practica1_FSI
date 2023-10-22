# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

#   Anchura-amplitud
#print(search.breadth_first_graph_search(ab).path())
#   Profundidad
#print(search.depth_first_graph_search(ab).path())

#   Ramificación y acotación
print(search.branch_and_bound(ab).path())
lista = [9123,3,4]
lista= sorted(lista, key=lambda node: node)


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
