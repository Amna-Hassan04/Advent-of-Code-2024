def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')

    rules = []
    updates = []
    reading_updates = False

    for line in lines:
        if line == '':
            reading_updates = True
            continue

        if reading_updates:
            updates.append(list(map(int, line.split(','))))
        else:
            x, y = map(int, line.split('|'))
            rules.append((x, y))

    return rules, updates

def is_update_valid(rules, update):
    position = {page: i for i, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position:
            if position[x] > position[y]:
                return False

    return True

def calculate_middle_sum(rules, updates):
    total_sum = 0

    for update in updates:
        if is_update_valid(rules, update):
            middle_index = len(update) // 2
            total_sum += update[middle_index]

    return total_sum

def main():
    input_file = 'day5input.txt'  # Replace with your input file path
    rules, updates = parse_input(input_file)

    result = calculate_middle_sum(rules, updates)
    print("Sum of middle page numbers for correctly ordered updates:", result)

if __name__ == "__main__":
    main()
