def calculate_total_distance(left_list, right_list):
    # Step 1: Sort both lists
    left_list.sort()
    right_list.sort()

    # Step 2: Calculate distances
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance

# Read input from a file
file_path = "./inputday1.txt"

try:
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []

        # Parse each line to separate left and right numbers
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Validate input lengths
    if len(left_list) != len(right_list):
        print("Error: Both lists must have the same number of elements.")
    else:
        # Calculate and print the total distance
        total_distance = calculate_total_distance(left_list, right_list)
        print("Total Distance:", total_distance)

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except ValueError:
    print("Error: File contains invalid data. Ensure all lines have two integers separated by spaces.")
