"""
Line-Search to determine step size 
See Section 3.4 - "Bi-Section Search"

"""

# calculate step-size for FW by line-search / BiSection search 
def lineSearch(net, prior, posterior):
    lowerB = 0.0
    upperB = 1.0
    step = (lowerB + upperB) / 2.0
    while abs(div(net, prior, posterior, step)) >= 0.01 and abs(upperB-lowerB) > 0.0001: 
        if div(net, prior, posterior, step) * div(net, prior, posterior, upperB) > 0:
            upperB = step
        else:
            lowerB = step
        step = (lowerB + upperB) / 2.0
    return step


def div(net, prior, posterior, step):
    idiv = 0
    for lid in prior.keys():
        dist = posterior[lid] - prior[lid]
        cost = dist*net.edgeset[lid].cal_costs(prior[lid] + step * dist)
        idiv += cost
    return idiv
