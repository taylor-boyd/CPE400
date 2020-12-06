from collections import defaultdict 

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

# takes in graph of nodes (so node items and their distances from each other)
# returns network layout
# we can also use this function to update/change the layout as energy depletes
def layout(graph):
    network = [] 
    # ^idk what data structure would be best here, we basically 
    # need to store which nodes will serve as hubs and which 
    # nodes report to each hub
    # I think all the 'hubs' will need to have the transmission power
    # to communicate w one another so that info can come from 
    # anywhere and travel to anywhere 

    return network

#def optimalPath()

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
