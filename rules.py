# filename: rules.py
# Author: Giorgio Campisano
# Description: A module for defining rules for 1D cellular automata.
# Date: 2025-01-18

class Rule:
    """Parameterized rule class for 1D cellular automata."""
    def __init__(self, rule_number, state_count=2, neighborhood_size=3):
        self.state_count = state_count
        self.neighborhood_size = neighborhood_size
        self.rule_number = rule_number
        self.rule_map = self._generate_rule_map()

    def __str__(self):
        neighborhoods = [f"{''.join([f'{i}' for i in k])}" 
                         for k, _ in self.rule_map.items()]
        outputs = [f" {v} " for _, v in self.rule_map.items()]
        return (f"""Rule {self.rule_number}
                Rule space: {"  ".join(neighborhoods)}
                            {"  ".join(outputs)}""") 

    def _generate_rule_map(self):
        """Generate a mapping from neighborhood to state based on the rule number."""
        num_combinations = self.state_count ** self.neighborhood_size
        binary_repr = f"{self.rule_number:0{num_combinations}b}"
        combinations = [
            tuple(int(x) for x in f"{i:0{self.neighborhood_size}b}")
            for i in range(num_combinations)
        ]
        return dict(zip(combinations, map(int, reversed(binary_repr))))

    def apply(self, neighborhood):
        return self.rule_map[tuple(neighborhood)]

    def reconstruct_past(self):
        """Reconstruct the possible past states of a given state."""
        rules = list(self.rule_map.keys())
        combinations = generate_combinations(rules, self.neighborhood_size)

        counter = {k: 0 for k in rules}
        # print(counter)
        for c in combinations:
            rule = []
            for i in range(self.neighborhood_size):
                rule.append(self.apply(c[i:i + self.neighborhood_size]))

            counter[tuple(rule)] += 1

        return counter

def generate_combinations(rules, neighborhood_size):
    combinations = []

    for r in rules:
        combinations += combine(list(r), neighborhood_size, 0)
        
    return combinations

def combine(rule, neighborhood_size, i):
    if i == neighborhood_size - 1:
        return [rule]
    else:
        rule_a = rule + [0]
        rule_b = rule + [1]
        return combine(rule_a, neighborhood_size, i + 1) + combine(rule_b, neighborhood_size, i + 1)
    
            
            
if __name__ == "__main__":
    rule = Rule(12)

    print(rule.reconstruct_past())