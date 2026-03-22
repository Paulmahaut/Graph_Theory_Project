from Floyd_Warshall import floyd_warshall
from MatrixHandler import draw_graph2matrix
from Parser import parse_graph
from FW_Reader import shortest_path

ongoing = True

nb_graph = input("Which graph do you want to analyze ? (1-13) or (\'q\' to quit): ")
if nb_graph == 'q':
    ongoing = False
else:
    nb_graph = int(nb_graph)
    
while ongoing:

    g = parse_graph('Graphes/' + str(nb_graph) + '.txt')

    print("Graph #" + str(nb_graph))
    draw_graph2matrix(g)
    
    try:
        L,P = floyd_warshall(g)
        
        display_paths = input("Do you want to display paths ? (y/n) : ")
        
        while display_paths.lower() == 'y':
            sv = int(input("Starting vertex ? (0-" + str(g.n - 1) + ") : "))
            ev = int(input("Ending vertex ? (0-" + str(g.n - 1) + ") : "))
            shortest_path(L, P, sv, ev, g.n)
            display_paths = input("Do you want to display paths ? (y/n) : ")     

    except ValueError:
        print("Absorbing circuit detected")
 
    nb_graph = input("Which graph do you want to analyze ? (1-13) or (\'q\' to quit): ")
    if nb_graph == 'q':
        ongoing = False
    else:
        nb_graph = int(nb_graph)
