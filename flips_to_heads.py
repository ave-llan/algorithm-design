import random

def flip ():
    return random.randrange(2) == 0

def flipsToHeads ():
    count = 0
    while True:
        count += 1
        if flip():
            return count

def averageFlipsUntilHeads (numExperiments):
    return sum( (flipsToHeads() for _ in range(numExperiments)) ) / float(numExperiments)

def flipGenerator ():
    while True:
        yield flip()




print [averageFlipsUntilHeads(1000) for _ in range(5)]