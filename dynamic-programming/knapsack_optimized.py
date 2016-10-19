"""Knapsack algorithm optimized to find only the max value and not list of used items.
    Uses two table rows.
"""

class Knapsack(object):
    def __init__(self, items, capacity):
        """
        :type items: (int, int) weight, value pair for each item
        :type capacity: int
        """
        self.items = items
        self.capacity = capacity
        self.__max_value = self.__optimize(items, capacity)

    def __optimize(self, items, capacity):
        items_remaining = len(items)
        prev = [0] * (capacity + 1)
        for weight, value in items:
            print(items_remaining)
            items_remaining -= 1
            prev = prev[:weight] + [max(prev[x], prev[x - weight] + value) 
                                    for x in range(weight, capacity + 1)]
        return prev[-1]

    @property
    def max_value(self):
        return self.__max_value


def unit_test():
    k = Knapsack([], 10)
    assert k.max_value == 0

    k = Knapsack([(5, 8)], 0)
    assert k.max_value == 0

    k = Knapsack([(5, 8)], 10)
    assert k.max_value == 8

    k = Knapsack([(2, 3), (2, 2), (7, 5), (9, 2)], 10)
    assert k.max_value == 8

    k = Knapsack([(2, 3), (8, 7), (2, 2), (7, 5), (9, 2)], 10)
    assert k.max_value == 10

    return "unit_test pass"


def solve_from_file(filepath):
    with open(filepath) as f:
        capacity, num_items = map(int, f.readline().rstrip('\n').split())
        items = [map(int, reversed(line.rstrip('\n').split())) for line in f.readlines()]
        knapsack = Knapsack(items, capacity)
        print(knapsack.max_value)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(unit_test())
    if len(sys.argv) == 2:
        solve_from_file(sys.argv[1])
