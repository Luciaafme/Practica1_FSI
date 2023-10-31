# Search methods

import search

problem1 = search.GPSProblem('A', 'B'
                       , search.romania)
print("Problem 1: From A to B (Romania Map)")
#   Anchura-amplitud
print(search.breadth_first_graph_search(problem1).path())
#   Profundidad
print(search.depth_first_graph_search(problem1).path())
#   Ramificación y acotación
print(search.branch_and_bound(problem1).path())
#   Ramificación y acotación Subestimación
print(search.branch_and_bound_subestimacion(problem1).path())

# Result:

# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 118 + 111 + 70 + 75 + 120 + 138 + 101 = 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] :


problem2 = search.GPSProblem('NSW', 'NT'
                       , search.australia)
print("\nProblem 2: From NSW to NT (Australia Map)")
#   Anchura-amplitud
print(search.breadth_first_graph_search(problem2).path())
#   Profundidad
print(search.depth_first_graph_search(problem2).path())
#   Ramificación y acotación
print(search.branch_and_bound(problem2).path())
#   Ramificación y acotación Subestimación
print(search.branch_and_bound_subestimacion(problem2).path())
