from collections import deque
def bfs():
    queue, visited = deque([((3, 3, 0), [])]), set()
    while queue:
        (m, c, b), p = queue.popleft()
        if (m, c, b) == (0, 0, 1): return p + [(m, c, b)]
        if (m, c, b) in visited: continue
        visited.add((m, c, b))
        for nm, nc, nb in [(m-2, c, 1-b), (m, c-2, 1-b), (m-1, c-1, 1-b), (m-1, c, 1-b), (m, c-1, 1-b)]:
            if 0 <= nm <= 3 and 0 <= nc <= 3 and (nm >= nc or nm == 0) and (3 - nm >= 3 - nc or 3 - nm == 0):
                queue.append(((nm, nc, nb), p + [(m, c, b)]))
    return None
path = bfs()
if path: 
    for step in path: 
        print(f"Missionaries: {step[0]}, Cannibals: {step[1]}, Boat: {'Left' if step[2] == 0 else 'Right'}")
else: 
    print("No solution found!")
