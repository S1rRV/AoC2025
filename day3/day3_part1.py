#!/usr/bin/env python3

def input_file(file):
    """Read a file one line at a time and process each line."""
    try:
        with open(file, 'r') as f:
            final_joltage = 0
            for line in f:
                #print(line)
                line = line.strip()

                first_max = max(line[:-1])
                max_first_index = line.index(first_max)

                second_max = max(line[max_first_index+1:])

                joltage = int(first_max + second_max)

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
