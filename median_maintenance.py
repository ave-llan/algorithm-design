"""Takes a stream of numbers and maintains the median."""

from heap import Heap

class MedianMaintainer(object):
    """Maintain medium while a stream of objects are inserted."""

    def __init__(self):
        self.left  = Heap(isOrderedBefore=lambda a, b: a > b)
        self.right = Heap(isOrderedBefore=lambda a, b: a < b)

    def insert(self, x):
        if self.left.is_empty or x < self.left.top:
            self.left.insert(x)
        else:
            self.right.insert(x)
        while self.left.count < self.right.count:
            self.left.insert(self.right.pop_top())
        while self.left.count > self.right.count + 1:
            self.right.insert(self.left.pop_top())

    @property
    def median(self):
        return self.left.top


def unit_test():
    """Unit test MedianMaintainer."""
    m = MedianMaintainer()
    m.insert(4)
    assert m.median == 4
    m.insert(2)
    assert m.median == 2
    m.insert(12)
    assert m.median == 4
    m.insert(23)
    assert m.median == 4
    m.insert(21)
    assert m.median == 12
    m.insert(0)
    assert m.median == 4
    m.insert(1)
    assert m.median == 4
    m.insert(0)
    assert m.median == 2
    return 'unit_test passed'

if __name__ == '__main__':
    print(unit_test())
