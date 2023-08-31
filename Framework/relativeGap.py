"""
Main performance metric in Traffic Assignment Models
Primarily calculated and used in "assignmentFW.py" 
See Section 4.3 for definition and purpose

"""


# component to calculate total costs of current iteration as part of relative gap calculation in assignmentFW.py
def computeTotalCosts(net, volumes): 
    sumCosts = 0

    for lid in volumes.keys():
        cost = net.edgeset[lid].cal_costs(volumes[lid])
        cost = cost * volumes[lid]
        sumCosts += cost
    return sumCosts