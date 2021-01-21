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

Simplifying the denominator:
```
n = 2, P = 2 / 2^2 = 2 / 2!^2
n = 3, P = 18 / 6^2 = 18 / 3!^2
n = 4, P = 408 / 24^2 = 408 / 4!^2
n = 5, P = 11640 / 120^2 = 11640 / 5!^2
n = 6, P = 458640 / 720^2 = 458640 / 6!^2
n = 7, P = 23360400 / 5040^2 = 23360400 / 7!^2
```

So what's the left hand side?

```
f(2) = 2 = 2! * 1
f(3) = 18 = 3! * 3
f(4) = 408 = 4! * 17
f(5) = 11 640 = 5! * 97
f(6) = 458 640 = 6! * 647
f(7) = 23 360 400 = 7! * 4 635
```

So we can factor out a set of factorials.

```
f(2) = 1 / 2!
f(3) = 3 / 3!
f(4) = 17 / 4!
f(5) = 97 / 5!
f(6) = 647 / 6!
f(7) = 4635 / 7!
```

2 = 2
3 = 4
4 = 18
5 = 98
6 = 648
7 = 4636



