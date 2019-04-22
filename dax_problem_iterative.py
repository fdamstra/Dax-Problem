#! /usr/bin/env python3
from itertools import permutations
from itertools import product
from statistics import mean
import json

MAX = 100

def dax_problem(num_people):
    # Ranks is the possible ranks, which is 1 through num_people
    ranks = range(1, num_people+1)
    rankings = permutations(ranks, num_people)
    #print(f'Possible rankings: {rankings}')
    paired_rankings = product(rankings, repeat=2)
    #print(f'Possible pairs of rankings: {paired_rankings}')

    same_averages = 0
    num_permutations = 0
    for pair in paired_rankings:
        # for each pair of rankings, generate averages for each person
        averages = []
        r1 = pair[0]
        r2 = pair[1]
        num_permutations += 1
        for i in range(0, num_people):
            averages.append((r1[i]+r2[i])/2)
        # determine if there's any match within the averages by comparing
        # the length of the list to the lenght of the set (which doesn't
        # allow repeats
        if len(averages) != len(set(averages)):
            same_averages += 1
            contains_matches = True
        else:
            contains_matches = False
        #print(f'Pair {pair[0]}, {pair[1]} [{contains_matches}]: {averages}')
    #print('')
    #print(f'Total: {same_averages} matched out of {len(paired_rankings)} possibilities.')
    print(f'n = {n}, P = {same_averages}/{num_permutations} = {same_averages/num_permutations}')
    return same_averages/num_permutations
        

if __name__ == "__main__":
    for n in range(2, MAX+1):
        dax_problem(n)
