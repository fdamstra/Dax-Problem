#! /usr/bin/env python3
from itertools import permutations
from itertools import product
from statistics import mean
import json

num_people = 3 # note: num_people is also number of ranks

if __name__ == "__main__":
    # Ranks is the possible ranks, which is 1 through num_people
    ranks = list(range(1, num_people+1))
    rankings = list(permutations(ranks, num_people))
    print(f'Possible rankings: {rankings}')
    paired_rankings = list(product(rankings, repeat=2))
    print(f'Possible pairs of rankings: {paired_rankings}')

    same_averages = 0
    for pair in paired_rankings:
        # for each pair of rankings, generate averages for each person
        averages = []
        r1 = pair[0]
        r2 = pair[1]
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
        print(f'Pair {pair[0]}, {pair[1]} [{contains_matches}]: {averages}')

    print('')
    print(f'Total: {same_averages} matched out of {len(paired_rankings)} possibilities.')
    print(f'   P = {same_averages/len(paired_rankings)}')

        

            


    
