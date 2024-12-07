def part1(updates, ordering_rules):
    valid_updates = []
    total_sum = 0

    for update in updates:
        is_valid = True
        for x, y in ordering_rules:
            if x in update and y in update: 
                if update.index(x) > update.index(y): 
                    is_valid = False
                    break
        
        if is_valid and update != [""]:
            valid_updates.append(update)
            middle_index = len(update) // 2
            total_sum += int(update[middle_index])


    print(f"Valid Updates: {valid_updates}")
    print(f"Sum of middle elements: {total_sum}")

    return total_sum

def part2(updates):
    valid_updates = []
    total_sum = 0

    for update in updates:
        is_valid = True
        for x, y in ordering_rules:
            if x in update and y in update: 
                if update.index(x) > update.index(y): 
                    is_valid = False
                    break
        
        if is_valid and update != [""]:
            valid_updates.append(update)
            middle_index = len(update) // 2
            total_sum += int(update[middle_index])


    print(f"Valid Updates: {valid_updates}")
    print(f"Sum of middle elements: {total_sum}")



def main():

    ordering_rules = []
    with open("pattern.txt", "r") as f:
        for line in f:
            x, y = line.strip().split("|")
            ordering_rules.append((x, y))
    
    updates = []
    with open("data.txt", "r") as f:
        for line in f:
            updates.append(line.strip().split(","))

    print(f"part 1 sums: {part1(updates)}")
    print(f"part 2 sums: {part2(updates)}")

