import os 

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

def count_sides(region, grid_width, grid_height):
    """Count the number of distinct sides for a region."""
    sides = set()
    
    def is_in_region(r, c):
        return (r, c) in region
    
    # For each cell in the region
    for row, col in region:
        # Check left edge
        if not is_in_region(row, col - 1):
            left_edge = True
            # Look for cells above and below that might continue this edge
            r = row - 1
            while r >= 0 and is_in_region(r, col) and not is_in_region(r, col - 1):
                r -= 1
            top = r + 1
            
            r = row + 1
            while r < grid_height and is_in_region(r, col) and not is_in_region(r, col - 1):
                r += 1
            bottom = r
            
            sides.add(('V', col, top, bottom))
        
        # Check right edge
        if not is_in_region(row, col + 1):
            # Look for cells above and below that might continue this edge
            r = row - 1
            while r >= 0 and is_in_region(r, col) and not is_in_region(r, col + 1):
                r -= 1
            top = r + 1
            
            r = row + 1
            while r < grid_height and is_in_region(r, col) and not is_in_region(r, col + 1):
                r += 1
            bottom = r
            
            sides.add(('V', col + 1, top, bottom))
        
        # Check top edge
        if not is_in_region(row - 1, col):
            # Look for cells left and right that might continue this edge
            c = col - 1
            while c >= 0 and is_in_region(row, c) and not is_in_region(row - 1, c):
                c -= 1
            left = c + 1
            
            c = col + 1
            while c < grid_width and is_in_region(row, c) and not is_in_region(row - 1, c):
                c += 1
            right = c
            
            sides.add(('H', row, left, right))
        
        # Check bottom edge
        if not is_in_region(row + 1, col):
            # Look for cells left and right that might continue this edge
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
    # Parse input into grid
    grid = [list(line) for line in input_text.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    
    # Find all regions
    regions = find_regions(grid)
    
    total_price = 0
    # Calculate price for each region
    for plant_type, region_coords in sorted(regions):
        area = len(region_coords)
        sides = count_sides(region_coords, width, height)
        price = area * sides
        total_price += price
        
    return total_price

# Test cases with their expected results
def run_test(test_input, expected, case_num):
    result = solve_garden_groups_part2(test_input)
    assert result == expected, f"Test case {case_num} failed: got {result}, expected {expected}"
    print(f"Test case {case_num} passed: {result}")
    return result

# Simple test case
test1 = """AAAA
BBCD
BBCC
EEEC"""
result1 = run_test(test1, 80, 1)

# O's and X's test case
test2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
result2 = run_test(test2, 436, 2)

# E-shaped region test case
test3 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
result3 = run_test(test3, 236, 3)

# Diagonal touching regions test case
test4 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
result4 = run_test(test4, 368, 4)

# Complex test case
test5 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
result5 = run_test(test5, 1206, 5)

print("All test cases passed!")

text = read_file("data.txt")
print(solve_garden_groups_part2(text))

