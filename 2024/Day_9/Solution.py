
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_9/{filename}', 'r') as file:
        contents = file.read()
    return contents

def create_initial_layout(numbers):
    """Convert the dense format into blocks with file IDs"""
    layout = []
    file_id = 0
    
    i = 0
    while i < len(numbers):
        file_length = int(numbers[i])
        layout.extend([str(file_id)] * file_length)
        file_id += 1
        i += 1
        if i < len(numbers):
            space_length = int(numbers[i])
            layout.extend(['.'] * space_length)
            i += 1
    
    return layout

def compact_files(layout):
    """Move files from right to left into empty spaces"""
    layout = layout.copy()
    
    while '.' in layout:
        empty_pos = layout.index('.')
        
        file_found = False
        for i in range(len(layout) - 1, empty_pos, -1):
            if layout[i] != '.':
                layout[empty_pos] = layout[i]
                layout[i] = '.'
                file_found = True
                break
        
        if not file_found:
            break
    
    return layout

def calculate_checksum(layout):
    """Calculate checksum by multiplying position by file ID"""
    total = 0
    for pos, val in enumerate(layout):
        if val != '.':
            total += pos * int(val)  
    return total

def Part_One():
    content = read_file('data.txt')
    initial_layout = create_initial_layout(content)
    compacted = compact_files(initial_layout)
    answer = calculate_checksum(compacted)
    return answer

if __name__ == "__main__":
    print(Part_One())

    