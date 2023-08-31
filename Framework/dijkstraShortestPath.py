"""
Shortest Path Problem - Priority Queue Dijkstra 
Further description in Section 3.1 - "SPP Shortest Path Dijkstra"

"""

import heapq

class ShortestPath:
    def __init__(self, name):
        self.name = name

    # compute shortest paths with priority queue
    @staticmethod
    def dijkstra(net, source, sink):
        queue, checked = [(0, source, [])], set()
        while queue:
            (cost, v, path) = heapq.heappop(queue)
            if v not in checked:
                path = path + [v]
                checked.add(v)
                if v == sink:
                    return cost, path
                for pl in net.nodeset[v].heads:
                    heapq.heappush(queue, (cost+pl.cost, pl.pointee.id, path))