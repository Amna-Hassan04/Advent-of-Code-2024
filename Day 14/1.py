# Part 2
import numpy as np
from typing import List, Tuple

def parse_input(filename: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Parse input file to extract robot positions and velocities.

    Args:
        filename (str): Path to input file

    Returns:
        List of tuples, each containing (position, velocity)
    """
    robots = []
    with open(filename, 'r') as f:
        for line in f:
            pos_str, vel_str = line.strip().split(' ')
            px, py = map(int, pos_str[2:].split(','))
            vx, vy = map(int, vel_str[2:].split(','))
            robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robots(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]],
                    time: int,
                    width: int,
                    height: int) -> np.ndarray:
    """
    Simulate robot movements and count robot positions after given time.

    Args:
        robots (List): List of robot (position, velocity) tuples
        time (int): Seconds to simulate
        width (int): Space width
        height (int): Space height

    Returns:
        numpy array of robot count per tile
    """
    # Initialize grid to track robot positions
    grid = np.zeros((height, width), dtype=int)

    for (px, py), (vx, vy) in robots:
        # Calculate final position after time, with wraparound
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        grid[final_y, final_x] += 1

    return grid

def is_christmas_tree(grid: np.ndarray) -> bool:
    """
    Check if the robot positions form a Christmas tree pattern.

    Args:
        grid (numpy array): Robot position grid

    Returns:
        Boolean indicating if a Christmas tree pattern is found
    """
    # Define a potential Christmas tree pattern
    # This is a simplistic representation and might need adjustment
    # based on the actual expected pattern
    tree_pattern = [
        [0, 0, 1, 0, 0],   # top of tree
        [0, 1, 1, 1, 0],   # middle of tree
        [1, 1, 1, 1, 1],   # base of tree
    ]

    height, width = grid.shape

    # Search for the pattern in the grid
    for y in range(height - len(tree_pattern)):
        for x in range(width - len(tree_pattern[0])):
            # Check if this section matches the tree pattern
            match = True
            for dy, row in enumerate(tree_pattern):
                for dx, val in enumerate(row):
                    if val == 1 and grid[y+dy, x+dx] == 0:
                        match = False
                        break
                if not match:
                    break

            if match:
                return True

    return False

def find_christmas_tree_time(filename: str, max_time: int = 10000, width: int = 101, height: int = 103) -> int:
    """
    Find the earliest time when robots form a Christmas tree pattern.

    Args:
        filename (str): Input file path
        max_time (int): Maximum time to search
        width (int): Space width
        height (int): Space height

    Returns:
        Time when Christmas tree pattern is found, or -1 if not found
    """
    # Parse input
    robots = parse_input(filename)

    # Search for Christmas tree pattern
    for time in range(max_time):
        # Simulate robot positions
        grid = simulate_robots(robots, time, width, height)

        # Check for Christmas tree pattern
        if is_christmas_tree(grid):
            return time

    return -1  # No pattern found within max_time

# Solve problem
result = find_christmas_tree_time('input.txt')
print(f"Seconds until Christmas Tree Pattern: {result}")
# Part 1
# Constants for the grid dimensions
grid_width = 101
grid_height = 103
time_limit = 100

# Function to determine the quadrant of a robot based on its position
def get_quadrant(x, y):
    if x == grid_width // 2 or y == grid_height // 2:
        return None  # On the middle line, not in any quadrant
    elif x < grid_width // 2 and y < grid_height // 2:
        return 1  # Top-left quadrant
    elif x >= grid_width // 2 and y < grid_height // 2:
        return 2  # Top-right quadrant
    elif x < grid_width // 2 and y >= grid_height // 2:
        return 3  # Bottom-left quadrant
    elif x >= grid_width // 2 and y >= grid_height // 2:
        return 4  # Bottom-right quadrant

# Read input from the file
def read_input(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                pos_part, vel_part = line.split()
                px, py = map(int, pos_part[2:].split(','))
                vx, vy = map(int, vel_part[2:].split(','))
                robots.append(((px, py), (vx, vy)))
    return robots

# Simulate the motion of robots and calculate the safety factor
def calculate_safety_factor(robots, time_limit):
    # Update positions after 100 seconds
    for i in range(len(robots)):
        (px, py), (vx, vy) = robots[i]
        px = (px + vx * time_limit) % grid_width
        py = (py + vy * time_limit) % grid_height
        robots[i] = ((px, py), (vx, vy))

    # Count robots in each quadrant
    quadrant_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    for (px, py), _ in robots:
        quadrant = get_quadrant(px, py)
        if quadrant:
            quadrant_counts[quadrant] += 1

    # Calculate the safety factor
    safety_factor = (quadrant_counts[1] * quadrant_counts[2] *
                     quadrant_counts[3] * quadrant_counts[4])
    return safety_factor

# Main function
def main():
    input_file = "input.txt"
    robots = read_input(input_file)
    safety_factor = calculate_safety_factor(robots, time_limit)
    print("Safety Factor:", safety_factor)

if __name__ == "__main__":
    main()
