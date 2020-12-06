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




def addEdge(u, v):
    graph[u].append(v)

def printAllPathsUtil(u, d, visited, path):

    visited[u] = True
    path.append(u)
    
    # If node equals destination
    if u == d:
        print (path)
    else:
        
        # Add path if the node hasn't been visited from source to dest
        for i in graph[u]:
            if visited[i] == False:
                printAllPathsUtil(i, d, visited, path)

    path.pop()

    visited[u] = False

def printAllPaths(s, d):
    visited = [False] * (V)

    path = []
    printAllPathsUtil(s, d, visited, path)


       

# takes in graph of nodes (so node items and their distances from each other)
# takes in nodes 
# returns network layout
# can use this function to update/change the layout as energy depletes
def layout(nodes):
   
    # Get all possible hubs and all possible one_hops
    hubs = nodes
    one_hop = []
    for n in nodes:
        # If any other node is greater than example hub, than that hub should be the node
        if n.transmit_pwr > hub.transmit_pwr:
            hub = n
        else:
            # Else small power can only do one hop
            one_hop.append(n)

    return hub, one_hop

# def optimalPath()


def sendPackets(hub, one_hop):

    packets = 0 # var for how many packets were sent before failure

    return packets


# def getOptimalPaths(nodes, src, dest):



V = 4
graph = defaultdict(list)

possiblePaths = []



# sensor nodes - I set processing_pwr to 0 for all of them 
# cuz i haven't implement it yet

# Last column is node distances from each node, 0 means 0 away from node at index
# n0 = Node(10, 5, 3, [0, 2, 3, 5])
# n1 = Node(8, 5, 3, [2, 0, 2, 6])
# n2 = Node(3, 3, 1, [3, 2, 0, 0])
# n3 = Node(8, 5, 2, [5, 6, 0, 0])

n0 = Node(10, 5, 3, [1,2,3])
n1 = Node(8,5,3, [0,2,3])
n2 = Node(3,3,1, [0,1])
n3 = Node(8,5,2,[0,1])


# IDEALLY I WANT TO USE THE ADJACENCY MATRIX TO GET ALL POSSIBLE PATHS, BUT IM TOO SMALL BRAIN
# SO I USED THIS

addEdge(0,1)
addEdge(0,2)
addEdge(0,3)
addEdge(1,0)
addEdge(1,2)
addEdge(1,3)
addEdge(2,0)
addEdge(2,1)
addEdge(3,0)
addEdge(3,1)

Source = 0 
Destination = 3

# print ("POSSIBLE: ", possiblePaths)
# list of nodes so it's easy to pass them to a function
nodes = [n0, n1, n2, n3]
nodesDistanceList = []
nodesDistanceList.append(n0.distances)
nodesDistanceList.append(n1.distances)
nodesDistanceList.append(n2.distances)
nodesDistanceList.append(n3.distances)

possiblePaths = [[]]
printAllPaths(Source,Destination)

print ("GRAPH IS: ", graph)

# getOptimalPaths(nodesDistanceList,0, 3)


# create initial network layout
network = layout(nodes)
hub, one_hop = layout(nodes)

# start sending packets
total_packets = 0

# First packet 
firstPacketTEST = 768 # 768 bytes


