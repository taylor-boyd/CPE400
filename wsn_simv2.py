import random
from collections import defaultdict 

# TO-DO: Add a routing table (probably should just be a list of lists to keep it simple) to 
# the node class so that we can begin to implement RREQ stuff
class Node():

    def __init__(self, id, energy, node_dist):
        self.id = id
        self.energy = energy
        self.distances = node_dist

    def setTransmitPwr(self, transmit_pwr):
        self.transmit_pwr = transmit_pwr

    def setProcPower(self, processing_pwr):
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

# takes in nodes; returns network 'layout'
# can use this function to update/change the layout as energy depletes
# or transmission power changes greatly because one of the nodes died/ran out of energy
def layout(nodes):

    hub = nodes[0]
    proximity = 100
    one_hop = []
    # adds up all the vals in each node's distance vector to see which node
    # is closest to the most nodes (the smallest sum means it's closest) and
    # will therefore use the least transmit pwr overall and serve as a good
    # initial hub
    for n in nodes:
        temp = 0
        for d in n.distances:
            temp += d
        # just an idea on how to init transmit power for all nodes so that
        # nodes close to a lot of others end up using less transmit pwr
        # like they're supposed to 
        n.setTransmitPwr(float(temp) / float(len(nodes))) # set transmit pwr to average dist from other nodes
        if temp < proximity:
            hub = n
            proximity = temp
    for n in nodes: # all other nodes become one-hop nodes
        if n != hub:
            one_hop.append(n)

    return hub, one_hop

# TO-DO: we need to add something in the sendPacket function or maybe outside when we call it
# to check for some threshold being hit to where we'd wanna change the layout. I'm thinking the
# threshold would be one of the nodes having low energy (let's say energy=2) so we'd call layout
# to a) change it from hub to one-hop if it's a hub to start or b) perhaps create another hub, one
# much closer to the dying node so that it can continue to send packets at a lower transmission
# power

# 'runs' the network / starts sending packets
def sendPacket(hub, one_hop, src, dest):

    packets = 0 # var for how many packets were sent before failure
    packet_size = 512 # let's say all packets being sent are of size 512 B

    # there is only one hub to start so it's the only one that can go
    # to destination, all the other nodes can only send info to hub
    hub.energy -= (packet_size * (hub.transmit_pwr / 1000))
    if src != hub.id:
        for n in one_hop:
            # find which node is source
            if src == n.id:
                # update energy left after packet is sent
                n.energy -= (packet_size * (n.transmit_pwr / 1000))
                # make sure there was enough energy to send it
                if n.energy >= 0 and hub.energy >= 0:
                    packets +=1 # energy left >= 0 so packet was sent successfully
    else:
        if hub.energy >= 0:
            packets += 1

    # this would be used if we had more than one hub because there 
    # would be multiple routes to dest
    #g = Graph(5)
    # add path from node 0 to node 1
    #g.addEdge(0,1)
    #s = 0 ; d = 1
    #g.printAllPaths(s, d)

    return packets

# destination / gateway variable
# val at each index is dest's dist from node (node # = index)
dest = [2, 10, 12, 3]

# sensor nodes - initialized with distances to other nodes and
# all start with same amount of energy
n0 = Node(0, 10, [0, 2, 3, 5])
n1 = Node(1, 10, [2, 0, 2, 6])
n2 = Node(2, 10, [3, 2, 0, 10])
n3 = Node(3, 10, [5, 6, 10, 0])

# list of nodes so it's easy to pass them to a function
nodes = [n0, n1, n2, n3]

# create initial network layout
hub, one_hop = layout(nodes)

# start sending packets
total_packets = 0

# TO-DO: put random generation of src node and calling of sendPacket into a loop
# that breaks once no more packets can be sent aka all the nodes have no energy left

# randomly generated source node
s = random.randint(0, 3)
print(s)
p = sendPacket(hub, one_hop, s, dest)
print(p)