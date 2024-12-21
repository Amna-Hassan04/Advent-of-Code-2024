from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Step 1: Count occurrences of each number in the right list
    right_count = Counter(right_list)

    # Step 2: Calculate similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)

    return similarity_score

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

    # Calculate and print the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", similarity_score)

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except ValueError:
    print("Error: File contains invalid data. Ensure all lines have two integers separated by spaces.")
