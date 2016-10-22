from collections import Counter

def key_indexed_sort(items, num_keys):
    """returns an array of indices for items from the original array."""
    counts = Counter(items)
    items = [(i, item) for i, item in enumerate(items)]
    aux = [None] * len(items)
    key_count = [0]
    for i in range(num_keys):
        key_count.append(key_count[-1] + counts[i])
    for i, item in items:
        aux[key_count[item]] = i
        key_count[item] += 1
    return aux

def unit_test():
    assert key_indexed_sort([0, 1, 2], 3) == [0, 1, 2]
    assert key_indexed_sort([2, 1, 0], 3) == [2, 1, 0]
    assert key_indexed_sort([2, 1, 2, 2, 0], 3) == [4, 1, 0, 2, 3]
    return "unit_test pass"

if __name__ == "__main__":
    print(unit_test())