import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colormaps as cm

__all__ = ["plot_rules_distributions", "plot_rules_combs", "plot_stats", "plot_scatter"]

def plot_rules_distributions(x_len, combinations_count):
    for c, v in combinations_count.items():
        plt.figure(figsize=(10, 5))
        plt.bar(range(x_len), v)
        plt.title(f"Combination {c}")
        plt.xlabel("Rule Index")
        plt.ylabel("Frequency")
        plt.show()

def plot_rules_combs(x_len, rules_combs):
    # Plot stacked bar chart for rules_combs
    x = range(x_len)  # X-axis: Rule indices
    keys = list(rules_combs[0].keys())  # Extract the keys from the first dictionary
    values_by_key = {key: [comb[key] for comb in rules_combs] for key in keys}

    # Use a colormap for better visibility
    cmap = cm.get_cmap("tab20c")  # Use 'tab10' colormap with one color per key
    colors = [cmap(i) for i in range(len(keys))]

    plt.figure(figsize=(15, 7))
    bottom = np.zeros(x_len)

    for idx, key in enumerate(keys):
        plt.bar(x, values_by_key[key], bottom=bottom, color=colors[idx], label=f"Key: {key}")
        bottom += np.array(values_by_key[key])  # Update the bottom for stacking

    # Highlight Rule 110 with an arrow
    rule_110_index = 109

    plt.annotate(
        "Rule 110",
        xy=(rule_110_index, 0),  # Arrow starting point (x-axis)
        xytext=(rule_110_index - 20, -50),  # Arrow's text position
        arrowprops=dict(facecolor="red", arrowstyle="->", lw=2),
        fontsize=12,
        color="red",
        fontweight="bold",
        ha="center"
    )

    # Finalize plot
    plt.title("Breakdown of Rules Combinations (Rule 110 Highlighted)")
    plt.xlabel("Rule Index")
    plt.ylabel("Contribution")
    plt.legend(title="Keys", loc="upper left")
    plt.tight_layout()
    plt.show()


def plot_stats(x_len, expected_value, title):
    plt.figure(figsize=(10, 5))
    plt.plot(range(x_len), expected_value, label="Expected Value", color="blue")
    
    # Highlight Rule 110 with a vertical line
    rule_110_index = 109
    plt.axvline(x=rule_110_index, color="red", linestyle="--", linewidth=0.5, label="Rule 110")

    # Add horizontal line for rule 110 value
    rule_110_value = expected_value[rule_110_index]
    plt.axhline(y=rule_110_value, color="black", linestyle="--", linewidth=0.5)
    
    # Add title, labels, and legend
    plt.title(f"{title} (Rule 110 Highlighted)")
    plt.xlabel("Rule Index")
    plt.ylabel("Expected Value")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_scatter(x_len, expected_value, reproduction_rate):
    plt.figure(figsize=(15, 15))
    plt.scatter(expected_value, reproduction_rate, c=range(x_len), cmap="viridis")
    # Highlight Rule 110 with a vertical line
    rule_110_index = 109
    rule_110_y = reproduction_rate[rule_110_index]
    plt.axhline(y=rule_110_y, color="black", linestyle="--", linewidth=0.5, label="Rule 110")

    # Add horizontal line for rule 110 value
    rule_110_x = expected_value[rule_110_index]
    plt.axvline(x=rule_110_x, color="red", linestyle="--", linewidth=0.5)

    # add x = y line
    plt.plot(expected_value, expected_value, color="green", label="x = y")

    plt.colorbar(label="Rule")
    plt.xlabel("Expected Value Of Life")
    plt.ylabel("Reproduction Rate")
    plt.title("Reproduction Rate vs Expected Value Of Life")
    plt.show()