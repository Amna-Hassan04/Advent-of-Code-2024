from collections import deque
import sys

# Define constants
XOR = 'XOR'
AND = 'AND'
OR = 'OR'

# Read input from a file
input_file = "input.txt"  # Specify your input file name
try:
    with open(input_file, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

# Parse the file content
g = {}
rg = {}

# Helper function to determine min and max
minmax = lambda _a, _b: (_a, _b) if _a <= _b else (_b, _a)

# Parse the input lines
try:
    lines = content.split('\n\n')
    if len(lines) < 2:
        raise ValueError("Invalid input format: Missing expected sections.")
    for line in lines[1].splitlines():
        parts = line.split()
        if len(parts) != 5:
            print(f"Skipping invalid line: {line}")
            continue
        a, op, b, _, c = parts
        a, b = minmax(a, b)
        g[a, b, op] = c
        rg[c] = a, b, op
except Exception as e:
    print(f"Error parsing input: {e}")
    sys.exit(1)

# Define the swap function
def swap(_a, _b):
    if _a in rg and _b in rg:
        rg[_a], rg[_b] = rg[_b], rg[_a]
        g[rg[_a]], g[rg[_b]] = g[rg[_b]], g[rg[_a]]
    else:
        print(f"Error in swapping: {_a} or {_b} not found.")

# Initialize variables
output = set()
c = ''

try:
    max_index = max(
        int(key[1:]) for key in rg.keys() if key[1:].isdigit()
    )
except ValueError:
    print("Error: Unable to determine the maximum index in rg keys.")
    sys.exit(1)

# Main processing loop
for i in range(max_index):
    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'
    zn = f'z{i + 1:02}'

    try:
        xxy = g.get((x, y, XOR), None)
        xay = g.get((x, y, AND), None)

        if xxy is None or xay is None:
            print(f"Missing keys for ({x}, {y}): XOR or AND")
            continue

        if not c:
            c = xay
        else:
            a, b = minmax(c, xxy)
            k = a, b, XOR

            if k not in g:
                if z not in rg:
                    print(f"Error: {z} not found in rg.")
                    continue
                diff = list(set(rg[z][:2]) ^ set(k[:2]))
                if len(diff) == 2:
                    a, b = diff
                    output.add(a)
                    output.add(b)
                    swap(a, b)
                else:
                    print(f"Error computing symmetric difference for {k} and {z}.")
            elif g[k] != z:
                output.add(g[k])
                output.add(z)
                swap(z, g[k])

            if z in rg:
                k = rg[z]

            try:
                c = g[minmax(c, xxy)[0], minmax(c, xxy)[1], AND]
                c = g[minmax(c, xay)[0], minmax(c, xay)[1], OR]
            except KeyError as e:
                print(f"KeyError during computation: {e}")
                continue

    except KeyError as e:
        print(f"KeyError: {e}")
        continue

# Output the result
print(','.join(sorted(output)))
