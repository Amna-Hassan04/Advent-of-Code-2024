import math

def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n\n")

    machines = []
    for block in data:
        lines = block.split("\n")
        button_a = tuple(map(int, lines[0].split("X+")[1].split(", Y+")))
        button_b = tuple(map(int, lines[1].split("X+")[1].split(", Y+")))
        prize = tuple(map(int, lines[2].split("X=")[1].split(", Y=")))
        machines.append((button_a, button_b, prize))

    return machines

def solve_claw_machine(button_a, button_b, prize):
    a, c = button_a
    b, d = button_b
    X, Y = prize

    min_cost = float('inf')
    best_na, best_nb = None, None

    # Iterate over possible n_A values
    for n_A in range(101):
        rem_x = X - n_A * a
        rem_y = Y - n_A * c

        if rem_x % b == 0 and rem_y % d == 0:
            n_B_x = rem_x // b
            n_B_y = rem_y // d

            if n_B_x == n_B_y and n_B_x >= 0:
                cost = 3 * n_A + n_B_x
                if cost < min_cost:
                    min_cost = cost
                    best_na, best_nb = n_A, n_B_x

    return min_cost if best_na is not None else None

def main(file_path):
    machines = parse_input(file_path)
    total_cost = 0
    prizes_won = 0

    for button_a, button_b, prize in machines:
        result = solve_claw_machine(button_a, button_b, prize)
        if result is not None:
            total_cost += result
            prizes_won += 1

    print(f"Prizes Won: {prizes_won}")
    print(f"Minimum Tokens Spent: {total_cost}")

# Example usage
main("input.txt")



def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_solution(a1, a2, b1, b2, target_x, target_y):
    print(f"\nSolving for equations:")
    print(f"{a1}A + {b1}B = {target_x}")
    print(f"{a2}A + {b2}B = {target_y}")

    # Calculate determinant
    det = a1 * b2 - a2 * b1

    if det == 0:
        print("No solution - equations are dependent")
        return None

    # Using Cramer's rule
    n = (target_x * b2 - target_y * b1) / det
    m = (a1 * target_y - a2 * target_x) / det

    # Check if solution is integer and non-negative
    if n != int(n) or m != int(m) or n < 0 or m < 0:
        print(f"No valid solution: A={n}, B={m}")
        return None

    n = int(n)
    m = int(m)

    # Verify solution
    if (a1 * n + b1 * m == target_x) and (a2 * n + b2 * m == target_y):
        print(f"Found solution: A={n}, B={m}")
        return (n, m)

    return None

def solve_claw_machines_part2(input_data):
    total_tokens = 0
    possible_prizes = 0
    OFFSET = 10000000000000

    lines = input_data.strip().split('\n')

    for i in range(0, len(lines), 4):
        if i + 2 >= len(lines):
            break

        print(f"\nProcessing Machine {i//4 + 1}")

        # Parse input
        a_line = lines[i].strip()
        ax = int(a_line[a_line.find('X+')+2:a_line.find(',')])
        ay = int(a_line[a_line.find('Y+')+2:])

        b_line = lines[i+1].strip()
        bx = int(b_line[b_line.find('X+')+2:b_line.find(',')])
        by = int(b_line[b_line.find('Y+')+2:])

        p_line = lines[i+2].strip()
        px = int(p_line[p_line.find('X=')+2:p_line.find(',')]) + OFFSET
        py = int(p_line[p_line.find('Y=')+2:]) + OFFSET

        print(f"Button A: X+{ax}, Y+{ay}")
        print(f"Button B: X+{bx}, Y+{by}")
        print(f"Prize: X={px}, Y={py}")

        # Find solution
        solution = find_solution(ax, ay, bx, by, px, py)

        if solution:
            n, m = solution
            tokens = 3 * n + m
            total_tokens += tokens
            possible_prizes += 1
            print(f"Solution found for Machine {i//4 + 1}:")
            print(f"Button A presses: {n}")
            print(f"Button B presses: {m}")
            print(f"Tokens needed: {tokens}")
        else:
            print(f"No solution found for Machine {i//4 + 1}")

    return total_tokens, possible_prizes

# Sample input
sample_input = """



"""

# Run with sample input
print("Running with sample input:")
total_tokens, possible_prizes = solve_claw_machines_part2(sample_input)
print("\nFinal Results:")
print(f"Total possible prizes: {possible_prizes}")
print(f"Total tokens needed: {total_tokens}")