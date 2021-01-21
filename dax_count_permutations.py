#! /usr/bin/env python3
from itertools import permutations

MAX = 100

def dax_problem(num_people):
    # Ranks is the possible ranks, which is 1 through num_people
    ranks = range(1, num_people+1)
    rankings = permutations(ranks, num_people)

    same_averages = 0
    num_permutations = 0
    for perm in rankings:
        num_permutations += 1
        if num_permutations == 1:
            continue
        # for each permutation (besides the identity), compare it to the identity
        sums = []
        for i in range(0, num_people):
            sums.append(ranks[i] + perm[i])
        # determine if there's any match within the averages by comparing
        # the length of the list to the length of the set (which doesn't
        # allow repeats
        if len(sums) != len(set(sums)):
            same_averages += 1
            contains_matches = True
        else:
            contains_matches = False
        #print(f'Pair {pair[0]}, {pair[1]} [{contains_matches}]: {averages}')
    #print('')
    #print(f'Total: {same_averages} matched out of {len(paired_rankings)} possibilities.')
    #print(f'n = {num_people}, P = {same_averages}/{num_permutations-1} = {same_averages/(num_permutations-1)}')
    print(f'n = {num_people}, num_matches = {same_averages}')
    return same_averages/num_permutations
        

if __name__ == "__main__":
    for n in range(2, MAX+1):
        dax_problem(n)
