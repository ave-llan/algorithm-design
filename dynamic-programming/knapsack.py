class Knapsack(object):
    def __init__(self, items, capacity):
        """
        :type items: (int, int) weight, value pair for each item
        :type capacity: int
        """
        self.items = items
        self.capacity = capacity
        self.__d = self.__optimize(items, capacity)
        self.__used = self.reconstruct(items, self.__d)

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

    def reconstruct(self, items, d):
        x = len(d[0]) - 1
        used = []
        for i, item in reversed(zip(range(1, len(d)), items)):
            if d[i - 1][x] < d[i][x]:
                used.append(item)
                x -= item[0]
        return used

    @property
    def max_value(self):
        return self.__d[-1][-1]

    @property
    def used(self):
        return self.__used


def unit_test():
    k = Knapsack([], 10)
    assert k.max_value == 0
    assert k.used == []

    k = Knapsack([(5, 8)], 0)
    assert k.max_value == 0
    assert k.used == []

    k = Knapsack([(5, 8)], 10)
    assert k.max_value == 8
    assert k.used == [(5, 8)]

    k = Knapsack([(2, 3), (2, 2), (7, 5), (9, 2)], 10)
    assert k.max_value == 8
    assert sorted(k.used) == sorted([(2, 3), (7, 5)])

    k = Knapsack([(2, 3), (8, 7), (2, 2), (7, 5), (9, 2)], 10)
    assert k.max_value == 10
    assert sorted(k.used) == sorted([(2, 3), (8, 7)])

    return "unit_test pass"

if __name__ == "__main__":
    print(unit_test())
