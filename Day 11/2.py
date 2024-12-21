from collections import defaultdict
import math

def count_digits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1

def transform_and_count(stones_count):
    """
    Instead of tracking individual stones, track count of each type
    Returns a dictionary with new counts after transformation
    """
    new_counts = defaultdict(int)
    
    for stone, count in stones_count.items():
        if stone == 0:
            new_counts[1] += count
        else:
            digits = count_digits(stone)
            if digits % 2 == 0:
                # Split the number
                stone_str = str(stone)
                mid = digits // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
    
    return new_counts

def simulate_blinks_optimized(initial_stones, num_blinks):
    # Initialize counts dictionary
    stones_count = defaultdict(int)
    for stone in initial_stones:
        stones_count[stone] += 1
    
    total_stones = []  # Track stone count at each step for pattern detection
    
    for blink in range(num_blinks):
        stones_count = transform_and_count(stones_count)
        current_total = sum(stones_count.values())
        total_stones.append(current_total)
        
        # Print progress every 5 blinks
        if (blink + 1) % 5 == 0:
            print(f"After {blink + 1} blinks: {current_total} stones")
            
        # Check for patterns every 10 steps after first 20 blinks
        if blink >= 20 and blink % 10 == 0:
            # Look for multiplicative pattern in last few steps
            last_ratios = [total_stones[i] / total_stones[i-1] 
                          for i in range(len(total_stones)-5, len(total_stones))]
            
            # If ratios are consistent (pattern found)
            if len(set([round(r, 6) for r in last_ratios])) == 1:
                growth_ratio = last_ratios[-1]
                remaining_blinks = num_blinks - (blink + 1)
                final_count = int(current_total * (growth_ratio ** remaining_blinks))
                print(f"\nPattern detected! Growth ratio: {growth_ratio}")
                print(f"Projecting final count...")
                return final_count
    
    return sum(stones_count.values())

def main():
    # Read input from file
    with open('input.txt', 'r') as file:
        initial_stones = list(map(int, file.readline().strip().split()))
    
    print("Starting optimized simulation...")
    print(f"Initial stones: {len(initial_stones)}")
    
    result = simulate_blinks_optimized(initial_stones, 75)
    
    print(f"\nFinal result:")
    print(f"Number of stones after 75 blinks: {result}")

if __name__ == "__main__":
    main()