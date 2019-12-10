import math
from collections import defaultdict


def get_inp():
  with open('input/day_10.txt') as f:
    asteroids = []
    for i, line in enumerate(f):
      for j, cell in enumerate(line):
        if cell == '#':
          asteroids.append((j, i))
    return asteroids

def get_key(x, y):
  quad = {
    (1, -1): 1,
    (1, 1): 2,
    (-1, 1): 3,
    (-1, -1): 4,
  }
  return (quad[(math.copysign(1, x), math.copysign(1, y))], y*1./x if x else y * float('inf'))

def by_ang(asteroids, center_idx):
  cx, cy = asteroids[center_idx]
  result = defaultdict(list)
  for i, (x, y) in enumerate(asteroids):
    if i == center_idx:
      continue
    dx, dy = x-cx, y-cy
    key = get_key(dx, dy)
    result[key].append((abs(dx) + abs(dy), x, y))
  return result

def easy():
  asteroids = get_inp()
  max_los = (0, 0, 0)
  for i in range(len(asteroids)):
    max_los = max(max_los, (len(by_ang(asteroids, i)), i))
  # base at 29, 28
  return max_los

def hard():
  asteroids = get_inp()
  _, cidx = easy()
  ang_to_ast = by_ang(asteroids, cidx)
  key = list(sorted(ang_to_ast))[199]
  _, x, y = min(ang_to_ast[key])
  return x * 100 + y

def test():
  return easy() == (256, 262), hard() == 1707

if __name__ == '__main__':
  print(easy()[0])
  print(hard())