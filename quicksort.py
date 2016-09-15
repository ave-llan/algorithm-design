import sys
print(sys.argv)





def quicksort (a):
    quicksortSub(a, 0, len(a) - 1)


def quicksortSub(a, l, r):
    if r - l <= 1:
        return
    p = partition(a, l, r)
    quicksortSub(a, l, p - 1)
    quicksortSub(a, p + 1, r)
    return

def partition(a, l, r):
    p = choosePivot(a, l, r)
    a[p], a[l] = a[l], a[p]          # put pivot at start
    pivot = a[p]

    i = l + 1
    for j in range(l + 1, r + 1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i - 1] = a[i - 1], a[l]  # move pivot into place
    return p

def choosePivot(a, l, r):
    return l


# test = [i for i in range(10)]
# quicksort(test)
# print(test)

filepath = sys.argv[1]
print(filepath)
with open(filepath) as f:
    lines = f.read().splitlines()
    numbers = [int(e) for e in lines]
    quicksort(numbers)
    print numbers