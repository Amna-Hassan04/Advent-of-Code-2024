def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Directions (dx, dy): horizontal, vertical, diagonal (all directions)
    directions = [
        (0, 1),  # Horizontal (right)
        (1, 0),  # Vertical (down)
        (1, 1),  # Diagonal (down-right)
        (1, -1),  # Diagonal (down-left)
        (0, -1),  # Horizontal (left)
        (-1, 0),  # Vertical (up)
        (-1, -1),  # Diagonal (up-left)
        (-1, 1)   # Diagonal (up-right)
    ]

    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                # Check if the word can fit in the current direction
                if 0 <= row + (word_length - 1) * dx < rows and 0 <= col + (word_length - 1) * dy < cols:
                    # Extract the word in the current direction
                    found_word = "".join(
                        grid[row + i * dx][col + i * dy] for i in range(word_length)
                    )
                    if found_word == word:
                        count += 1

    return count


def main():
    # Read input from a file
    input_file = "day4input.txt"  # Replace with your input file name
    with open(input_file, "r") as f:
        grid = [line.strip() for line in f]

    # Count occurrences of "XMAS"
    result = count_xmas(grid)

    # Print the result
    print(f"The word 'XMAS' appears {result} times.")


if __name__ == "__main__":
    main()
