from pyeasyga.pyeasyga import GeneticAlgorithm
import random
import numpy as np
import deap.tools.crossover
import scoring
import parse_input
import rand

temp_max = 0

data = parse_input.load()
ga = GeneticAlgorithm(data, 100, 20, 0.1, 0.8, True, True)


def create_individual(data):
    a = np.arange(80000)
    np.random.shuffle(a)
    return a

ga.create_individual = create_individual



def crossover(parent_1, parent_2):
    ch1, ch2 = deap.tools.crossover.cxPartialyMatched(parent_1, parent_2)
    return ch1, ch2

ga.crossover_function = crossover


def mutate(individual):
    a = np.random.randint(0, individual.size)
    b = np.random.randint(0, individual.size)

    tp = individual[a]
    individual[a] = individual[b]
    individual[b] = tp
    return individual

ga.mutate_function = mutate

def selection(population):
    return random.choice(population)


ga.selection_function = selection


def fitness(individual, data):
    global temp_max
    a = scoring.evaluate(individual.reshape(-1,1), data)
    if a > temp_max:
        print("Nasiel som:", a)
        print(individual)
        rand.write("naj.txt", individual)
        temp_max = a
    return a

ga.fitness_function = fitness
ga.run()

print(ga.best_individual())





