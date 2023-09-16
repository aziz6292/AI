from Node import Node
from Problem import Problem
import sys


# global variables
N = None  # no of puzzle
puzzle = []

# function for taking input from file into variables


def input_from_file(fileName):
    with open(fileName, 'r') as file:
        stdin_original = sys.stdin
        sys.stdin = file
        N = int(input())
        for _ in range(N):
            temp_list = ([int(x) for x in input().split()])
            d = (len(temp_list))**0.5
            d = int(d)
            s = 0
            init = []
            goal = []
            for _ in range(d):
                i1 = []
                g1 = []
                for j in range(d):
                    i1.append(temp_list[s])
                    s += 1
                    g1.append(s)
                goal.append(g1)
                init.append(i1)
            puzzle.append(init)
            goal[d-1][d-1] = 0
            puzzle.append(goal)
        sys.stdin = stdin_original


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


def solution(node):
    path = []
    while node.parent:
        path.append(node.action)
        node = node.parent
    return path


def child(problem, action, parent):#['','up/down/left/right', 'Node of parent']
    state = problem.result(action, parent.state)
    return Node(state, action, parent, parent.cost+1)


def bfs(problem):
    current = Node(problem.initial_state, None, None, 0)
    frontier = [current]
    exposed = set()
    # if both are same at the beginning no need to check
    if problem.goal_test(current.state):
        solution(current)
    while frontier:
        current = frontier.pop(0)
        exposed.add(str(current.state))
        # if both are same at the beginning no need to check
        if problem.goal_test(current.state):
            return solution(current)
        else:
            for action in problem.actions(current.state):#['left','right','up','down']
                node = child(problem, action, current)
                # if both are same at the beginning no need to check
                if problem.goal_test(node.state):
                    return solution(node)
                if not str(node.status) in exposed and not node in frontier:
                    frontier.append(node)
    return []


# main program
fileName = input("File Name (input.txt): ")
input_from_file(fileName)

# in puzzle list the initial state is at odd and goal state is at the recent even index
for i in range(0, len(puzzle), 2):
    problem = Problem(
        initial_state=puzzle[i], goal_state=puzzle[i+1], path_cost=0)
    result = list(bfs(problem))
    if result:
        result.reverse()
        print("path: ", result)
    else:
        print(f"path not found")
    input("press any key to check for next puzzle...")
    print()
    output_into_file("output.txt", result)
print("Successfully written into output.txt")
