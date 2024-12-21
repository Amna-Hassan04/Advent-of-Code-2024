from collections import deque

def read_map(filename):
    with open(filename, 'r') as f:
        return [[int(c) for c in line.strip()] for line in f if line.strip()]

def find_trailheads(height_map):
    rows, cols = len(height_map), len(height_map[0])
    return [(r, c) for r in range(rows) for c in range(cols) if height_map[r][c] == 0]

def get_neighbors(pos, rows, cols):
    r, c = pos
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    return [(r + dr, c + dc) for dr, dc in directions 
            if 0 <= r + dr < rows and 0 <= c + dc < cols]

def calculate_trailhead_score(height_map, start):
    rows, cols = len(height_map), len(height_map[0])
    reachable_nines = set()
    visited = set()
    
    # Queue stores (position, current_height)
    queue = deque([(start, 0)])
    visited.add(start)
    
    while queue:
        pos, height = queue.popleft()
        
        # If we've reached a 9, add it to reachable_nines
        if height_map[pos[0]][pos[1]] == 9:
            reachable_nines.add(pos)
            continue
            
        for next_pos in get_neighbors(pos, rows, cols):
            next_height = height_map[next_pos[0]][next_pos[1]]
            
            # Only follow path if it increases by exactly 1
            if next_height == height + 1 and next_pos not in visited:
                queue.append((next_pos, next_height))
                visited.add(next_pos)
    
    return len(reachable_nines)

def solve_hiking_trails(filename):
    # Read the height map from file
    height_map = read_map(filename)
    
    # Find all trailheads (positions with height 0)
    trailheads = find_trailheads(height_map)
    
    # Calculate score for each trailhead
    total_score = 0
    for i, trailhead in enumerate(trailheads):
        score = calculate_trailhead_score(height_map, trailhead)
        print(f"Trailhead {i+1} at position {trailhead}: Score = {score}")
        total_score += score
    
    return total_score

if __name__ == "__main__":
    # Replace 'input.txt' with your actual input file name
    filename = 'input.txt'
    total_score = solve_hiking_trails(filename)
    print(f"\nSum of all trailhead scores: {total_score}")