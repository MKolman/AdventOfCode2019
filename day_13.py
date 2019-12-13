import intcode
from collections import defaultdict
import sys

def get_inp():
  with open('input/day_13.txt') as f:
    return list(map(int, f.read().split(',')))

def easy():
  state = get_inp()
  game = list(intcode.Runner(state))
  tiles = defaultdict(int)
  for i in range(0, len(game), 3):
    tiles[(game[i], game[i+1])] = game[i+2]
  return list(tiles.values()).count(2)

def prn(tiles):
  print(tiles[(-1, 0)])
  for i in range(30):
    for j in range(50):
      print(' #H-o'[tiles[(j, i)]], end='')
    print()

def hard():
  state = get_inp()
  state[0] = 2
  game = intcode.Runner(state)
  tiles = defaultdict(int)
  ballx, paddlex = -1, -1
  buf = []
  class Stdin(object):
    def __init__(self):
      pass
    def __len__(self):
      return 1
    def __getitem__(self, key):
      if isinstance(key, slice):
        return self
      if ballx < paddlex:
        return -1
      if ballx > paddlex:
        return 1
      return 0

  game.stdin = Stdin()
  for n in game:
    if n is not None:
      buf.append(n)
    else:
      assert(False)
    if len(buf) == 3:
      x, y, tile = buf
      tiles[(x, y)] = tile
      ballx = x if tile == 4 else ballx
      paddlex = x if tile == 3 else paddlex
      buf = []
  return tiles[(-1, 0)]

def test():
  return easy() == 268, hard() == 13989

if __name__ == '__main__':
  print(easy())
  print(hard())