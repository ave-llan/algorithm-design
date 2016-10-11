class Knapsack(object):
    def __init__(self, items, capacity):
        """
        :type items: (int, int) weight, value pair for each item
        :type capacity: int
        """
        self.items = items
        self.capacity = capacity
        self.__d = self.__optimize(items, capacity)

    def __optimize(self, items, capacity):
        d = [[0] * (capacity + 1)]
        for weight, value in items:
            row = []
            for x in range(capacity + 1):
                if weight > x:
                    row.append(d[-1][x])
                else:
                    row.append(max(d[-1][x], d[-1][x - weight] + value))
            d.append(row)
        return d

    @property
    def max_value(self):
        return self.__d[-1][-1]

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

if __name__ == "__main__":
    print(unit_test())
