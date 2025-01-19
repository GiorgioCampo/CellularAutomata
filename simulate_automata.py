import numpy as np
import matplotlib.pyplot as plt

from rules import Rule

__all__ = ["simulate_automaton", "plot_automaton"]

# Simulation function
def simulate_automaton(rule_number, length, steps, initial_state=None):
    """
    Simulate a 1D cellular automaton.

    Args:
        rule_number (int): Rule number for the automaton.
        length (int): Length of the grid.
        steps (int): Number of steps to simulate.
        initial_state (list[int], optional): Initial state of the grid. 
                                             If None, a random state is generated.

    Returns:
        np.ndarray: 2D array representing the automaton evolution.
    """
    # Initialize the rule
    rule = Rule(rule_number)
    
    # Generate a random initial state if none is provided
    if initial_state is None:
        initial_state = np.random.choice([0, 1], size=length)
    else:
        initial_state = np.array(initial_state)

    # Ensure the initial state matches the specified length
    if len(initial_state) != length:
        raise ValueError("Initial state length does not match specified length.")

    # Initialize the grid to store automaton evolution
    grid = np.zeros((steps, length), dtype=int)
    grid[0] = initial_state

    # Simulate the automaton evolution
    for t in range(1, steps):
        for i in range(length):
            # Determine the neighborhood with wrap-around boundary conditions
            neighborhood = [
                grid[t - 1][(i - 1) % length],
                grid[t - 1][i],
                grid[t - 1][(i + 1) % length]
            ]
            # Apply the rule to determine the next state
            grid[t][i] = rule.apply(neighborhood)

    return grid

# Plotting function
def plot_automaton(grid):
    """
    Plot the evolution of the automaton.

    Args:
        grid (np.ndarray): 2D array representing the automaton evolution.
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap="binary", interpolation="nearest")
    plt.title("Cellular Automaton Evolution")
    plt.xlabel("Cell Index")
    plt.ylabel("Time Step")
    plt.show()