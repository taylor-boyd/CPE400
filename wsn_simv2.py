from collections import defaultdict 

# IDEA 2
# Get all possible routes from source to destination
# To some calculations to find the least energy consumed power for each node
# Refer to IDEA 1 of wsn_sim.py for some ideas
# Pick the possible route that has the least amount of energy consumed

# Pretty good because we don't have to find the energy consumed for each node i don't think?
# Distance is euclidean distance, should distance be energy consumed or some other metric?

# From here
# https://www.geeksforgeeks.org/find-paths-given-source-destination/
# Should probably change so we aren't accused of cheating LOL
class Node():

    def __init__(self, energy, transmit_pwr, processing_pwr):
        self.energy = energy
        self.transmit_pwr = transmit_pwr
        self.processing_pwr = processing_pwr

class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):

        visited[u] = True
        path.append(u)
        
        # If node equals destination
        if u == d:
            print (path)
        else:

            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):
        visited = [False] * (self.V)

        path = []

        self.printAllPathsUtil(s, d, visited, path)

        print("GRAPH:" , self.graph)

# This is graph similar to what i posted in discord
g = Graph(8)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,7)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,7)
g.addEdge(4,6)
g.addEdge(5,6)

s = 0 ; d = 4
g.printAllPaths(s, d)
