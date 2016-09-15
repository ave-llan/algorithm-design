"""Implementation of a min heap."""

class MinHeap (object):
    """Standard min heap that offers remove_min and insert."""

    def __init__(self, nums=None):
        self.__h = [None]  + (list(nums) if nums else [])  # index 0 is not used
        # heapify
        for k in range(self.count, 0, -1):
            self.__sink(k)

    def insert(self, x):
        self.__h += [x]
        self.__swim(len(self.__h) - 1)

    def pop_min(self):
        min = self.min
        self.__swap(1, self.count)
        self.__h.pop()
        self.__sink(1)
        return min

    @property
    def min(self):
        """Get the current min."""
        return self.__h[1]

    @property
    def count(self):
        """Get the number of items in the heap."""
        return len(self.__h) - 1

    def __swim(self, k):
        """Move the value at index k up until heap order is restored."""
        while k  > 1 and self.__h[k] < self.__h[k / 2]:
            self.__swap(k, k / 2)
            k /= 2

    def __sink(self, k):
        """Move the value at index k down until heap order is restored."""
        while k  * 2 <= self.count:
            j = k * 2
            if j < self.count and self.__h[j + 1] < self.__h[j]:
                j += 1  # j + 1 is the less than j
            if not self.__h[j] < self.__h[k]:
                break
            self.__swap(k, j)
            k = j

    def __swap(self, k, j):
        """Swap the values at indices j and k."""
        self.__h[j], self.__h[k] = self.__h[k], self.__h[j]


# Test Code
def unit_tests():
    """Small battery of unit tests."""
    m = MinHeap()
    assert m.count == 0

    m.insert(5)
    assert m.min == 5
    assert m.count == 1

    m.insert(7)
    assert m.min == 5
    assert m.count == 2

    m.insert(4)
    assert m.min == 4
    assert m.count == 3

    m.insert(3)
    assert m.min == 3
    assert m.count == 4

    m.insert(12)
    assert m.min == 3
    assert m.count == 5

    assert m.pop_min() == 3
    assert m.min == 4
    assert m.count == 4

    from random import randrange
    nums = [randrange(-1000, 1000) for _ in range(1000)]
    m = MinHeap()
    used_nums = []
    for num in nums:
        assert m.count == len(used_nums)
        m.insert(num)
        used_nums.append(num)
        used_nums.sort()
        assert m.min == used_nums[0]
        if randrange(2):
            assert m.pop_min() == used_nums[0]
            used_nums = used_nums[1:]

    for num in sorted(used_nums):
        assert m.pop_min() == num
    assert m.count == 0

    # test with starting values
    m = MinHeap([5])
    assert m.min == 5
    assert m.count == 1
    m = MinHeap([])
    assert m.count == 0
    try:
        m.min
        raise AssertionError('Did not throw IndexError')
    except IndexError:
        pass  # IndexError should be thrown
    return 'unit_tests pass'

if __name__ == '__main__':
    print(unit_tests())
