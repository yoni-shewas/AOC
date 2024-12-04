import re

def part1():
    with open('data.txt', 'r') as file:
        lines = file.readlines()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total_sum = 0

    for line in lines:
        matches = re.findall(pattern, line)

        if matches:
            for left, right in matches:
                total_sum += int(left) * int(right)

        else:
            print("No valid mul found in line:", line.strip())

    return total_sum

def part2():
    total = 0
    with open('data.txt', 'r') as file:
        enabled = True

        pattern = r"mul\((\d{1-3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

        for a, b, do, dont in re.findall(pattern, file.read()):
            if do or dont:
         
                enabled = bool(do)  
            else:
                x = int(a) * int(b)
                if enabled:
                    total += x 

    return total

def main():
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")


if __name__ == "__main__":
    main()
