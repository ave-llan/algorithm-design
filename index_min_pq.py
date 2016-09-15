"""Implementation of an indexed min heap."""

class IndexMinPQ (object):
    """Indexed min heap that offers remove_min and insert."""

    def __init__(self, nums=None):
        self.__h = [None]
        self.__keys = {}           # val -> priority
        self.__index_in_heap = {}  # val -> index in __h

    def insert(self, x, p):
        """Insert item x with priority p."""
        if x in self.__keys:
            return self.update_priority(x, p)
        self.__h += [x]
        self.__index_in_heap[x] = self.count
        self.__keys[x] = p
        self.__swim(self.count)

    def pop_min(self):
        min = self.min
        self.__swap(1, self.count)
        self.__h.pop()
        del self.__keys[min]
        del self.__index_in_heap[min]
        self.__sink(1)
        return min

    def update_priority(self, x, p):
        """Update the priority value of x to be p."""
        if x not in self.__keys:
            raise KeyError('Cannot update priority of a value not in PQ')
        previous_p, i = self.__keys[x], self.__index_in_heap[x]
        self.__keys[x] = p
        if p < previous_p:
            self.__swim(i)
        elif p > previous_p:
            self.__sink(i)

    @property
    def min(self):
        """Get the current min."""
        return self.__h[1]

    @property
    def count(self):
        """Get the number of items in the heap."""
        return len(self.__h) - 1

    def __contains__(self, x):
        """Return True if x in the IndexMinPQ."""
        return x in self.__keys

    def __swim(self, k):
        """Move the value at index k up until heap order is restored."""
        while k  > 1 and self.__is_less(k, k / 2):
            self.__swap(k, k / 2)
            k /= 2

    def __sink(self, k):
        """Move the value at index k down until heap order is restored."""
        while k  * 2 <= self.count:
            j = k * 2
            if j < self.count and self.__is_less(j + 1, j):
                j += 1  # j + 1 is the less than j
            if not self.__is_less(j, k):
                break
            self.__swap(k, j)
            k = j

    def __swap(self, k, j):
        """Swap the values at indices j and k."""
        self.__index_in_heap[self.__h[k]] = j
        self.__index_in_heap[self.__h[j]] = k
        self.__h[j], self.__h[k] = self.__h[k], self.__h[j]

    def __is_less(self, k, j):
        return self.__keys[self.__h[k]] < self.__keys[self.__h[j]]


# Test Code
def unit_tests():
    """Small battery of unit tests."""
    m = IndexMinPQ()
    assert m.count == 0

    m.insert('zebra', 10)
    assert m.count == 1
    assert m.min == 'zebra'

    m.insert('bat', 4)
    assert m.count == 2
    assert m.min == 'bat'

    m.insert('frog', 22)
    m.insert('cow', 34)
    m.insert('snake', 33)
    m.insert('dog', 5)
    assert m.count == 6

    assert 'frog' in m
    assert 'finch' not in m

    assert m.pop_min() == 'bat'
    assert m.count == 5

    assert m.min == 'dog'

    m.update_priority('dog', 25)
    assert m.min == 'zebra'

    m.update_priority('snake', 1)
    assert m.pop_min() == 'snake'

    return 'unit_tests pass'

if __name__ == '__main__':
    print(unit_tests())
