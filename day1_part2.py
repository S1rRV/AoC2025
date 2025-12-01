#!/usr/bin/env python3

def input_file(file):
    """Read a file one line at a time and process each line."""
    print(" - The dial is starts by pointing at 50")
    try:
        with open(file, 'r') as f:
            position = 50
            count = 0
            for line in f:
                line = line.strip()   

                prev_position = position
                direction = 1 if line[0] == "R" else -1  
                value = int(line[1:])   
                count += value // 100

                remainder = value % 100
                position += (direction * remainder)
                

                
                while position >= 100:
                    position -= 100
                    if position != 0 and prev_position != 0:
                        count += 1
                    
                while position < 0:
                    position += 100
                    if position != 0 and prev_position != 0:
                        count += 1
                
                if position == 0:
                    count += 1

                
                print(f" - The dial is rotated {line} by pointing at {position}") 
        return count
    
        
                    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Read the input file
    final_count = input_file("./input")
    print(final_count)
