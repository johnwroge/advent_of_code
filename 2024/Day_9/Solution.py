
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
    
    pass

def find_files(layout):
    """Find continuous blocks of each file ID"""
    files = {} 
    
    i = 0
    while i < len(layout):
        if layout[i] != '.':
            start = i
            file_id = layout[i]
            length = 0
            
            while i < len(layout) and layout[i] == file_id:
                length += 1
                i += 1
                
            if file_id not in files:
                files[file_id] = []
            files[file_id].append((start, length))
        else:
            i += 1
            
    return files

def find_free_space(layout, start, needed_length):
    """Find leftmost free space of sufficient length"""
    i = 0
    while i < start:
        if layout[i] == '.':
            space_start = i
            length = 0
            while i < start and layout[i] == '.':
                length += 1
                i += 1
            if length >= needed_length:
                return space_start
        else:
            i += 1
    return -1

def compact_files_part2(layout):
    layout = layout.copy()
    files = find_files(layout)
    
    for file_id in sorted(files.keys(), key=int, reverse=True):
        for start, length in files[file_id]:
            new_pos = find_free_space(layout, start, length)
            if new_pos != -1:
                for i in range(length):
                    layout[new_pos + i] = file_id
                    layout[start + i] = '.'
    
    return layout

def Part_Two():
    content = read_file('data.txt')
    initial_layout = create_initial_layout(content)
    compacted = compact_files_part2(initial_layout)
    return calculate_checksum(compacted)

if __name__ == "__main__":
    print('Part 1:', Part_One())
    print('Part 2:', Part_Two())

