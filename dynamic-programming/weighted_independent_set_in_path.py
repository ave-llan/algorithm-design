class WeightedIndependentSetInPath(object):
    """Calculate max weight possible in a path using no neighboring members."""

    def __init__(self, weights):
        self.weights = weights
        self.__bestPrefix = self.__getMaxISForAllPrefixes(weights)

    def __getMaxISForAllPrefixes(self, path):
        """Return maxWeight possible for each prefix i of path."""
        bestPrefix = [0, path[0]]
        for weight in path[1:]:
            bestPrefix.append(max(bestPrefix[-1], bestPrefix[-2] + weight))
        return bestPrefix

    @property
    def maxWeight(self):
        return self.__bestPrefix[-1]

def unit_test():
    wis = WeightedIndependentSetInPath([5])
    assert wis.maxWeight == 5

    wis = WeightedIndependentSetInPath([5, 4, 5, 4])
    assert wis.maxWeight == 10

    wis = WeightedIndependentSetInPath([5, 0, 4, 5, 4])
    assert wis.maxWeight == 13
    return "unit_test pass"

if __name__ == "__main__":
    print(unit_test())
