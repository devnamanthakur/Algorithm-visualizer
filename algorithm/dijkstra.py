import heapq

def dijkstra(graph, start, visualize_step=None):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    queue = [(0, start)]
    
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_node in visited:
            continue
        visited.add(curr_node)
        
        if visualize_step:
            # Call visualizer after each node is finalized
            visualize_step(dict(distances), set(visited), curr_node)

        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances