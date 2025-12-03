#!/usr/bin/env python3

def input_file(file):
    """Read a file one line at a time and process each line."""
    try:
        with open(file, 'r') as f:
            sum = 0
            line = f.readline().split(',')
            for my_range in line:
                my_range = my_range.split("-")
                first = my_range[0]
                last = my_range[1]    
                if len(first) != len(last):        
                    if len(first) % 2 != 0:
                        first = str(10**(len(first))) 
                    elif len(last) % 2 != 0:
                        last = str(10**(len(last)-1)-1) 
                if len(first) == len(last) and int(len(first)) % 2 == 0:
                    my_list = list(range(int(first), int(last)+1))
                    for id in my_list:
                        id = str(id)
                        l = int(len(id)) // 2
                        if id[l:] == id[:l]:
                            sum += int(id)
        return sum
                    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Read the input file
    final_sum = input_file("../day2_input")
    print(final_sum)
