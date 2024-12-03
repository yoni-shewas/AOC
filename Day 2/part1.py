

def part1():
    count = 0

    try:
        with open('reactorData.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:  
                    try:
                        reading = list(map(int, line.split()))
                        
                        isSafe = True
                        increasing = all(0 < reading[i+1] - reading[i] <= 3 for i in range(len(reading) - 1))
                        decreasing = all(0 < reading[i] - reading[i+1] <= 3 for i in range(len(reading) - 1))
                        
                        if not (increasing or decreasing):
                            isSafe = False
                        
                        if isSafe:
                            count += 1
                        else:
                            print(f"Unsafe: {reading}")

                    except ValueError:
                        print(f"Skipping line due to formatting error: {line}")
            return count
    except FileNotFoundError:
        print("Error: The file 'data.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    print(count)


def is_safe(report):
    """Checks if the report is safe without removing any levels."""
    increasing = sum([1 if 0 < report[i+1] - report[i] <= 3 else 0 for i in range(len(report) - 1)])
    decreasing = sum([1 if 0 < report[i] - report[i+1] <= 3 else 0 for i in range(len(report) - 1)])
    
    n = len(report)
    return increasing >= n - 1 or decreasing >= n - 1

def part2():
    count = 0

    try:
        with open('reactorData.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:  
                    try:
                        reading = list(map(int, line.split()))
                        
                        # Check if the report is safe initially
                        if is_safe(reading):
                            count += 1
                            print(f"safe: {len(reading)} {reading}")
                        else:
                            # Try removing each element and check if the report becomes safe
                            is_safe_after_removal = False
                            for i in range(len(reading)):
                                modified_report = reading[:i] + reading[i+1:]
                                if is_safe(modified_report):
                                    is_safe_after_removal = True
                                    break
                            
                            if is_safe_after_removal:
                                count += 1
                                print(f"safe by removal: {len(reading)} {reading}")
                            else:
                                print(f"unsafe: {len(reading)} {reading}")

                    except ValueError:
                        print(f"Skipping line due to formatting error: {line}")
            return count
    except FileNotFoundError:
        print("Error: The file 'data.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    print(count)

def main():
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")

if __name__ == "__main__":
    main()