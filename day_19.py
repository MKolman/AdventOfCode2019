import intcode
from collections import deque

def get_inp():
  with open('input/day_19.txt') as f:
    return list(map(int, f.read().split(',')))

def easy():
  state = get_inp()
  stdin = ((x, y) for x in range(50) for y in range(50))
  result = 0
  for x, y in stdin:
    result += next(intcode.Runner(state[:], [x, y]))
  return result

def hard():
  state = get_inp()
  starty = 10
  startx, stopx = None, None
  for x in range(starty):
    beam = next(intcode.Runner(state[:], [x, starty]))
    if beam and startx is None:
      startx = [x]
    elif not beam and startx is not None:
      stopx = [x]
      break

  for y in range(starty+1, 1100):
    for expected, store in enumerate([stopx, startx]):
      x = store[-1]
      beam = next(intcode.Runner(state[:], [x, y]))
      if beam != expected:
        x += 1
      store.append(x)

  for y, (start, stop) in enumerate(zip(startx[99:], stopx)):
    if stop - start >= 100:
      return 10000*start + y + starty

def test():
  return easy() == 166, hard() == 3790981

if __name__ == '__main__':
  print(easy())
  print(hard())
