class WeightedIndependentSetInPath(object):
    """Calculate max weight possible in a path using no neighboring members."""

    def __init__(self, weights):
        self.weights = weights
        self.__bestPrefix = self.__getMaxISForAllPrefixes(weights)
        self.__components = self.__reconstruct_components(self.__bestPrefix, weights)

    def __getMaxISForAllPrefixes(self, path):
        """Return maxWeight possible for each prefix i of path."""
        best_prefix = [0, path[0]]
        for weight in path[1:]:
            best_prefix.append(max(best_prefix[-1], best_prefix[-2] + weight))
        return best_prefix

    def __reconstruct_components(self, best_prefix, path):
        """From a given list of MaxWeight prefixes, reconstruct components used to build it."""
        components = []
        i = len(best_prefix) - 1
        while i >= 2:
            if best_prefix[i - 1] >= best_prefix[i - 2] + path[i - 1]:
                i -= 1
            else:
                components.append(path[i - 1])
                i -= 2
        if i == 1:
            components.append(path[i - 1])
        return components

    @property
    def max_weight(self):
        return self.__bestPrefix[-1]

    @property
    def components(self):
        return self.__components

def unit_test():
    wis = WeightedIndependentSetInPath([5])
    assert wis.max_weight == 5
    assert sorted(wis.components) == [5]

    wis = WeightedIndependentSetInPath([5, 4, 5, 4])
    assert wis.max_weight == 10
    assert sorted(wis.components) == [5, 5]

    wis = WeightedIndependentSetInPath([5, 0, 4, 5, 4])
    assert wis.max_weight == 13
    assert sorted(wis.components) == [4, 4, 5]

    wis = WeightedIndependentSetInPath([5, 2, 3, 8, 7, 0, 1])
    assert wis.max_weight == 16
    assert sorted(wis.components) == sorted([5, 3, 7, 1])

    return "unit_test pass"

if __name__ == "__main__":
    print(unit_test())
