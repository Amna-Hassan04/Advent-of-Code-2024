def transform_stone(stone):
    # Rule 1: If stone is 0, replace with 1
    if stone == 0:
        return [1]
    
    # Convert to string to check number of digits
    stone_str = str(stone)
    
    # Rule 2: If even number of digits, split into two stones
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    
    # Rule 3: Multiply by 2024
    return [stone * 2024]

def simulate_blinks(stones, num_blinks):
    current_stones = stones.copy()
    
    for blink in range(num_blinks):
        new_stones = []
        for stone in current_stones:
            new_stones.extend(transform_stone(stone))
        current_stones = new_stones
        
    return current_stones

def main():
    # Read input from file
    with open('input.txt', 'r') as file:
        # Read the first line and split by whitespace
        initial_stones = list(map(int, file.readline().strip().split()))
    
    # Simulate 25 blinks
    final_stones = simulate_blinks(initial_stones, 25)
    
    # Print the result
    print(f"Number of stones after 25 blinks: {len(final_stones)}")

if __name__ == "__main__":
    main()