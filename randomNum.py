#!/usr/bin/python3

# Random number using the middle square method
def nextRand(seed: int):
    numString = str(seed ** 2)
    
    # Insert 0s at front until eight digits
    while len(numString) < 8:
        numString = "0" + numString

    middleFour = numString[2:-2]

    return int(middleFour)

import argparse

parser = argparse.ArgumentParser(description="Generate a series of random numbers using the middel square method.")
parser.add_argument("seed", help="Seed for the random number generator", type=int)
parser.add_argument("-c", "--count", type=int, default=1, help="Number of steps into seed to print")
parser.add_argument("-u", "--upper", type=int, default=9999, help="Upper value possible (max 9999)")
parser.add_argument("-l", "--lower", type=int, default=0, help="Lower value possible (min 0)")
parser.add_argument("-s", "--stats", action="store_true", help="Print a bar graph for num appearances of each value")

args = parser.parse_args()

seed = args.seed
count = args.count
upper = args.upper
lower = args.lower

numBin = [0] * ((upper - lower) + 1)

doStats = args.stats

for i in range(count):
    random = nextRand(seed) 
    seed = random
    random = (random % upper) + lower
    print(f"{i + 1}. {random}")
    numBin[(random - lower)] += 1

if doStats:
    print()

    for i in range(len(numBin)):
        label = i + lower
        bar = "█" * numBin[i]
        print(f"{label:<5} | {bar} {numBin[i]}")
        




