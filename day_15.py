import intcode
from collections import deque

def get_inp():
  with open('input/day_15.txt') as f:
    return list(map(int, f.read().split(',')))

def mv(x, y, dr):
  if dr == 1:
    return x, y-1
  if dr == 2:
    return x, y+1
  if dr == 3:
    return x-1, y
  if dr == 4:
    return x+1, y

def flood(game):
  visited = set([(0, 0)])
  q = deque([(0, (0, 0), game)])
  while len(q):
    l, (x, y), game = q.popleft()
    for i in range(4):
      nx, ny = mv(x, y, i+1)
      if (nx, ny) in visited:
        continue
      subgame = intcode.Runner(game)
      subgame.stdin = [i+1]
      success = next(subgame)
      visited.add((nx, ny))
      if success == 1:
        q.append((l+1, (nx, ny), subgame))
      elif success == 2:
        return l+1, subgame
  return l, subgame

def easy():
  state = get_inp()
  visited = set([(0, 0)])
  return flood(intcode.Runner(state))[0]

def hard():
  state = get_inp()
  game = intcode.Runner(state)
  # Flood to find Oxygen tank
  game = flood(game)[1]
  # Flood from oxygen tank
  return flood(game)[0]


def test():
  return easy() == 304, hard() == 310

if __name__ == '__main__':
  print(easy())
  print(hard())
