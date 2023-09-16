def percept(percept_str, grid, goal):
    percept_list = percept_str.split()
    x, y = int(percept_list[1]), int(percept_list[2])
    if percept_list[0] == 'p':
        grid[x-1][y-1]['is_pit'] = True
    elif percept_list[0] == 'w':
        grid[x-1][y-1]['is_wumpus'] = True
    elif percept_list[0] == 'g':
        grid[x-1][y-1]['has_gold'] = True
        goal = (x-1, y-1)

def move(direction, current_position):
    if direction == 'up':
        return (current_position[0] - 1, current_position[1])
    elif direction == 'down':
        return (current_position[0] + 1, current_position[1])
    elif direction == 'left':
        return (current_position[0], current_position[1] - 1)
    elif direction == 'right':
        return (current_position[0], current_position[1] + 1)

def get_valid_moves(current_position, size):
    valid_moves = []
    x, y = current_position
    if x > 0:
        valid_moves.append('up')
    if x < size - 1:
        valid_moves.append('down')
    if y > 0:
        valid_moves.append('left')
    if y < size - 1:
        valid_moves.append('right')
    return valid_moves

def update_safe_cells(grid, current_position, safe_cells, size):
    safe_cells.add(current_position)
    adjacent_cells = get_adjacent_cells(current_position, size)
    for cell in adjacent_cells:
        if not grid[cell[0]][cell[1]]['is_pit'] and not grid[cell[0]][cell[1]]['is_wumpus']:
            safe_cells.add(cell)

def get_adjacent_cells(position, size):
    x, y = position
    adjacent_cells = []
    if x > 0:
        adjacent_cells.append((x - 1, y))
    if x < size - 1:
        adjacent_cells.append((x + 1, y))
    if y > 0:
        adjacent_cells.append((x, y - 1))
    if y < size - 1:
        adjacent_cells.append((x, y + 1))
    return adjacent_cells
import heapq as hq
def a_star_search(start, goal, grid):
    frontier = []
    hq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = hq.heappop(frontier)

        if current == goal:
            break

        for next_cell in get_adjacent_cells(current, len(grid)):
            new_cost = cost_so_far[current] + 1

            if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                cost_so_far[next_cell] = new_cost
                priority = new_cost + heuristic(goal, next_cell)
                hq.heappush(frontier, (priority, next_cell))
                came_from[next_cell] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def heuristic(goal, cell):
    return abs(goal[0] - cell[0]) + abs(goal[1] - cell[1])

def explore_unvisited_cells(actions, size, visited, safe_cells, current_position, grid):
    unvisited_cells = set([(i, j) for i in range(size) for j in range(size)]) - visited
    if unvisited_cells:
        start = current_position
        goal = unvisited_cells.pop()
        path = a_star_search(start, goal, grid)
        for cell in path:
            actions.append(f"({cell[0] + 1},{cell[1] + 1})")
            current_position = move_to(cell, current_position)
            visited.add(cell)

def move_to(cell, current_position):
    if cell[0] < current_position[0]:
        return move('up', current_position)
    elif cell[0] > current_position[0]:
        return move('down', current_position)
    elif cell[1] < current_position[1]:
        return move('left', current_position)
    elif cell[1] > current_position[1]:
        return move('right', current_position)

def make_safe_move(actions, size, visited, safe_cells, current_position, grid):
    unvisited_safe_cells = safe_cells - visited
    if unvisited_safe_cells:
        start = current_position
        goal = unvisited_safe_cells.pop()
        path = a_star_search(start, goal, grid)
        for cell in path:
            actions.append(f"({cell[0] + 1},{cell[1] + 1})")
            current_position = move_to(cell, current_position)
            visited.add(cell)

def shoot_arrow(direction, arrows):
    if arrows > 0:
        actions.append(f"SHOOT {direction}")
        return arrows - 1
    return arrows

def grab_gold(grid, current_position, has_gold):
    if grid[current_position[0]][current_position[1]]['has_gold']:
        actions.append("GRAB")
        has_gold = True
    return has_gold

def play(environment_file):
    grid = []
    visited = set()
    safe_cells = set()
    actions = []
    current_position = (0, 0)
    has_gold = False
    arrows = 0
    print (f"({current_position[0] + 1}, {current_position[1] + 1})", end = " -> ")
    with open(environment_file, 'r') as file:
        size = int(file.readline().strip())
        arrows = int(file.readline().strip())
        grid = [[{'is_pit': False, 'is_wumpus': False, 'has_gold': False} for _ in range(size)] for _ in range(size)]
        goal = (-1,-1)
        for line in file:
            percept_str = line.strip()
            percept(percept_str, grid, goal)
    while not has_gold:
        update_safe_cells(grid, current_position, safe_cells, size)
        explore_unvisited_cells(actions, size, visited, safe_cells, current_position, grid)
        make_safe_move(actions, size, visited, safe_cells, current_position, grid)
        has_gold = grab_gold(grid, current_position, has_gold)
        if has_gold:
            print("Found")
            return actions

    
            

# Usage example
actions = play("env1.txt")

for action in actions:
    print(action, end = " -> ")
print("Found")
