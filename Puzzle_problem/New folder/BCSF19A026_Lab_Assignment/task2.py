from Problem import Problem
from Node import Node
def getInvCount(arr):
    size = len(arr)
    i = 0
    count = 0
    while i < size:
        j = i + 1
        while j < size:
            if arr[i] > arr[j] and not arr[j] == 0:
                count = count + 1
            j += 1
        i += 1
    return count
def findXPosition(puzzle):
    size = len(puzzle)
    i = 0
    while i < size:
        j = 0
        while j < size:
            if puzzle[i][j] == 0:
                return size - i
            j += 1
        i += 1
def isSolvable(puzzle):
    arr = []
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            arr.append(puzzle[i][j])
    count = getInvCount(arr)
    positionX = findXPosition(puzzle)
    if size % 2 == 1:
        return count % 2 == 0
    else:
        if count % 2 == 0:
            return positionX % 2 == 1
        else:
            return positionX % 2 == 0
import sys   
puzzles = []     
def input_from_file(fileName):
    with open(fileName, 'r') as file:
        stdin_original = sys.stdin
        sys.stdin = file
        N = int(input())
        for _ in range(N):
            line = ([int(x) for x in input().split()])
            line_index = 0
            size = int((len(line))**0.5)
            puzzle = []
            for _ in range(size):
                row = []
                for _ in range(size):
                    row.append(line[line_index])
                    line_index += 1
                puzzle.append(row)
            puzzles.append(puzzle)
        sys.stdin = stdin_original
input_from_file('problem.txt')


def output_into_file(fileName, result):
    with open(fileName, 'a') as file:
        stdout_original = sys.stdout
        sys.stdout = file
        size = len(result)
        if size:
            for i in range(size - 1):
                print(result[i], end='->')
            print(result[size - 1])
        sys.stdout = stdout_original

def make_goal(size):
    goal = []
    num = 1
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(num)
            num += 1
        goal.append(row)
    goal[size-1][size-1] = 0
    return goal

def solution(node):
    path = []
    while node.parent:
        path.append(node.action)
        node = node.parent
    return path

def get_hr(state, goal_state):
    i=0
    j=0
    size=len(state)
    hr_count = 0
    while i< size:
        while j<size:
            if state[i][j] !=goal_state[i][j]:
                hr_count += 1
            j += 1
        i += 1
    return hr_count

import heapq as hq
def informed_Search(problem):
    hr = get_hr(problem.initial_state, problem.goal_state)
    current = Node(problem.initial_state,0, hr + 0 , None, None)
    frontier = []
    hq.heappush(frontier, current)
    exposed = set()
    # if both are same at the beginning no need to check
    if problem.goal_test(current.state):
        solution(current)
    while frontier:
        current = hq.heappop(frontier)
        exposed.add(str(current.state))
        # if both are same at the beginning no need to check
        if problem.goal_test(current.state):
            return solution(current)
        else:
            childs = problem.actions(current.state)
            states = childs['states']
            actions = childs['actions']
            for i in range (len(states)):
                hr = get_hr(states[i], problem.goal_state)
                fn = current.cost + hr
                node = Node(states[i], current.cost+1, fn , current ,actions[i])
                if not str(node.state) in exposed and not node in frontier:
                   hq.heappush(frontier, node)


for puzzle in puzzles:
    print(puzzle)
    if isSolvable(puzzle):
        goal = make_goal(len(puzzle))
        problem = Problem(puzzle, goal, 0)
        path = list(informed_Search(problem))
        path.reverse()
        output_into_file('output.txt',path )
        for i,action in enumerate(path):
            if not i == len(path)-1:
                print(action, end = "->")
            else:
                print(action)

    else:
        print (" is not solvable")
    input("press any key to continue .......")
        