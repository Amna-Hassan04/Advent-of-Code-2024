def parse_input(file_path):
    """Read the map from the input file and return antenna positions."""
    antennas = {}
    with open(file_path, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                if char.isalnum():  # Valid antenna frequency
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((row, col))
    return antennas, row + 1, col + 1  # Include map dimensions

def calculate_antinode_positions(antennas, map_height, map_width):
    """Calculate unique antinode positions."""
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # Positions of two antennas
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate potential antinodes
                dx, dy = x2 - x1, y2 - y1
                antinode1 = (x1 - dx, y1 - dy)  # Extend backwards
                antinode2 = (x2 + dx, y2 + dy)  # Extend forwards

                # Validate antinodes within bounds
                if 0 <= antinode1[0] < map_height and 0 <= antinode1[1] < map_width:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < map_height and 0 <= antinode2[1] < map_width:
                    antinodes.add(antinode2)

    return antinodes

def count_unique_antinodes(file_path):
    """Main function to calculate the total unique antinodes."""
    antennas, map_height, map_width = parse_input(file_path)
    antinodes = calculate_antinode_positions(antennas, map_height, map_width)
    return len(antinodes)

# Input and Output
input_file = "input.txt"  # Replace with your input file path
result = count_unique_antinodes(input_file)
print("Number of Unique Locations with Antinodes:", result)
