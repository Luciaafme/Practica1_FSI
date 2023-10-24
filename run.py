# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

#   Anchura-amplitud
print(search.breadth_first_graph_search(ab).path())
#   Profundidad
print(search.depth_first_graph_search(ab).path())
#   Ramificación y acotación
print(search.branch_and_bound(ab).path())
#   Ramificación y acotación Subestimación
print(search.branch_and_bound_subestimacion(ab).path())


# Result:

# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 118 + 111 + 70 + 75 + 120 + 138 + 101 = 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
