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
            temp_list = ([int(x) for x in input().split()])
            s = 0
            d = int((len(temp_list))**0.5)
            init = []
            for _ in range(d):
                i1 = []
                for _ in range(d):
                    i1.append(temp_list[s])
                    s += 1
                init.append(i1)
            puzzles.append(init)
        sys.stdin = stdin_original
input_from_file('problem.txt')

for puzzle in puzzles:
    print(puzzle)
    if isSolvable(puzzle):
        print (" is solvable")
    else:
        print (" is not solvable")
        