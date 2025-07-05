import os


    

def solve_rope_bridge(moves):
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    
    tail_visited = {(0, 0)} 
    
    directions = {
        'R': (1, 0),  
        'L': (-1, 0), 
        'U': (0, 1),   
        'D': (0, -1)  
    }
    
    for move in moves:
        direction, steps = move.split()
        steps = int(steps)
        dx, dy = directions[direction]
        
        for _ in range(steps):
            head_x += dx
            head_y += dy
            
            dist_x = head_x - tail_x
            dist_y = head_y - tail_y
            
            if abs(dist_x) > 1 or abs(dist_y) > 1:
                
                if dist_x > 0:
                    tail_x += 1
                elif dist_x < 0:
                    tail_x -= 1
                    
                if dist_y > 0:
                    tail_y += 1
                elif dist_y < 0:
                    tail_y -= 1
            
            tail_visited.add((tail_x, tail_y))
    
    return len(tail_visited)


example_moves = [
    "R 4",
    "U 4", 
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"
]

result = solve_rope_bridge(example_moves)
print(f"Example, {result}")

with open(os.getcwd() + '/2022/Day9/day9.txt', 'r') as f:
    puzzle_moves = f.read().strip().split('\n')
answer = solve_rope_bridge(puzzle_moves)
print(f"Part 1, answer: {answer}")
    

