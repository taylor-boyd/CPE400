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

    hub = nodes[0]
    one_hop = []
    for n in nodes:
        if n.transmit_pwr > hub.transmit_pwr:
            hub = n
        else:
            one_hop.append(n)

    return hub, one_hop

# 'runs' the network / starts sending packets
def sendPackets(hub, one_hop, dest):

    packets = 0 # var for how many packets were sent before failure

    # parameter is how many vertices (nodes)
    #g = Graph(2)
    # node 0 can go to node 1
    #g.addEdge(0,1)
    #s = 0 ; d = 1
    #g.printAllPaths(s, d)

    return packets

# destination / gateway variable
# val at each index is dest's dist from node (node # = index)
dest = [2, 10, 12, 3]

# sensor nodes - I set processing_pwr to 0 for all of them 
# cuz i haven't implement it yet
n0 = Node(10, 5, 0, [0, 2, 3, 5])
n1 = Node(8, 5, 0, [2, 0, 2, 6])
n2 = Node(3, 3, 0, [3, 2, 0, 10])
n3 = Node(8, 5, 0, [5, 6, 10, 0])

# list of nodes so it's easy to pass them to a function
nodes = [n0, n1, n2, n3]

# create initial network layout
hub, one_hop = layout(nodes)

# start sending packets
total_packets = 0
total_packets.append(sendPackets(hub, one_hop))