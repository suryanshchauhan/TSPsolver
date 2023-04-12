import random
import sys

# Function to read the TSP file
def read_tsp_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        cities = [file.readline().strip() for _ in range(n)]
        costs = [[int(x) for x in file.readline().split()] for _ in range(n)]
    return n, cities, costs

# Function to generate a random path
def random_path(n):
    path = list(range(n))
    random.shuffle(path)
    return path

# Function to calculate the cost of a path
def path_cost(path, costs):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += costs[path[i]][path[i + 1]]
    total_cost += costs[path[-1]][path[0]]
    return total_cost

# Function to perform selection
def selection(population, costs):
    population = sorted(population, key=lambda x: path_cost(x, costs))
    return population[:len(population)//2]

# Function to perform crossover
def crossover(parent1, parent2):
    n = len(parent1)
    start, end = random.sample(range(n), 2)
    start, end = min(start, end), max(start, end)
    child = [None] * n
    child[start:end] = parent1[start:end]

    for city in parent2:
        if city not in child:
            i = child.index(None)
            child[i] = city
    return child

# Function to perform mutation
def mutation(path):
    i, j = random.sample(range(len(path)), 2)
    path[i], path[j] = path[j], path[i]
    return path

# Genetic algorithm function
def genetic_algorithm(filename, generations, population_size):
    n, cities, costs = read_tsp_file(filename)
    population = [random_path(n) for _ in range(population_size)]

    for generation in range(generations):
        population = selection(population, costs)
        new_population = []
        for i in range(population_size // 2):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            new_population.append(mutation(child))
        population += new_population
        best_path = min(population, key=lambda x: path_cost(x, costs))
        print(f"Generation {generation}: Best cost = {path_cost(best_path, costs)}")

    best_path = min(population, key=lambda x: path_cost(x, costs))
    return best_path, path_cost(best_path, costs)

# Main function
def main():
    filename = input("Enter the file name: ")
    generations = 1000
    population_size = 100

    try:
        best_path, best_cost = genetic_algorithm(filename, generations, population_size)
        print("Best path found:", " -> ".join(map(str, best_path)))
        print("Best path cost:", best_cost)
    except FileNotFoundError:
        print("Error: File not found.")

# Run the main function
if __name__ == "__main__":
    main()
