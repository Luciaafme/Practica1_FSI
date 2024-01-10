# Search methods

import search

def getTotalCost(list):
    totalCost = 0
    for node in list:
        totalCost += node.get_path_cost()
        print(node)
        print(node.get_path_cost())
    return totalCost

problem1 = search.GPSProblem('A', 'B'
                       , search.romania)
print("***Problem 1: From A to B (Romania Map)***")

#   Anchura-amplitud
print("---Busqueda por anchura-amplitud---")
busquedaPorAmplitud = search.breadth_first_graph_search(problem1).path()
print("\t\t-Coste total:", busquedaPorAmplitud[0].get_path_cost())
print(busquedaPorAmplitud, "\n\n")

#   Profundidad
print("---Busqueda por profundidad---")
busquedaPorProfundidad  = search.depth_first_graph_search(problem1).path()
print("\t\t-Coste total:", busquedaPorProfundidad[0].get_path_cost())
print(busquedaPorProfundidad, "\n\n")

#   Ramificación y acotación
print("---Busqueda por Ramificación y acotación SIN heurística---")
busquedaPorAnchuraAmplitud = search.branch_and_bound(problem1).path()
print("\t\t-Coste total:", busquedaPorAnchuraAmplitud[0].get_path_cost())
print(busquedaPorAnchuraAmplitud)

#   Ramificación y acotación Subestimación
print("\n---Busqueda por Ramificación y acotación CON heurística---")
busquedaPorAnchuraAmplitudConHeuristica = search.branch_and_bound_subestimacion(problem1).path()
print("\t\t-Coste total:", busquedaPorAnchuraAmplitudConHeuristica[0].get_path_cost())
print(busquedaPorAnchuraAmplitudConHeuristica)
# Result:

# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 118 + 111 + 70 + 75 + 120 + 138 + 101 = 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] :


problem2 = search.GPSProblem('O', 'E'
                       , search.romania)
print("\nProblem 2: From Oradea to Eforie (Romania Map)")
#   Anchura-amplitud
print("---Busqueda por anchura-amplitud---")
busquedaPorAmplitud = search.breadth_first_graph_search(problem2).path()
print("\t\t-Coste total:", busquedaPorAmplitud[0].get_path_cost())
print(busquedaPorAmplitud, "\n\n")

#   Profundidad
print("---Busqueda por profundidad---")
busquedaPorProfundidad  = search.depth_first_graph_search(problem2).path()
print("\t\t-Coste total:", busquedaPorProfundidad[0].get_path_cost())
print(busquedaPorProfundidad, "\n\n")

#   Ramificación y acotación
print("---Busqueda por Ramificación y acotación SIN heurística---")
busquedaPorAnchuraAmplitud = search.branch_and_bound(problem2).path()
print("\t\t-Coste total:", busquedaPorAnchuraAmplitud[0].get_path_cost())
print(busquedaPorAnchuraAmplitud)

#   Ramificación y acotación Subestimación
print("---Busqueda por Ramificación y acotación CON heurística---")
busquedaPorAnchuraAmplitudConHeuristica = search.branch_and_bound_subestimacion(problem2).path()
print(busquedaPorAnchuraAmplitudConHeuristica)
print("\t\t-Coste total:", busquedaPorAnchuraAmplitudConHeuristica[0].get_path_cost())



problem3 = search.GPSProblem('G', 'Z'
                       , search.romania)
print("\nProblem 3: From Giurgiu to Zerind (Romania Map)")
#   Anchura-amplitud
print("---Busqueda por anchura-amplitud---")
busquedaPorAmplitud = search.breadth_first_graph_search(problem3).path()
print("\t\t-Coste total:", busquedaPorAmplitud[0].get_path_cost())
print(busquedaPorAmplitud, "\n\n")

