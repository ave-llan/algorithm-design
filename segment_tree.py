"""Segment tree with a fixed size that can return sums over a range."""

class SegmentTree(object):
    """Segment tree for arrays of a fixed size. Supports updates of values but not insertions/deletions."""

    class TreeNode(object):
        def __init__(self, interval, sum):
            self.interval = interval
            self.sum = sum

        def __str__(self):
            return "{0}={1}".format(str(self.interval), self.sum)

        def __repr__(self):
            return self.__str__()

    def __init__(self, nums):
        if not len(nums): return
        head = self.TreeNode((0, len(nums) - 1), 0)
        self.tree = [None, head]   # 1-based binary tree
        i = 1
        while i < len(self.tree):
            if not self.tree[i]:
                i += 1
                continue
            start, end = self.tree[i].interval
            if start == end:   # finished for this index, add value up the tree
                k, val = i, nums[start]
                while k > 0:
                    self.tree[k].sum += val
                    k /= 2
            else:
                mid = start + (end - start) / 2
                # TODO: fix so that tree is balanced at beginning and this next line is not needed
                self.tree += [None] * (i * 2 - len(self.tree))
                self.tree += [self.TreeNode((start, mid), 0), self.TreeNode((mid + 1, end), 0)]
            i += 1

    def sum_in_range(self, start, end):
        return self.__sum_in_range((start, end), 1)

    def update_val(self, i, new_val):
        change = new_val - self.sum_in_range(i, i)
        k = self.__tree_index_of(i)
        while k > 0:
            self.tree[k].sum += change
            k /= 2

    def __tree_index_of(self, i):
        """Get the index of index i in the tree. (The node with interveral [i, i])."""
        k = 1
        while True:
            start, end = self.tree[k].interval
            if start == end:
                return k
            k *= 2
            if i > start + (end - start) / 2:
                k += 1

    def __sum_in_range(self, range, k):
        if self.tree[k].interval == range:
            return self.tree[k].sum

        start, end = self.tree[k].interval
        target_start, target_end = range
        mid = start + (end - start) / 2
        if target_end <= mid:
            return self.__sum_in_range(range, k * 2)
        elif target_start > mid:
            return self.__sum_in_range(range, k * 2 + 1)
        else:
            return (self.__sum_in_range((target_start, mid), k * 2) +
                    self.__sum_in_range((mid + 1, target_end), k * 2 + 1))

def unit_test():
    t = SegmentTree([])
    t = SegmentTree([44])
    assert t.sum_in_range(0, 0) == 44

    nums = [8, 1, 7, 5, 2, 3, 1, 0, 12, 3]
    t = SegmentTree(nums)
    for i, thing in enumerate(t.tree):
        print i, thing
    assert t.sum_in_range(0, 1) == 9
    for i, num in enumerate(nums):
        assert t.sum_in_range(i, i) == num
    assert t.sum_in_range(0, len(nums) - 1) == sum(nums)

    import random
    for _ in range(1000):
        i, j = sorted([random.randrange(len(nums)), random.randrange(len(nums))])
        assert t.sum_in_range(i, j) == sum(nums[i:j + 1])

    nums[2] = -1
    t.update_val(2, -1)
    assert t.sum_in_range(2, 2) == -1
    assert t.sum_in_range(0, len(nums) - 1) == sum(nums)

    for _ in range(1000):
        i, num = random.randrange(len(nums)), random.randrange(-100, 100)
        nums[i] = num
        t.update_val(i, num)
        assert t.sum_in_range(i, i) == num
        assert t.sum_in_range(0, len(nums) - 1) == sum(nums)

    return "unit_tests pass"

if __name__ == "__main__":
    print(unit_test())
