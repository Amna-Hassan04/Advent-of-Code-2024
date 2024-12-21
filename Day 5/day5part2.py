from collections import defaultdict, deque

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

def topological_sort(rules, update):
    """Sort pages in an update based on the rules."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    # Build the graph and in-degree for pages in the current update
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sort
    queue = deque([node for node in pages_in_update if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def calculate_middle_sum_part_two(rules, updates):
    total_sum = 0
    for update in updates:
        if not is_update_valid(rules, update):
            # Reorder the update using topological sort
            sorted_update = topological_sort(rules, update)
            middle_index = len(sorted_update) // 2
            total_sum += sorted_update[middle_index]

    return total_sum
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

    # Part 1: Correctly ordered updates
    part1_sum = calculate_middle_sum(rules, updates)
    print("Part 1: Sum of middle page numbers for correctly ordered updates:", part1_sum)

    # Part 2: Reorder and process incorrectly ordered updates
    part2_sum = calculate_middle_sum_part_two(rules, updates)
    print("Part 2: Sum of middle page numbers after reordering incorrectly ordered updates:", part2_sum)

if __name__ == "__main__":
    main()
