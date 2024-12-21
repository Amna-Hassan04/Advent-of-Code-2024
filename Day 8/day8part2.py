from collections import defaultdict
from itertools import combinations

def read_grid(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def find_antennas(grid):
    # Dictionary to store positions of each frequency
    frequency_positions = defaultdict(list)
    rows, cols = len(grid), len(grid[0])
    
    # Find all antennas and group by frequency
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] not in '.#':
                frequency_positions[grid[i][j]].append((i, j))
    
    return frequency_positions

def is_aligned(p1, p2, p3):
    # Check if three points are collinear using slope formula
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    # Handle vertical lines
    if x2 - x1 == 0:
        return x3 - x1 == 0
    if x3 - x1 == 0:
        return False
        
    # Compare slopes
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y3 - y1) / (x3 - x1)
    return abs(slope1 - slope2) < 1e-10  # Use small epsilon for floating point comparison

def find_antinodes(grid):
    frequency_positions = find_antennas(grid)
    antinodes = set()
    rows, cols = len(grid), len(grid[0])
    
    # Process each frequency separately
    for frequency, positions in frequency_positions.items():
        if len(positions) < 2:
            continue
            
        # Add antenna positions as antinodes if there are multiple antennas of same frequency
        antinodes.update(positions)
        
        # Check all points in grid for alignment with antenna pairs
        for i in range(rows):
            for j in range(cols):
                current_point = (i, j)
                # Skip if already an antinode
                if current_point in antinodes:
                    continue
                    
                # Check all pairs of antennas of the same frequency
                for ant1, ant2 in combinations(positions, 2):
                    if is_aligned(ant1, ant2, current_point):
                        antinodes.add(current_point)
                        break
    
    return len(antinodes)

def solve_part2(input_filename, output_filename):
    grid = read_grid(input_filename)
    result = find_antinodes(grid)
    
    # Print result to screen
    print(f"Number of unique locations containing an antinode: {result}")
    
    # Write to file
    with open(output_filename, 'w') as f:
        f.write(str(result))
        
if __name__ == "__main__":
    solve_part2("input.txt", "output.txt")