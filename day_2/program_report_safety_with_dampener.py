MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 3


def check_levels(levels, increasing):
    for i in range(1, len(levels)):
        diff = levels[i - 1] - levels[i]
        if increasing and (diff <= 0 or not (MIN_DIFFERENCE <= diff <= MAX_DIFFERENCE)):
            return False
        elif not increasing and (diff >= 0 or not (MIN_DIFFERENCE <= abs(diff) <= MAX_DIFFERENCE)):
            return False
    return True


def check_safety(levels): return check_levels(levels, True) or check_levels(levels, False)


def check_safety_with_dampener(levels):
    if check_safety(levels): return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if check_safety(modified_levels):
            return True

    return False



file = open("input.txt", 'r')
lines = file.readlines()

report_state_map = {}
for index, line in enumerate(lines):
    levels = list(map(int, line.split(" ")))

    print(f"Report {index}: {levels}")
    report_state_map[index] = check_safety_with_dampener(levels)
    print("\n")

print(f"Report State Map: {report_state_map}")

safe_reports = sum(report_state_map.values())

print(f"Safe reports: {safe_reports}")
