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

    def __init__(self, energy, transmit_pwr, processing_pwr, node_dist):
        self.energy = energy
        self.transmit_pwr = transmit_pwr
        self.processing_pwr = processing_pwr
        self.distances = node_dist

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

# takes in graph of nodes (so node items and their distances from each other)
# takes in nodes 
# returns network layout
# can use this function to update/change the layout as energy depletes
def layout(nodes):
    network = [] 

    return network

# def optimalPath()

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
# first, we'd take in a graph and create node items accordingly
# then, we'd call layout function to organize the network
# next, we'd call a function that will 'run' the network and
# choose optimal paths for each node to report to the main location
# (or gateway). It'd basically keep running until it gets to 
# some point (we have to decide what this point is) where one
# of the hub nodes is running out of energy and must be converted
# to a single-hope type. At this time, we would call the layout
# function once again to see if we can rearrange the network
# in order to make the energy last longer
# 'runs' the network / starts sending packets
def sendPackets(network):

    packets = 0 # var for how many packets were sent before failure
    
    # parameter is how many vertices (nodes)
    #g = Graph(2)
    # node 0 can go to node 1
    #g.addEdge(0,1)
    #s = 0 ; d = 1
    #g.printAllPaths(s, d)

    return packets

# sensor nodes - I set processing_pwr to 0 for all of them 
# cuz i haven't implement it yet
n0 = Node(10, 5, 0, [0, 2, 3, 5])
n1 = Node(8, 5, 0, [2, 0, 2, 6])
n2 = Node(3, 3, 0, [3, 2, 0, 0])
n3 = Node(8, 5, 0, [5, 6, 0, 0])

# list of nodes so it's easy to pass them to a function
nodes = [n0, n1, n2, n3]

# create initial network layout
network = layout(nodes)
