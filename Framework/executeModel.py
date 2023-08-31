"""
Main file to execute Traffic Equilibrium Model
Computes equilibrium flows according to specified network in "Input"-Folder
Final results are stored in "Output- EquilibriumResults"-Folder

"""

from assignmentFW import frank_wolfe
from searchStepSize import *
from networkStructure import * 
import time 
import csv 
import json 

# save capacity
capac = []
# define & Read-In network structure 
net = Network('net')

with open('Input\SiouxFalls_network.csv') as input:
    lines = input.readlines()
    for ln in lines:
        sep = ln.split(',')
        #ADDITION Safe Capacity
        capac.append(sep[4])
        #
        net.add_edge(Edge(sep))
# initialize network costs
net.init_cost()


# loads expected user trips on network / read data from .JSON
#-->
with open('Input\SiouxFalls_trips.json') as od_demand:
      od_data = json.load(od_demand)


# determine considered origins & destinations
origins = ['N002', 'N003', 'N004', 'N001', 'N005', 'N006','N007','N008', 'N009', 'N010', 'N011', 'N012', 'N013', 'N014', 'N015', 'N016', 'N017', 'N018', 'N019', 'N020', 'N021', 'N022', 'N023', 'N024']
destinations = ['N001', 'N002','N003', 'N004', 'N005','N006','N007','N008','N009','N010','N011','N012','N013','N014','N015','N016','N017','N018','N019','N020','N021','N022','N023','N024']


# time & execute main flow distribution
start_time = time.time()
vol2 = frank_wolfe(net, od_data, origins, destinations)

# Print results of edge, costs and calculated flow into Costs.csv file
f = open("Output- EquilibriumResults\EquilibriumFlows_Costs.csv", "w") 
header=['EdgeNumber','Costs','Flow']
content= csv.DictWriter(f, fieldnames=header)
content.writeheader()

for l in net.edgeset.keys():
            content.writerow({'EdgeNumber': net.edgeset[l].id , 'Costs': net.edgeset[l].cost, 'Flow': vol2[l] })
f.close()


# Output results and return FW as sorted dictionary with corresponding edges
for key in sorted(vol2):
    print ("%s: %s" % (key, vol2[key]))   
elapsed_time = time.time() - start_time
print('\nTotal CPU Time: ', elapsed_time)
print('Equilibrium results have been successfully transfered to Output-Folder!\n')

