import re

def calculate_multiplication_with_conditions(input_file):
    with open(input_file, 'r') as file:
        data = file.read()
    
    # Combined regex to match all relevant instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)|do\(\)|don't\(\)"
    matches = re.finditer(pattern, data)

    # Track whether mul instructions are enabled
    enabled = True
    total = 0

    for match in matches:
        if match.group(0).startswith("mul"):  # Check if it's a mul(X, Y) instruction
            if enabled:  # Only process if enabled
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y
        elif match.group(0) == "do()":  # do() instruction
            enabled = True
        elif match.group(0) == "don't()":  # don't() instruction
            enabled = False

    print("Total sum of all enabled multiplications:", total)

# Example usage
input_file = "inputday3.txt"  # Replace with your input file path
calculate_multiplication_with_conditions(input_file)
