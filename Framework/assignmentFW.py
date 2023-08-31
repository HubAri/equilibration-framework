"""
Traffic Flow Assignment / Equilibration 
See Section 3.5 - "Frank-Wolfe" for a description of framework components
Also, see Section 3.2 - "AON All or Nothing Assignment" as initial flow pattern  

"""

from copy import deepcopy
from searchStepSize import *
from relativeGap import * 
from dijkstraShortestPath import ShortestPath as SPP
import csv
import time

# Frank-Wolfe method to calculate equilibrium link flows  
def frank_wolfe(network, od_flow, origins, destinations):
    # track and transfer main metrics into Output folder
    f = open("Output- EquilibriumResults/Accuracy_Time_Iteration.csv", "w") 
    header=['RelativeGap','CPU_time', 'Iteration']
    fcontent= csv.DictWriter(f, fieldnames=header)
    fcontent.writeheader()
    # initialization of volumes and costs
    network.init_cost()
    empty = {}
    for l in network.edge_id_set:
        empty[l] = 0

    potential_volume = deepcopy(empty)
   
    # iteration counter, computation time
    n = 1 
    totalTime = 0
    # Shortest Path Travel Times to compute relativeGap
    SPTT = 0
    # initial relativeGap to check convergence 
    relativeGap = 1

    # provide initial & feasible solution by All-Or-Nothing Assignment
    for o in origins:
        for d in destinations:
            cost, path = SPP.dijkstra(network, o, d)
            lpath = [network.edgenode[(path[i], path[i + 1])] for i in range(len(path) - 1)]
            for l in lpath:
                potential_volume[l] += od_flow[o][d]

    volume = deepcopy(potential_volume)
    potential_volume = deepcopy(empty)
    step = 2
   
    
    # iterative flow distribution according to previous AON-Flow pattern - Stopping Criterion at Relative Gap of 10^-4 
    while  relativeGap > 0.0001: # 10^-4 
        start = time.time() 
        network.update_cost(volume)

        for o in origins:
            for d in destinations:
                cost, path = SPP.dijkstra(network, o, d)
                # component of rgap 
                if(od_flow[o][d] != 0 and cost != 0 ):
                    SPTT += cost * od_flow[o][d]
                
                lpath = [network.edgenode[(path[i], path[i + 1])] for i in range(len(path) - 1)]
                for l in lpath:
                    potential_volume[l] += od_flow[o][d] 

        step = lineSearch(network, volume, potential_volume)

        # assign flows / volumes of corresponding link
        for link in network.edge_id_set:
            volume[link] += step * (potential_volume[link] - volume[link])
        potential_volume = deepcopy(empty)

        # compute and display result metrics of each iteration (iteration, convergence, speed)
        stop = time.time() 
        iterationTime = stop-start 
        totalTime += iterationTime
        # determine RGAP 
        TSTT = computeTotalCosts(network, volume)
        # compute relativeGap and check in next iteration 
        relativeGap = abs((TSTT/SPTT)-1)
        fcontent.writerow({'RelativeGap': relativeGap, 'CPU_time' : totalTime, 'Iteration': n})
        # reset
        SPTT = 0
        # end  
        n = n+1 


    f.close()        
    return volume