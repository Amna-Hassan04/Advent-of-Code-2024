def is_safe(report):
    """
    Determines if a report is safe based on the following rules:
    1. Levels must be either all increasing or all decreasing.
    2. Any two adjacent levels must differ by at least 1 and at most 3.
    """
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are positive (increasing) or all are negative (decreasing)
    all_increasing = all(1 <= diff <= 3 for diff in diffs)
    all_decreasing = all(-3 <= diff <= -1 for diff in diffs)

    return all_increasing or all_decreasing


def count_safe_reports(file_path):
    """
    Reads a file of reports and counts how many are safe.
    """
    safe_count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                report = list(map(int, line.split()))
                if is_safe(report):
                    safe_count += 1
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return -1
    except ValueError:
        print("Error: File contains invalid data. Ensure all lines contain integers separated by spaces.")
        return -1

    return safe_count


# Get the file path from the user and count safe reports
# Read input from a file
file_path = "./inputday2.txt"
safe_reports = count_safe_reports(file_path)

if safe_reports != -1:
    print("Number of safe reports:", safe_reports)
