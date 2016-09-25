import sys

def has_pair_that_sums_to(target, distincts):
    # distincts = set(nums) - set([target / 2])
    for num in distincts:
        if target - num in distincts:
            return True
    return False


def unit_tests():
    assert not has_pair_that_sums_to(4, [0, 1, 2, 5])
    assert not has_pair_that_sums_to(4, [0, 1, 2, 2])
    assert has_pair_that_sums_to(4, [0, 1, 2, 2, 4])
    return "unit_tests passed"

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(unit_tests())
    elif len(sys.argv) == 2:
        filepath = sys.argv[1]
        with open(filepath) as f:
            nums = [int(num) for num in f.read().splitlines()]
            distincts = set(nums)
            print sum((has_pair_that_sums_to(i, distincts - set([i / 2])) for i in range(-10000, 10001)))
