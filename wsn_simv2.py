from collections import defaultdict 

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

# takes in nodes 
# returns network layout
# can use this function to update/change the layout as energy depletes
def layout(nodes):
    network = [] 

    return network

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