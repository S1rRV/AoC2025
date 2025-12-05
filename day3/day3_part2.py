#!/usr/bin/env python3

def input_file(file):
    """Read a file one line at a time and process each line."""
    try:
        with open(file, 'r') as f:
            final_joltage = 0
            for line in f:
                #print(line)
                line = line.strip()
                result = ""
                remaining_str = line
                for i in range(12):
                    if len(remaining_str) < (12 - i):
                        break
                    if i == 11:  # Last digit
                        max_digit = max(remaining_str)
                    else:
                        max_digit = max(remaining_str[:-(12-i-1)])
                    pos = remaining_str.index(max_digit)
                    result += max_digit
                    remaining_str = remaining_str[pos+1:]

                joltage = int(result)

                #print(f"Joltage for this line: {joltage}")
                final_joltage += joltage
        return final_joltage
                    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Read the input file
    final_sum = input_file("../day3_input")
    #final_sum = input_file("../test")
    print(final_sum)
