import copy 
class Problem:
    def __init__(self, initial_state, goal_state, path_cost):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.path_cost = path_cost

    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False

    
    def actions(self, state):
        actions_list = []
        states_list = []
        size = len(state[0])
        for i in range(size):#2
            for j in range(size):#2
                if state[i][j] == 0:#i=0,j=0
                    if i > 0:
                        actions_list.append('UP')
                        states_list.append(self.result('UP', state, i, j))
                    if i + 1 < size:
                        actions_list.append('DOWN')
                        states_list.append(self.result('DOWN', state, i, j))
                    if j > 0:
                        actions_list.append('LEFT')
                        states_list.append(self.result('LEFT', state, i, j))
                    if j + 1 < size:
                        actions_list.append('RIGHT')
                        states_list.append(self.result('RIGHT', state, i, j))
                    break
        return {'states': states_list, 'actions': actions_list}


        
    def result(self, action, state , i , j):
        child_state = copy.deepcopy(state)
        if action == 'UP':
            child_state[i][j], child_state[i - 1][j] = child_state[i-1][j], child_state[i][j]
        elif action == 'DOWN':
            child_state[i][j], child_state[i + 1][j] = child_state[i+1][j], child_state[i][j]
        elif action == 'RIGHT':
            child_state[i][j], child_state[i][j + 1] = child_state[i][j+1], child_state[i][j]
        else:
            child_state[i][j], child_state[i][j - 1] = child_state[i][j-1], child_state[i][j]
        return child_state
