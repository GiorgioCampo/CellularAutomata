import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

from rules import Rule
from utilities import *
from simulate_automata import *

def run_experiment(neighborhood_size, rules=None):
    combinations = Rule(0, neighborhood_size=neighborhood_size).rule_map.keys()
    combinations_count = {c: list() for c in combinations}
    rules_combs = []

    n_rules = 2**(2**neighborhood_size)

    if rules is None:
        rules = range(n_rules)
    print("Generating rules")
    all_rules = [Rule(i, neighborhood_size=neighborhood_size) for i in tqdm(rules)]

    print("Reconstructing past states")
    for rule in tqdm(all_rules):
        counter = rule.reconstruct_past()
        rules_combs.append(counter)

        for c, v in counter.items():
            combinations_count[c].append(v)

    # calculate expected value of life
    print("Calculating expected value of life")
    life_expected_value = np.zeros(len(rules))
    for c, v in tqdm(combinations_count.items()):
        life_vect = np.array([rule.apply(c) for rule in all_rules])
        life_expected_value += np.array(v) * life_vect

    life_expected_value /= len(combinations_count.keys())

    # Calculate reproduction rate
    print("Calculating reproduction rate")
    reproduction_rate = np.zeros(len(rules))
    for c, v in tqdm(combinations_count.items()):
        if c.count(1) == 0:
            continue
        repr_vect = np.array([rule.apply(c) / c.count(1) for rule in all_rules])
        reproduction_rate += np.array(v) * repr_vect

    reproduction_rate /= len(combinations_count.keys())

    print("Calculating reproduction/life index")
    index = reproduction_rate / life_expected_value

    return life_expected_value, reproduction_rate, index


def experiments():
    life_value_3, repr_rate_3, index_3 = run_experiment(neighborhood_size=3)
    n_rules = 2**(2**3)
    # plot_stats(n_rules, life_value_3, "Expected Value Of Life")
    # plot_stats(n_rules, repr_rate_3, "Reproduction Rate")
    # plot_stats(n_rules, index_3, "Reproduction/Life Index")
    # plot_scatter(n_rules, life_value_3, repr_rate_3)

    lv_110 = life_value_3[109]
    rr_110 = repr_rate_3[109]
    index_110 = index_3[109]
    # Plot histograms for all combinations
    # plot_rules_distributions(combinations_count)

    # Plot stacked bar chart for rules_combs
    # plot_rules_combs(rules_combs)

    # life_value_4, repr_rate_4, index_4 = run_experiment(neighborhood_size=4)
    # n_rules = 2**(2**4)

    # indices = np.where(np.logical_and(np.isclose(life_value_4, lv_110), 
    #         np.logical_and(np.isclose(repr_rate_4, rr_110), np.isclose(index_4, index_110))))[0]
    # print(indices)
    # print(len(indices))

    # plot_stats(n_rules, life_value_4, "Expected Value Of Life")
    # plot_stats(n_rules, repr_rate_4, "Reproduction Rate")
    # plot_stats(n_rules, index_4, "Reproduction/Life Index")
    # plot_scatter(n_rules, life_value_4, repr_rate_4)

    n_rules = 2**(2**5)
    
    print("Generating random rules")
    rand_rules = []

    for _ in tqdm(range(1_000_000)):
        rand = ""
        for _ in range(32):
            rand += str(np.random.randint(0, 2))
        rand_rules.append(int(rand, 2))

    print(rand_rules[:20])

    life_value_5, repr_rate_5, index_5 = run_experiment(neighborhood_size=5, rules=rand_rules)

    indices = np.where(np.logical_and(np.isclose(life_value_5, lv_110), 
            np.logical_and(np.isclose(repr_rate_5, rr_110), np.isclose(index_5, index_110))))[0]
    print(indices)
    print(len(indices))

def main():
    # experiments()

    grid = simulate_automaton(rule_number=110, length=200, steps=200)
    plot_automaton(grid)

if __name__ == "__main__":
    main()