#   Profundidad
print("---Busqueda por profundidad---")
busquedaPorProfundidad  = search.depth_first_graph_search(problem3).path()
print("\t\t-Coste total:", busquedaPorProfundidad[0].get_path_cost())
print(busquedaPorProfundidad, "\n\n")

#   Ramificación y acotación
print("---Busqueda por Ramificación y acotación SIN heurística---")
busquedaPorAnchuraAmplitud = search.branch_and_bound(problem3).path()
print("\t\t-Coste total:", busquedaPorAnchuraAmplitud[0].get_path_cost())
print(busquedaPorAnchuraAmplitud)

#   Ramificación y acotación Subestimación
print("---Busqueda por Ramificación y acotación CON heurística---")
busquedaPorAnchuraAmplitudConHeuristica = search.branch_and_bound_subestimacion(problem3).path()
print(busquedaPorAnchuraAmplitudConHeuristica)
print("\t\t-Coste total:", busquedaPorAnchuraAmplitudConHeuristica[0].get_path_cost())


problem4 = search.GPSProblem('N', 'D'
                       , search.romania)
print("\nProblem 4: From Neamt to Dobreta (Romania Map)")
#   Anchura-amplitud
print("---Busqueda por anchura-amplitud---")
busquedaPorAmplitud = search.breadth_first_graph_search(problem4).path()
print("\t\t-Coste total:", busquedaPorAmplitud[0].get_path_cost())
print(busquedaPorAmplitud, "\n\n")

#   Profundidad
print("---Busqueda por profundidad---")
busquedaPorProfundidad  = search.depth_first_graph_search(problem4).path()
print("\t\t-Coste total:", busquedaPorProfundidad[0].get_path_cost())
print(busquedaPorProfundidad, "\n\n")

#   Ramificación y acotación
print("---Busqueda por Ramificación y acotación SIN heurística---")
busquedaPorAnchuraAmplitud = search.branch_and_bound(problem4).path()
print("\t\t-Coste total:", busquedaPorAnchuraAmplitud[0].get_path_cost())
print(busquedaPorAnchuraAmplitud)

#   Ramificación y acotación Subestimación
print("---Busqueda por Ramificación y acotación CON heurística---")
busquedaPorAnchuraAmplitudConHeuristica = search.branch_and_bound_subestimacion(problem4).path()
print(busquedaPorAnchuraAmplitudConHeuristica)
print("\t\t-Coste total:", busquedaPorAnchuraAmplitudConHeuristica[0].get_path_cost())


problem5 = search.GPSProblem('M', 'F'
                       , search.romania)
print("\nProblem 5: From Mehadia to Fagaras (Romania Map)")
#   Anchura-amplitud
print("---Busqueda por anchura-amplitud---")
busquedaPorAmplitud = search.breadth_first_graph_search(problem5).path()
print("\t\t-Coste total:", busquedaPorAmplitud[0].get_path_cost())
print(busquedaPorAmplitud, "\n\n")

#   Profundidad
print("---Busqueda por profundidad---")
busquedaPorProfundidad  = search.depth_first_graph_search(problem5).path()
print("\t\t-Coste total:", busquedaPorProfundidad[0].get_path_cost())
print(busquedaPorProfundidad, "\n\n")

#   Ramificación y acotación
print("---Busqueda por Ramificación y acotación SIN heurística---")
busquedaPorAnchuraAmplitud = search.branch_and_bound(problem5).path()
print("\t\t-Coste total:", busquedaPorAnchuraAmplitud[0].get_path_cost())
print(busquedaPorAnchuraAmplitud)

#   Ramificación y acotación Subestimación
print("---Busqueda por Ramificación y acotación CON heurística---")
busquedaPorAnchuraAmplitudConHeuristica = search.branch_and_bound_subestimacion(problem5).path()
print(busquedaPorAnchuraAmplitudConHeuristica)
print("\t\t-Coste total:", busquedaPorAnchuraAmplitudConHeuristica[0].get_path_cost())

