import random
from collections import defaultdict 
from numpy.random import randint
import numpy as np
import math

class Node():

    def __init__(self, id, energy, location):
        self.id = id
        self.energy = energy
        self.location = location
        self.routing_tbl = []
        self.hubID = -1

    def setTransmitPwr(self, transmit_pwr):
        self.transmit_pwr = transmit_pwr

    def setProcPower(self, processing_pwr):
        self.processing_pwr = processing_pwr

    def setHub(self, hubID):
        self.hubID = hubID

    # route entry will look like this: [seq.#, # of hops / energy it'll take, path]
    # # of hops / energy it'll take can def change to some other measurement of path cost
    # path will be a list so like 0 > 1 > 2 would be [0,1,2]
    def addRoute(self, route):
        routing_tbl.append(route)

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

# Function calculates distance between two points
def dist(p1, p2, d): 
      
    x = []
    for i in range(d):
        x.append(p1[i] - p2[i])
        
    tot = 0
    for i in range(d):
        tot = tot + (x[i] * x[i])
        
    return tot

# Function to find the min dist between any 2 pnts
def minDist(t, p, d):
    
    n = len(t)
    index = 0
    
    # Iterate over all possible pairs
    minm = 100
    for i in range(n):
        # Update minm and index
        di = dist(t[i], p, d)
        if di < minm:
            minm = di
            index = i
    
    # Return index of closest cluster center
    return index

def new_centers(c):

    a = []
    for i in range(len(c)):
        d = len(c[i])
    for i in range(d):
        a.append([])
    for i in range(len(c)):
        for j in range(d):
            a[j] += c[i][j]
            
    for i in range(len(a)):
        a[i] = a[i] / len(c)
        
    return a

def helper_function(X,mu):
    
    clusters = []
    cc_final = []
    for i in range(len(mu)):
        clusters.append([])
    for i in range(len(X)):
        for j in range(len(X[i])):
            center = minDist(mu, X[i][j], len(X[i][j]))
            clusters[center].append(X[i][j])
    for i in range(len(clusters)):
        cc_final.append(new_centers(clusters[i]))
        
    return clusters

def K_Means(X,K):
    
    # variable for returned final cluster centers
    cc_final = np.array([])
    
    maxm = minm = X[0][0]
    d = 0 # point dimensions
    for i in range(len(X)):
        d = len(X[i])
        for j in range(d):
            maxm = max(maxm, X[i][j])
            minm = min(minm, X[i][j])
    cc_initial = []
    for i in range(K):
        cc_initial.append(randint(minm,maxm,d))
    
    c_final = []
    centers = []
    for i in range(len(cc_initial)):
        c_final.append([])
    for i in range(len(X)):
        center = minDist(mu, X[i], len(X[i]))
        c_final[center].append(X[i])
    c_final = helper_function(c_final, cc_initial)
            
    return c_final

# takes in nodes, dest, and k (num of clusters); returns network 'layout'
# can use this function to update/change the layout as energy depletes
# or transmission power changes greatly because one of the nodes died/ran out of energy
def layout(nodes, dest, k):

    node_locs = np.zeros(shape=(len(nodes)+1, 2))
    for n in range(len(nodes)):
        node_locs[n] = nodes[n].location
    node_locs[len(nodes)] = dest
    clusters = K_Means(node_locs, k)
    
    for c in clusters:
        h = c[0] # initialize h with possible hub for cluster c
        proximity = 100
        for i in range(len(c)):
            temp = 0
            for j in range(len(c)):
                temp += dist(c[i], c[j], 2)
            for n in nodes:
                if np.all(n.location == c[i]):
                    n.setTransmitPwr(float(temp) / float(len(nodes)))
            if temp < proximity:
                proximity = temp
                for n in nodes:
                    if np.all(n.location == c[i]):
                        h = n
        for l in c:
            for n in nodes:
                if np.all(n.location == l):
                    n.setHub(h.id)

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

# destination / gateway location
dest = [5, 6]

# sensor nodes - initialized with node locations and they'll
# all start with same amount of energy
n0 = Node(0, 10, [3, 5])
n1 = Node(1, 10, [3, 1])
n2 = Node(2, 10, [1, 3])
n3 = Node(3, 10, [6, 3])

# list of nodes so it's easy to pass them to a function
nodes = [n0, n1, n2, n3]

# create initial network layout
layout(nodes, dest, 2)
print("CLUSTER 1:")
print("Hub is n" + str(nodes[0].hubID))
print("One-hop nodes are: ")
other_hub = 0
for n in nodes:
    if n.hubID == nodes[0].hubID and n.id != nodes[0].hubID:
        print("n" + str(n.id) + " ")
    elif n.hubID != nodes[0].hubID:
        other_hub = n.hubID
print("")
print("CLUSTER 2:")
print("Hub is n" + str(other_hub))
print("One-hop nodes are: ")
for n in nodes:
    if n.hubID == other_hub and n.id != other_hub:
        print("n" + str(n.id) + " ")

# start sending packets
total_packets = 0

# TO-DO: put random generation of src node and calling of sendPacket into a loop
# that breaks once no more packets can be sent aka all the nodes have no energy left

# randomly generated source node
s = random.randint(0, 3)
#print(s)
#p = sendPacket(hub, one_hop, s, dest)
#print(p)