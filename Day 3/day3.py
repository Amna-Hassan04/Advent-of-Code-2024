import re

def calculate_multiplication_sum(input_file):
    with open(input_file, 'r') as file:
        data = file.read()
    
    # Improved regex pattern
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    matches = re.findall(pattern, data)
    
    # Debugging: Print all matches found
    print("Valid matches found:", matches)
    
    # Compute the sum of results of all valid multiplications
    total = sum(int(x) * int(y) for x, y in matches)
    
    print("Total sum of all valid multiplications:", total)

# Example usage
input_file = "inputday3.txt"  # Replace with your input file path
calculate_multiplication_sum(input_file)
