def get_initial():
    initial = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
    return initial
def display(initial):
    for row in initial:
        print(row)

def terminate(state):
    draw = True
    dig1 = True
    dig2 = True
    dig3 = True
    dig4 = True
    for i in range (3):
        row_user = True
        col_user = True
        row_opp = True
        col_opp = True
        for j in range (3):
            if state[i][j] == '-':
                draw = False
            if state[i][j] != 'X':
                row_user = False
            if state[j][i] != 'X':
                col_user = False
            if state[i][j] != 'O':
                row_opp = False
            if state[j][i] != 'O':
                col_opp = False
        if row_user or col_user:
            return -1
        if row_opp or col_opp:
            return 1
        if state[i][i] != 'X':
            dig1 = True
        if state[i][2 - i] != 'X':
            dig2 = True
        if state[i][i] != 'O':
            dig3 = True
        if state[i][2 - i] != 'O':
            dig4 = True
    if dig1 or dig2:
        return -1
    if dig3 or dig4:
        return 1
    if draw:
        return 0
    return 2
import copy
def get_actions(state):
    actions = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '-':
                actions.append([i,j])
    return actions
def result(state, action):
    child = copy.deepcopy(state)
    child[action[0]][action[1]] = 'X'
    return min_value(child) 
def min_max_decision(state):
    best_action = None 
    best_score = int('inf')
    actions = get_actions(state)
    for action in actions:
        score = result(state, action)
        if score < best_score:
            best_score = score
            best_action = action
    return best_action
def main():
    # node = Node(initial, None, 0, None)
    state = get_initial
    frontiar = [state]
    while True:
        if terminate(state) == 2:
            action = min_max_decision(state)
            new_state = copy.deepcopy(state)
            new_state[action[0]][action[1]] = 'X'
            frontiar.append(new_state)
        else:
            return frontiar
        display(new_state)
        x= input("row: ")
        y = input("col: ")
        temp = copy.deepcopy(new_state)
        temp[x][y] = 'O'
        frontiar.append(temp)
        state = temp

states = main()
for state in states:
    display(state)


    
    


        
