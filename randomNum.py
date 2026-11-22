#!/usr/bin/python3

import argparse
import sys

# Random number using the middle square method
def nextRand(seed: int):
    numString = str(seed ** 2).zfill(8)
    middleFour = numString[-6:-2]
    return int(middleFour)

parser = argparse.ArgumentParser(description="Generate a series of random numbers using the middle square method.")
parser.add_argument("seed", help="Seed for the random number generator", type=int)
parser.add_argument("-c", "--count", type=int, default=1, help="Number of steps into seed to print")
parser.add_argument("-u", "--upper", type=int, default=10000, help="Upper value possible (max 9999)")
parser.add_argument("-l", "--lower", type=int, default=0, help="Lower value possible (min 0)")
parser.add_argument("-s", "--stats", action="store_true", help="Print a bar graph for num appearances of each value")

args = parser.parse_args()

seed = args.seed
count = args.count
upper = args.upper
lower = args.lower

doStats = args.stats

if not (0 <= args.lower <= args.upper <= 10000):
    sys.exit("Error: Bounds must be in form 0 <= lower <= upper <= 9999")

if count < 1:
    sys.exit("Error: Count must be at least 1")

if doStats:
    numBin = [0] * ((upper - lower) + 1)

for i in range(count):
    random = nextRand(seed) 
    seed = random
    random = (random % (upper - lower + 1)) + lower
    if count > 1:
        print(f"{i + 1}. {random}")
    else:
        print(random)
    numBin[(random - lower)] += 1


if doStats:
    print()

    for i in range(len(numBin)):
        label = i + lower
        bar = "█" * numBin[i]
        print(f"{label:<5} | {bar} {numBin[i]}")
        




