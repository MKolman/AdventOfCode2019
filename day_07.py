from itertools import permutations

import intcode

def get_inp():
  with open('input/day_07.txt') as f:
    return list(map(int, f.read().split(',')))

def easy():
  result = float("-inf")
  code = get_inp()
  for perm in permutations(range(5)):
    val = 0
    for p in perm:
      val = next(intcode.Runner(code[:], [p, val]))
    result = max(val, result)
  return result

def hard():
  result = float("-inf")
  code = get_inp()
  for perm in permutations(range(5, 10)):
    val = 0
    gens = [intcode.Runner(code[:], [p]) for p in perm]
    try:
      while True:
        for i in range(5):
          gens[i].stdin.append(val)
          val = next(gens[i])
    except StopIteration:
      pass
    result = max(val, result)
  return result

print(easy())
print(hard())