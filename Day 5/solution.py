from collections import defaultdict, deque

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

def part2(updates, ordering_rules):

    incorrect_updates = []
    sum_middle_pages = 0

    for update in updates:
        is_valid = True
        for x, y in ordering_rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):  
                    is_valid = False
                    break
        
        if not is_valid:
            pages_in_update = set(update)
            graph, in_degree = build_graph(pages_in_update, ordering_rules)
            fixed_update = topological_sort(graph, in_degree)
            
            incorrect_updates.append(fixed_update)
            middle_index = len(fixed_update) // 2
            sum_middle_pages += int(fixed_update[middle_index])

    
    print(f"Incorrect Updates (Fixed): {incorrect_updates}")
    print(f"Sum of middle pages: {sum_middle_pages}")

    return sum_middle_pages


def build_graph(pages, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Add edges based on rules
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x, 0)  # Ensure all nodes are in in_degree
    
    return graph, in_degree

# Perform topological sort to fix order
def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order



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

    print(f"part 1 sums: {part1(updates, ordering_rules)}")
    print(f"part 2 sums: {part2(updates, ordering_rules)}")


if __name__ == "__main__":
    main()

