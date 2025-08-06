'''
The time complexity of Dijkstra's algorithm is O((V + E) * log V), 
    where V is the number of vertices (nodes) and E is the number of edges in the graph.
        O(V) - visiting each node
        O(E) - iterating through all the edges
        log V - the priority queue operations (insertion and extraction of the minimum element)
'''

import heapq

def dijkstra(graph, start):
    # Step 1: Initialize the distance array and priority queue
    distances = {node: float('inf') for node in graph}  # Set initial distances to infinity
    distances[start] = 0  # Distance to start node is 0
    priority_queue = [(0, start)]  # Start with the source node in the priority queue (distance, node)
    
    while priority_queue:
        # Step 2: Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the stored one, we skip processing
        if current_distance > distances[current_node]:
            continue
        
        # Step 3: Relax the edges of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If the new distance is shorter, update the distance and push the neighbor into the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],  # A -> B (1), A -> C (4)
    'B': [('A', 1), ('C', 2), ('D', 5)],  # B -> A (1), B -> C (2), B -> D (5)
    'C': [('A', 4), ('B', 2), ('D', 1)],  # C -> A (4), C -> B (2), C -> D (1)
    'D': [('B', 5), ('C', 1)]  # D -> B (5), D -> C (1)
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)