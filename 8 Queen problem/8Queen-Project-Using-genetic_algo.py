import random

population = []
explored = set()
# Generate initial population
def initial_random_population_generator():
    for _ in range(8):
        state = [random.randint(0,7) for _ in range(8)]
        population.append(state)
initial_random_population_generator()


def fitness_function(state):
    clashes = 0
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                clashes += 1
    return 28 - clashes


def crossover(x, y):
    c = random.randint(0,7)
    child = x[:c] + y[c:]
    return child
def random_parent_selector(population):
    fitness_score = []
    percentage_each = []
    for state in population:
        fitness_score.append(fitness_function(state))
    total = sum(fitness_score)
    for i in range (8):
        percentage_each.append((fitness_score[i]/total) * 100)
    val = random.randint(0, 100)
    #for index calculation
    index = -1
    cur_sum = 0
    for i in range(8):
        cur_sum += percentage_each[i]
        if val <= cur_sum:
            index = i
            break
    return population[index]


def mutation(state):
    index = random.randint(0,7)
    val = random.randint(0, 7)
    state[index] = val
    return state

def genetic_algorithm(population):
    max_clash = 0
    best_child = None
    count = 0
    while count < 1000:
        new_population = []
        for _ in range(8):
            x = random_parent_selector(population)
            y = random_parent_selector(population)
            child= crossover(x,y)
            if random.random() < 0.01:
                child = mutation(child)
            new_population.append(child)
        
        population = new_population
        for state in population:
            clash = fitness_function(state)
            if clash > max_clash:
                max_clash = clash
                best_child = state
        
        
        
        
        explored.add(str(best_child))
        if max_clash == 28:
            return best_child
        count += 1
    return best_child

 

# Run the genetic algorithm
solution = genetic_algorithm(population)
print("No of State explored: ", len(explored))
print("Clashes: ", 28 - fitness_function(solution))
# Print the board configuration
print("Solution found:")
for row in solution:
    board_row = ['Q' if i == row else '.' for i in range(8)]
    print(' '.join(board_row))
 