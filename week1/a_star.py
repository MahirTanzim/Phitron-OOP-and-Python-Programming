import heapq

graph = {
    's': {'a': 5, 'c': 6, 'd': 6},
    'a': {'b': 3, 'g': 9},
    'b': {'h': 5},
    'c': {'b': 1, 'f': 7},
    'd': {'c': 2, 'e': 2},
    'e': {'i': 7},
    'f': {'i': 8},
    'g': {},
    'h': {},
    'i': {}
}
heuristic = {
    's': 5, 'a': 7, 'b': 3, 'c': 4, 'd': 6, 'e': 5,
    'f': 6, 'g': 12, 'h': 11, 'i': 0
}

def a_star_search(start, goal):
    priority_queue = []  
    heapq.heappush(priority_queue, (heuristic[start], 0, start, []))  
    visited = {}
    
    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)
        
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        path = path + [node]
        
        if node == goal:
            return path, g  
        
        for neighbor, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(priority_queue, (new_f, new_g, neighbor, path))
    
    return None, float('inf')  

# Run A* Search
path, cost = a_star_search('s', 'i')
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)
