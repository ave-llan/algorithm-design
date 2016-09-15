import random

def rselect(a, i):
    """Given array a, select the ith order statistic."""
    print("reselct called on size {0}".format(len(a)))
    print(a, i)
    if i > len(a): 
        return None
    if len(a) == 1:
        return a[i]

    j = partition(a, choosePivotIndex(a))
    if j == i:
        return a[j]
    if j > i:
        print("went left")
        return rselect(a[:j], i)
    else:
        print("went right")
        return rselect(a[j + 1:], i - (j + 1))

def choosePivotIndex(a):
    """Randomly select a pivot index from array a."""
    return random.randrange(0, len(a))

def partition(a, pivot_index):
    """Partition array arround the element at pivot_index."""
    p = a[pivot_index]
    a[0], a[pivot_index] = a[pivot_index], a[0]  # move pivot to start
    i = 1

    for j in range(1, len(a)):
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[0], a[i - 1] = a[i - 1], a[0]              # move pivot into place
    return i - 1


a = [i for i in range(100)]
# a = [2, 1]
random.shuffle(a)
# print(a)
print(rselect(a, 50))
# print(a)
