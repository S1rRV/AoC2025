#!/usr/bin/env python3

def all_elements_equal(arr):
    if not arr:  # Handle empty array case
        return True
    first_element = arr[0]
    for element in arr:
        if element != first_element:
            return False
    return True

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
                my_list = list(range(int(first), int(last)+1))
                for id in my_list:
                    id = str(id)
                    l = len(id)
                    while l > 0:
                        if len(id) % l == 0:
                            output = [id[i:i+l] for i in range(0, len(id), l)]
                            if len(output) >= 2 and all_elements_equal(output):
                                #print(id)
                                sum += int(id)
                                break
                        l-=1
        return sum
                    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Read the input file
    final_sum = input_file("../day2_input")
    print(final_sum)
