import sys 

# IDEA 1 
# Instead of distances from each node (the weights), we make the weights
# as energy consumed from that node, so ex: weight from node A to node {NEIGHBOR}
# is energy consumated rate (or some kind of equation to tell us if we used a lot of energy at that node)
# from node A to any neighboring node. We can then find the destination with dijkstras
# by finding the path that picks the smallest energy consumed rate.

# To find that initial energy consumed rate we can use equations from the PDF ima link, and
# we can maybe use some kind of math involving the packet size * (equation involving transmission
# and processing ; all other power)

# WHAT IF (not sure if this works) we send a packet that holds the integer of the packet
# to be sent (so no big data being processed) to find the initial energy consumed rate
# for each node? Maybe!

class Node():

    def __init__(self, energy, transmit_pwr, processing_pwr):
        self.energy = energy
        self.transmit_pwr = transmit_pwr
        # Add processing power?
        self.processing_pwr = processing_pwr
        # Add any other delays? Or just these

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist, Path): 
        # First col is vertex, second is distance from src to vertex, third is prev node
        print ("Vertex \tDistance Prev Node")
        for node in range(self.V): 
            print (node, "\t", dist[node], "\t", Path[node])
    
    # Get optimal path from dijkstras yay!!
    def getOptimalPath(self, Path, src, target):
        optimalPath = []
        x = target
        optimalPath.append(Path[x])

        while (Path[x] != src):
            x = Path[x]
            optimalPath.append(Path[x])
        
        # Add target to the end
        optimalPath.reverse()
        optimalPath.append(target)
        print ("OPTIMAL PATH TO TARGET" , target,":", optimalPath)
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxsize
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src, target): 
        
        # Initialize the dist list of size V
        dist = [sys.maxsize] * self.V 
        # Initialize the shortest path
        Path = [0] * self.V
        # Set distances of source to 0
        dist[src] = 0

        # Set all of sptSet list to False
        sptSet = [False] * self.V 


        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True

  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v] 
                    # Store previous node
                    Path[v] = u

        self.printSolution(dist, Path)
        self.getOptimalPath(Path, src, target)
  
# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
 
# First is src, second is target
g.dijkstra(0, 8); 
