import random

numberOfTrials = 100000000

numberOfHits = 0


for i in range(numberOfTrials):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0) 

    if x*x + y*y <= 1:
        numberOfHits+=1

pi = 4*numberOfHits/numberOfTrials

print(pi)