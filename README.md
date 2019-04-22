# The Dax Problem
Presented by Daniel Bernstein

## Informal Statement
Suppose each of n people are randomly assigned a rank 1 through n (assume
a uniform distribution). Do this twice in a row and take the average rank
for each person. What are the chances that you end up with two people who
have the same average rank?

## More formal
See `dax_problem.jpg`

## Simulation
`python3 dax_problem.py` will run it once for a given value of `n`, with
lots of accompanying details so you can check my work.

`python3 dax_problem_iterative.py` will run it multiple times for values
of `n` so you can try to find a pattern.

## Results/Output

### n=2
Results for n=2:
```
Pair (1, 2), (1, 2) [False]: [1.0, 2.0]
Pair (1, 2), (2, 1) [True]: [1.5, 1.5]
Pair (2, 1), (1, 2) [True]: [1.5, 1.5]
Pair (2, 1), (2, 1) [False]: [2.0, 1.0]

Total: 2 matched out of 4 possibilities.
   P = 0.5
```

### n = 3
Results for n=3
```
Pair (1, 2, 3), (1, 2, 3) [False]: [1.0, 2.0, 3.0]
Pair (1, 2, 3), (1, 3, 2) [True]: [1.0, 2.5, 2.5]
Pair (1, 2, 3), (2, 1, 3) [True]: [1.5, 1.5, 3.0]
Pair (1, 2, 3), (2, 3, 1) [False]: [1.5, 2.5, 2.0]
Pair (1, 2, 3), (3, 1, 2) [False]: [2.0, 1.5, 2.5]
Pair (1, 2, 3), (3, 2, 1) [True]: [2.0, 2.0, 2.0]
Pair (1, 3, 2), (1, 2, 3) [True]: [1.0, 2.5, 2.5]
Pair (1, 3, 2), (1, 3, 2) [False]: [1.0, 3.0, 2.0]
Pair (1, 3, 2), (2, 1, 3) [False]: [1.5, 2.0, 2.5]
Pair (1, 3, 2), (2, 3, 1) [True]: [1.5, 3.0, 1.5]
Pair (1, 3, 2), (3, 1, 2) [True]: [2.0, 2.0, 2.0]
Pair (1, 3, 2), (3, 2, 1) [False]: [2.0, 2.5, 1.5]
Pair (2, 1, 3), (1, 2, 3) [True]: [1.5, 1.5, 3.0]
Pair (2, 1, 3), (1, 3, 2) [False]: [1.5, 2.0, 2.5]
Pair (2, 1, 3), (2, 1, 3) [False]: [2.0, 1.0, 3.0]
Pair (2, 1, 3), (2, 3, 1) [True]: [2.0, 2.0, 2.0]
Pair (2, 1, 3), (3, 1, 2) [True]: [2.5, 1.0, 2.5]
Pair (2, 1, 3), (3, 2, 1) [False]: [2.5, 1.5, 2.0]
Pair (2, 3, 1), (1, 2, 3) [False]: [1.5, 2.5, 2.0]
Pair (2, 3, 1), (1, 3, 2) [True]: [1.5, 3.0, 1.5]
Pair (2, 3, 1), (2, 1, 3) [True]: [2.0, 2.0, 2.0]
Pair (2, 3, 1), (2, 3, 1) [False]: [2.0, 3.0, 1.0]
Pair (2, 3, 1), (3, 1, 2) [False]: [2.5, 2.0, 1.5]
Pair (2, 3, 1), (3, 2, 1) [True]: [2.5, 2.5, 1.0]
Pair (3, 1, 2), (1, 2, 3) [False]: [2.0, 1.5, 2.5]
Pair (3, 1, 2), (1, 3, 2) [True]: [2.0, 2.0, 2.0]
Pair (3, 1, 2), (2, 1, 3) [True]: [2.5, 1.0, 2.5]
Pair (3, 1, 2), (2, 3, 1) [False]: [2.5, 2.0, 1.5]
Pair (3, 1, 2), (3, 1, 2) [False]: [3.0, 1.0, 2.0]
Pair (3, 1, 2), (3, 2, 1) [True]: [3.0, 1.5, 1.5]
Pair (3, 2, 1), (1, 2, 3) [True]: [2.0, 2.0, 2.0]
Pair (3, 2, 1), (1, 3, 2) [False]: [2.0, 2.5, 1.5]
Pair (3, 2, 1), (2, 1, 3) [False]: [2.5, 1.5, 2.0]
Pair (3, 2, 1), (2, 3, 1) [True]: [2.5, 2.5, 1.0]
Pair (3, 2, 1), (3, 1, 2) [True]: [3.0, 1.5, 1.5]
Pair (3, 2, 1), (3, 2, 1) [False]: [3.0, 2.0, 1.0]

Total: 18 matched out of 36 possibilities.
   P = 0.5
```

### Iterative:
This is a nonpolynomial solution to the problem, so it gets beyond my PC's processing power
very quickly.

```
n = 2, P = 2/4 = 0.5
n = 3, P = 18/36 = 0.5
n = 4, P = 408/576 = 0.7083333333333334
n = 5, P = 11640/14400 = 0.8083333333333333
n = 6, P = 458640/518400 = 0.8847222222222222
n = 7, P = 23360400/25401600 = 0.9196428571428571
```


