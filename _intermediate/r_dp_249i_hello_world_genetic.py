import random
import string
import time

mutation_rate = 0.1
valid_chars = string.punctuation + string.ascii_letters + " "
#valid_chars = valid_chars.replace("'","")
#valid_chars = string.ascii_letters + "!,"

def hamming_distance(input, target):
    """Return the Hamming distance between equal-length sequences"""
    if len(input) != len(target):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(input,target))


def generate_random_child(parent_string):
    word = ""
    for ch in parent_string:
        word += random.choice(valid_chars)
    return word

def get_child(parent1, parent2):
    child = ""
    length = len(goal)

    for i in range(length):
        if random.random() < mutation_rate:
            child += random.choice(valid_chars)
        else:
            child += parent1[i] if random.randint(0,1) == 0 else parent2[i]

    return child

def breed_population(pop_size, goal):
    current_population = []

    gen_count = 0

    for i in range(pop_size):
        current_population.append(generate_random_child(goal))

    while True:
        gen_count += 1

        next_population = []
        best_fitness = 1000

        for i in range(pop_size):
            parent_tuple = random.sample(current_population, 2)

            family = {parent_tuple[0]: hamming_distance(parent_tuple[0], goal),
                      parent_tuple[1]: hamming_distance(parent_tuple[1], goal)}

            child = get_child(parent_tuple[0], parent_tuple[1])
            family[child] = hamming_distance(child, goal)

            best_fit = min(family, key=family.get)

            next_population.append(best_fit)

            fitness = hamming_distance(next_population[i], goal)

            if fitness < best_fitness:
                best_fitness = fitness
                print("New best member of generation {} id {}".format(gen_count,next_population[i]))

        if best_fitness == 0:
            break

        current_population = next_population

    return gen_count

if __name__ == "__main__":
    goal = "Hello, world!"
    start_time = time.time()
    gen_count = breed_population(20, goal)
    end_time = time.time()
    print("Bred the perfect specimen in {} generations and {} seconds!".format(gen_count, end_time - start_time))
