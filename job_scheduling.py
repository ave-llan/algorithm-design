import sys

def greedySubtraction(job):
    """Key value of a job that sorts by weight-length, breaking ties by putting larger weight first."""
    weight, length = job
    return (weight - length, weight)

def greedyDivision(job):
    weight, length = job
    return float(weight) / float(length)


def optimize_schedule(jobs, greedyKey):
    """Order jobs to minimize total completion time.
        jobs is an array of tuples (Int, Int) represent (weight, length) of each job
    """
    jobs.sort(key=greedyKey, reverse=True)


def sumOfWeightedCompletionTimes(jobs):
    timeSpent, total = 0, 0
    for weight, length in jobs:
        timeSpent += length
        total += weight * timeSpent
    return total



def unit_test_sumOfWeightedCompletionTimes():
    assert sumOfWeightedCompletionTimes([(5, 1)]) == 5
    assert sumOfWeightedCompletionTimes([(5, 1), (3, 8)]) == 32
    assert sumOfWeightedCompletionTimes([(1, 1), (2, 2), (1, 1)]) == 11

def unit_test():
    unit_test_sumOfWeightedCompletionTimes()
    jobs = [(2, 1), (7, 3), (3, 1), (5, 1)]
    optimize_schedule(jobs, greedySubtraction)
    assert jobs == [(7, 3), (5, 1), (3, 1), (2, 1)]
    optimize_schedule(jobs, greedyDivision)
    assert jobs == [(5, 1), (3, 1), (7, 3), (2, 1)]
    return "unit_test pass"

def run_on_file():
    filepath = sys.argv[1]
    with open(filepath) as f:
        print(int(f.readline()))  # number of items in files
        jobs = [map(int, line.rstrip('\n').split()) for line in f.readlines()]

        optimize_schedule(jobs, greedySubtraction)
        print(sumOfWeightedCompletionTimes(jobs))

        optimize_schedule(jobs, greedyDivision)
        print(sumOfWeightedCompletionTimes(jobs))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(unit_test())
    elif len(sys.argv) == 2:
        run_on_file()
