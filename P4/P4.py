# ---------------------------------------------
# Genetic Algorithm using 2-bit Chromosomes
# Fitness Function: f(x) = x^2
# ---------------------------------------------

import random

# ---------------------------------------------
# Fitness Function
# ---------------------------------------------
def fitness(chromosome):
    x = int(chromosome, 2)      # Convert binary to decimal
    return x * x                # f(x) = x^2


# ---------------------------------------------
# Initial Population
# ---------------------------------------------
population = ["00", "01", "10", "11"]

print("INITIAL POPULATION")
print("------------------")

for c in population:
    print(c, " Decimal =", int(c,2), " Fitness =", fitness(c))


# ---------------------------------------------
# Selection (Best Two Chromosomes)
# ---------------------------------------------
population = sorted(population,
                    key=fitness,
                    reverse=True)

parent1 = population[0]
parent2 = population[1]

print("\nSELECTED PARENTS")
print("----------------")
print("Parent 1 =", parent1)
print("Parent 2 =", parent2)


# ---------------------------------------------
# Single Point Crossover
# ---------------------------------------------
cross_point = 1

child1 = parent1[:cross_point] + parent2[cross_point:]
child2 = parent2[:cross_point] + parent1[cross_point:]

print("\nAFTER CROSSOVER")
print("----------------")
print("Child 1 =", child1)
print("Child 2 =", child2)


# ---------------------------------------------
# Mutation
# Flip one random bit of Child 1
# ---------------------------------------------
bit = random.randint(0,1)

child1 = list(child1)

if child1[bit] == '0':
    child1[bit] = '1'
else:
    child1[bit] = '0'

child1 = "".join(child1)

print("\nAFTER MUTATION")
print("----------------")
print("Mutated Child 1 =", child1)
print("Child 2         =", child2)


# ---------------------------------------------
# New Population
# ---------------------------------------------
new_population = [child1, child2]

print("\nNEW POPULATION")
print("----------------")

for c in new_population:
    print(c, " Decimal =", int(c,2), " Fitness =", fitness(c))


# ---------------------------------------------
# Best Solution
# ---------------------------------------------
best = max(new_population, key=fitness)

print("\nBEST SOLUTION")
print("----------------")
print("Best Chromosome =", best)
print("Decimal Value   =", int(best,2))
print("Maximum Fitness =", fitness(best))
