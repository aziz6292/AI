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

    
    def get_hr(self,state):
        i=0
        j=0
        size=len(state)
        hr_count = 0
        while i< size:
            while j<size:
                if not state[i][j]==self.goal_state[i][j]:
                    hr_count += 1
                j += 1
            i += 1
        return hr_count

    def actions(self, state):
        actions_list = []
        size = len(state[0])
        for i in range(size):#2
            for j in range(size):#2
                if state[i][j] == 0:#i=0,j=0
                    if i > 0:
                        actions_list.append('UP')
                    if i + 1 < size:
                        actions_list.append('DOWN')
                    if j > 0:
                        actions_list.append('LEFT')
                    if j + 1 < size:
                        actions_list.append('RIGHT')
                    return actions_list
        return None
    def result(self, action, state):
        size = len(state)
        child_state = copy.deepcopy(state)
        for i in range(size):
            for j in range(size):
                if state[i][j] == 0:
                    if action == 'UP':
                        child_state[i][j], child_state[i - 1][j] = child_state[i-1][j], child_state[i][j]
                    elif action == 'DOWN':
                        child_state[i][j], child_state[i + 1][j] = child_state[i+1][j], child_state[i][j]
                    elif action == 'RIGHT':
                        child_state[i][j], child_state[i][j + 1] = child_state[i][j+1], child_state[i][j]
                    else:
                        child_state[i][j], child_state[i][j - 1] = child_state[i][j-1], child_state[i][j]
                    return child_state
        return None
    # def actions(self, original_state):
    #     d = len(original_state[0])
    #     actions_list = []

    #     print("Current state:")
    #     for row in original_state:
    #         print(row)

    #     x, y = None, None
    #     for i in range(d):
    #         for j in range(d):
    #             if original_state[i][j] == 0:
    #                 x, y = i, j
    #     print(f"x={x}, y={y}")

    #     for dx, dy, action in [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]:
    #         if 0 <= y + dy < d and 0 <= x + dx < d:
    #             new_state = [row[:] for row in original_state]
    #             new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
    #             actions_list.append([new_state, action])

    #     print("Possible Child states are below")
    #     size = len(actions_list)
    #     for j in range (d):
    #         for i in range (size):
    #             print(actions_list[i][0][j], end= '\t\t')
    #         print()
    #     print("\n\n")
    #     return actions_list
