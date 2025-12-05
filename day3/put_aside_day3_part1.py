#!/usr/bin/env python3

def input_file(file):
    """Read a file one line at a time and process each line."""
    try:
        with open(file, 'r') as f:
            final_joltage = 0
            for line in f:
                line = line.strip() 
                lenth = len(line)
                joltage = 0
                l_index = 0
                r_index = lenth - 1

                while l_index < r_index:   
                    print(int(line[l_index])*10 + int(line[r_index]))
                    if int(line[l_index])*10 + int(line[r_index]) > joltage:
                        joltage = int(line[l_index])*10 + int(line[r_index])

                    move_left = (l_index + 1 < r_index) and (int(line[l_index + 1]) > (l_index))
                    move_right = (r_index - 1 < l_index) and (int(line[r_index - 1]) > (r_index))

                    if move_left and move_right:
                        l_index += 1
                    elif move_right:
                        r_index -= 1
                    elif move_left:
                        l_index += 1
                    else:
                        break




                print(f"Joltage for this line: {joltage}")
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
