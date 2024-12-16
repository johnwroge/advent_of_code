import heapq
import os

def read_file(file):
    with open(os.getcwd() + f'/2024/Day_16/{file}', 'r') as file:
        content = file.read().splitlines()
    return [list(line) for line in content]

def print_grid(grid):
    for line in grid:   
        print(''.join(line))


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_forward_position(state):
    if state.direction == 0:  
        return (state.x + 1, state.y)
    if state.direction == 1: 
        return (state.x, state.y + 1)
    if state.direction == 2:  
        return (state.x - 1, state.y)
    if state.direction == 3:  
        return (state.x, state.y - 1)

def is_valid_move(maze, x, y):
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != "#"
class State:
    def __init__(self, x, y, direction, cost, end):
        self.x = x
        self.y = y
        self.direction = direction
        self.cost = cost
        self.estimated = cost + manhattan_distance((x,y), end)
        self.parent = None
    def __lt__(self, other):
        return self.estimated < other.estimated
    

def visualize_optimal_tiles(maze, optimal_tiles):
    viz_maze = [row[:] for row in maze]
    for y, x in optimal_tiles:
        if viz_maze[y][x] not in ['S', 'E']:
            viz_maze[y][x] = 'O'
    print_grid(viz_maze)

def find_path(maze, start, end, part_2):
    open_set = []
    heapq.heapify(open_set)
    best_costs = {}
    start_state = State(start[1], start[0], 0, 0, end)
    optimal_cost = float('inf')
    optimal_tiles = set()  
    
    heapq.heappush(open_set, start_state)
    
    while open_set:
        current = heapq.heappop(open_set)
        state_key = (current.x, current.y, current.direction)
        
        if state_key in best_costs and current.cost > best_costs[state_key]:
            continue
            
        best_costs[state_key] = current.cost
        
        if (current.x, current.y) == (end[1], end[0]):
            if current.cost <= optimal_cost:
                optimal_cost = current.cost
                temp = current
                while temp:
                    optimal_tiles.add((temp.y, temp.x))
                    temp = temp.parent
            if not part_2:
                return optimal_cost
            continue 
            
        next_x, next_y = get_forward_position(current)
        if is_valid_move(maze, next_x, next_y):
            new_state = State(
                next_x, 
                next_y,
                current.direction,
                current.cost + 1,
                end
            )
            new_state.parent = current
            heapq.heappush(open_set, new_state)
        
        for turn in [-1, 1]: 
            new_direction = (current.direction + turn) % 4
            new_state = State(
                current.x,
                current.y,
                new_direction,
                current.cost + 1000,
                end
            )
            new_state.parent = current
            heapq.heappush(open_set, new_state)

    if part_2:
        visualize_optimal_tiles(maze, optimal_tiles)
        return len(optimal_tiles)
    return float('inf')    

def Solution():
    grid  = read_file('data.txt')
    start = None
    end = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if start and end:
                break
            elif grid[i][j] == 'S':
                start = (i,j)
            elif grid[i][j] == 'E':
                end = (i,j)
    first = find_path(grid, start, end, False)
    print('Part One:', first)
    first = find_path(grid, start, end, True)
    print('Part Two:', first)

if __name__ == "__main__":
    print(Solution())