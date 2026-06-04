# P4 Genetic Algorithm

import random

# Fitness function
def fitness(chromosome):
    x = int(chromosome, 2)
    return x * x

# Initial population
population = [''.join(random.choice('01') for _ in range(4))
              for _ in range(4)]

for generation in range(10):

    # Sort population by fitness
    population = sorted(population,
                        key=fitness,
                        reverse=True)

    print("Generation", generation, population)

    # Selection (best two)
    parent1 = population[0]
    parent2 = population[1]

    # One-point crossover
    point = 2
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    # Mutation
    child1 = list(child1)
    pos = random.randint(0, 3)
    child1[pos] = '1' if child1[pos] == '0' else '0'
    child1 = ''.join(child1)

    # New population
    population = [parent1, parent2, child1, child2]

# Best solution
best = max(population, key=fitness)
print("\nBest Chromosome =", best)
print("x =", int(best, 2))
print("Fitness =", fitness(best))