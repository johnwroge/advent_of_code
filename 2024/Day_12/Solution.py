import os


"""
AAAA
BBCD
BBCC
EEEC

A,B,C,D - individual garden plots

A,B,C - region of area 4
C - 3
D - 1

region - 5 types of plants connected horizontally and vertically

cost of fence = area (number of garden plots of region) * perimeter 

"""


def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_12/{filename}', 'r') as file:
        contents = file.read()
    return contents

def find_regions(grid):
    """Find all regions in the grid using flood fill."""
    height = len(grid)
    width = len(grid[0])
    visited = set()
    regions = []
    
    def flood_fill(row, col, plant_type):
        if (row < 0 or row >= height or col < 0 or col >= width or 
            (row, col) in visited or grid[row][col] != plant_type):
            return set()
        
        region = {(row, col)}
        visited.add((row, col))
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            region.update(flood_fill(new_row, new_col, plant_type))
            
        return region

    for row in range(height):
        for col in range(width):
            if (row, col) not in visited:
                plant_type = grid[row][col]
                region = flood_fill(row, col, plant_type)
                if region:
                    regions.append((plant_type, region))
    
    return regions

def calculate_perimeter(region_coords, grid_width, grid_height):
    """Calculate the perimeter of a region."""
    perimeter = 0
    
    for row, col in region_coords:
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc

            if (
                new_row < 0 or new_row >= grid_height or
                new_col < 0 or new_col >= grid_width or
                (new_row, new_col) not in region_coords
            ):
                perimeter += 1
                
    return perimeter

def solve_garden_groups(input_text):
    grid = [list(line) for line in input_text.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    
    regions = find_regions(grid)
    
    total_price = 0
    for plant_type, region_coords in regions:
        area = len(region_coords)
        perimeter = calculate_perimeter(region_coords, width, height)
        price = area * perimeter
        total_price += price
        
    return total_price


def count_sides(region, grid_width, grid_height):
    """Count the number of distinct sides for a region."""
    sides = set()
    
    def is_in_region(r, c):
        return (r, c) in region
    
    for row, col in region:
        if not is_in_region(row, col - 1):
            left_edge = True
            r = row - 1
            while r >= 0 and is_in_region(r, col) and not is_in_region(r, col - 1):
                r -= 1
            top = r + 1
            
            r = row + 1
            while r < grid_height and is_in_region(r, col) and not is_in_region(r, col - 1):
                r += 1
            bottom = r
            
            sides.add(('V', col, top, bottom))
        
        if not is_in_region(row, col + 1):
            r = row - 1
            while r >= 0 and is_in_region(r, col) and not is_in_region(r, col + 1):
                r -= 1
            top = r + 1
            
            r = row + 1
            while r < grid_height and is_in_region(r, col) and not is_in_region(r, col + 1):
                r += 1
            bottom = r
            
            sides.add(('V', col + 1, top, bottom))
        
        if not is_in_region(row - 1, col):
            c = col - 1
            while c >= 0 and is_in_region(row, c) and not is_in_region(row - 1, c):
                c -= 1
            left = c + 1
            
            c = col + 1
            while c < grid_width and is_in_region(row, c) and not is_in_region(row - 1, c):
                c += 1
            right = c
            
            sides.add(('H', row, left, right))
        
        if not is_in_region(row + 1, col):
            c = col - 1
            while c >= 0 and is_in_region(row, c) and not is_in_region(row + 1, c):
                c -= 1
            left = c + 1
            
            c = col + 1
            while c < grid_width and is_in_region(row, c) and not is_in_region(row + 1, c):
                c += 1
            right = c
            
            sides.add(('H', row + 1, left, right))
    
    return len(sides)

def solve_garden_groups_part2(input_text):
    """Solve part 2 of the garden groups puzzle."""
    grid = [list(line) for line in input_text.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    
    regions = find_regions(grid)
    
    total_price = 0
    for plant_type, region_coords in sorted(regions):
        area = len(region_coords)
        sides = count_sides(region_coords, width, height)
        price = area * sides
        total_price += price
        
    return total_price


def Part_One():
    contents = read_file('data.txt')
    return solve_garden_groups(contents)

def Part_Two():
    contents = read_file('data.txt')
    return solve_garden_groups_part2(contents)

if __name__ == '__main__':
    print(Part_One())
    print(Part_Two())
