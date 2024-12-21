from collections import deque
from typing import List, Set, Tuple

def read_input(filename: str) -> List[List[str]]:
    """Read the garden plot map from a file."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

def find_regions(grid: List[List[str]]) -> List[Set[Tuple[int, int]]]:
    """Find all distinct regions in the grid using BFS."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []
    
    def bfs(start_r: int, start_c: int, plant_type: str) -> Set[Tuple[int, int]]:
        """BFS to find all connected plots of the same plant type."""
        queue = deque([(start_r, start_c)])
        region = set()
        
        while queue:
            r, c = queue.popleft()
            if (r, c) in region:
                continue
                
            region.add((r, c))
            # Check all 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < rows and 0 <= new_c < cols and 
                    grid[new_r][new_c] == plant_type and 
                    (new_r, new_c) not in region):
                    queue.append((new_r, new_c))
        return region
    
    # Find all regions
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region = bfs(r, c, grid[r][c])
                visited.update(region)
                regions.append(region)
    
    return regions

def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[List[str]]) -> int:
    """Calculate the perimeter of a region."""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for r, c in region:
        # Check all 4 sides
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            # If outside grid or different plant type, add to perimeter
            if (new_r < 0 or new_r >= rows or 
                new_c < 0 or new_c >= cols or 
                (new_r, new_c) not in region):
                perimeter += 1
    
    return perimeter

def calculate_total_price(grid: List[List[str]]) -> int:
    """Calculate the total price of fencing all regions."""
    regions = find_regions(grid)
    total_price = 0
    
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region, grid)
        price = area * perimeter
        total_price += price
    
    return total_price

def main():
    # Read input from file
    grid = read_input('input.txt')
    
    # Calculate and print the result
    result = calculate_total_price(grid)
    print(f"Total price of fencing all regions: {result}")

if __name__ == "__main__":
    main()