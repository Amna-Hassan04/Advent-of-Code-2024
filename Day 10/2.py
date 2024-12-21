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

def count_distinct_trails(height_map, start, cache=None):
    if cache is None:
        cache = {}
    
    rows, cols = len(height_map), len(height_map[0])
    
    def dfs(pos):
        # If we've seen this position before, return its cached value
        if pos in cache:
            return cache[pos]
        
        r, c = pos
        current_height = height_map[r][c]
        
        # If we've reached height 9, we've found one valid trail
        if current_height == 9:
            return 1
            
        total_trails = 0
        
        # Try all possible next steps
        for next_pos in get_neighbors(pos, rows, cols):
            next_r, next_c = next_pos
            next_height = height_map[next_r][next_c]
            
            # Only follow path if it increases by exactly 1
            if next_height == current_height + 1:
                total_trails += dfs(next_pos)
        
        # Cache the result for this position
        cache[pos] = total_trails
        return total_trails
    
    return dfs(start)

def solve_hiking_trails_part2(filename):
    # Read the height map from file
    height_map = read_map(filename)
    
    # Find all trailheads (positions with height 0)
    trailheads = find_trailheads(height_map)
    
    # Calculate rating for each trailhead
    total_rating = 0
    cache = {}  # Share cache across all trailheads for better performance
    
    for i, trailhead in enumerate(trailheads):
        rating = count_distinct_trails(height_map, trailhead, cache)
        print(f"Trailhead {i+1} at position {trailhead}: Rating = {rating}")
        total_rating += rating
    
    return total_rating

if __name__ == "__main__":
    # Replace 'input.txt' with your actual input file name
    filename = 'input.txt'
    total_rating = solve_hiking_trails_part2(filename)
    print(f"\nSum of all trailhead ratings: {total_rating}")