from typing import List, Tuple
from itertools import product

def concatenate(a: int, b: int) -> int:
    """
    Concatenate two numbers.
    Example: concatenate(12, 345) = 12345
    """
    return int(str(a) + str(b))

def evaluate_expression(nums: List[int], operators: List[str]) -> int:
    """
    Evaluate expression with left-to-right evaluation including concatenation.
    """
    result = nums[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
        else:  # op == '||'
            result = concatenate(result, nums[i + 1])
    return result

def find_valid_expression(target: int, nums: List[int]) -> str:
    """
    Find and return the valid expression if it exists.
    """
    num_operators = len(nums) - 1
    for ops in product(['+', '*', '||'], repeat=num_operators):
        try:
            if evaluate_expression(nums, ops) == target:
                # Construct the expression string
                expression = str(nums[0])
                for i, op in enumerate(ops):
                    expression += f" {op} {nums[i + 1]}"
                return expression
        except (ValueError, OverflowError):
            # Skip invalid concatenations or overflow errors
            continue
    return ""

def parse_line(line: str) -> Tuple[int, List[int]]:
    """
    Parse input line into target value and list of numbers.
    """
    target_str, nums_str = line.strip().split(': ')
    return int(target_str), [int(x) for x in nums_str.split()]

def solve_calibration_from_file(filename: str) -> None:
    """
    Solve the calibration problem from a file and print detailed output.
    """
    try:
        with open(filename, 'r') as file:
            valid_equations = []
            total = 0
            
            print("\nProcessing equations...")
            print("-" * 50)
            
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                target, nums = parse_line(line)
                expression = find_valid_expression(target, nums)
                
                if expression:
                    valid_equations.append((target, expression))
                    total += target
                    print(f"✓ {target}: {expression} = {target}")
                else:
                    print(f"✗ {target}: No valid solution")
            
            print("-" * 50)
            print(f"\nFound {len(valid_equations)} valid equations:")
            for target, expr in valid_equations:
                print(f"  • {target} = {expr}")
            
            print(f"\nTotal calibration result: {total}")
            
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    # Read from input.txt
    input_file = "input.txt"
    solve_calibration_from_file(input_file)