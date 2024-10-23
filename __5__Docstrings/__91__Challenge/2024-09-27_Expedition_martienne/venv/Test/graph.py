from heapq import heapify, heappop, heappush

graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}

class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph  # A dictionary for the adjacency list

   def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
       self.graph[node1][node2] = weight  # Else, add a connection to its neighbor


    # The add_edge method omitted for space

   def shortest_distances(self, source: str):
       # Initialize the values of all nodes with infinity
       distances = {node: float("inf") for node in self.graph}
       print(distances)
       distances[source] = 0  # Set the source value to 0

       # Initialize a priority queue
       priority_queue = [(0, source)] # Point de départ
       # print(f"priority queue: {priority_queue}")
       heapify(priority_queue) # Transform priority queue in tuple

       # Create a set to hold visited nodes
       visited = set()

       while priority_queue:  # While the priority queue isn't empty
           current_distance, current_node = heappop(priority_queue)  # Get the node with the min distance
           print(f"Current distance: {current_distance} Current node: {current_node}") # Affiche 0 point de départ

           if current_node in visited:
               continue  # Skip already visited nodes
           visited.add(current_node)  # Else, add the node to visited set

           print(f"graph current node: {self.graph[current_node]}") # Affiche les prochains points et leurs distances
           for neighbor, weight in self.graph[current_node].items():
               # Calculate the distance from current_node to the neighbor
               tentative_distance = current_distance + weight
               if tentative_distance < distances[neighbor]:
                   distances[neighbor] = tentative_distance
                   heappush(priority_queue, (tentative_distance, neighbor))

       return distances


G = Graph(graph)
# Sneak-peek - find the shortest paths from B
distances = G.shortest_distances("B")
print(distances, "\n")

to_F = distances["F"]
print(f"The shortest distance from B to F is {to_F}")
