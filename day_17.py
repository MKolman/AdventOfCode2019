import intcode
from collections import deque

def get_inp():
  with open('input/day_17.txt') as f:
    return list(map(int, f.read().split(',')))

def easy():
  inp = get_inp()
  view = list(intcode.Runner(inp))
  view = ''.join(map(chr, view)).strip().split('\n')
  result = 0
  for i, line in enumerate(view):
    if i == 0 or i == len(view) - 1:
      continue
    for j, c in enumerate(line):
      if j == 0 or j == len(line) - 1:
        continue
      if c == line[j-1] == line[j+1] == view[i+1][j] == view[i-1][j] == '#':
        result += j * i
  return result

def get_nei(direction, x, y):
  # Return forward, left right in this order
  if direction == 0:  # Up
    return [(x, y-1), (x-1, y), (x+1, y)]
  if direction == 1:  # Right
    return [(x+1, y), (x, y-1), (x, y+1)]
  if direction == 2:  # Down
    return [(x, y+1), (x+1, y), (x-1, y)]
  if direction == 3:  # left
    return [(x-1, y), (x, y+1), (x, y-1)]

def hard():
  inp = get_inp()
  view = ''.join(map(chr, intcode.Runner(inp))).strip().split('\n')
  view = ['.' + line + '.' for line in view]
  view = ['.'* len(view[0])] + view + ['.'*len(view[0])]
  pos = [(x, y) for y, line in enumerate(view) for x, c in enumerate(line) if c in '^<>v']
  pos = pos[0]
  direction = '^>v<'.index(view[pos[1]][pos[0]])
  instructions = []
  while True:
    f, l, r = get_nei(direction, *pos)
    if view[f[1]][f[0]] == '#':
      pos = f
      instructions[-1] += 1
    elif view[l[1]][l[0]] == '#':
      pos = l
      instructions += ['L', 1]
      direction = (direction-1) % 4
    elif view[r[1]][r[0]] == '#':
      pos = r
      direction = (direction+1) % 4
      instructions += ['R', 1]
    else:
      break

  main = ','.join(map(str, instructions))
  # Find these manually ¯\_(ツ)_/¯
  A = 'L,10,R,8,R,6,R,10'
  B = 'L,12,R,8,L,12'
  C = 'L,10,R,8,R,8'
  main = main.replace(A, 'A')
  main = main.replace(B, 'B')
  main = main.replace(C, 'C')
  stdin = list(map(ord, '{}\n{}\n{}\n{}\nn\n'.format(main, A, B, C)))
  
  inp = get_inp()
  inp[0] = 2
  return list(intcode.Runner(inp, stdin))[-1]

def test():
  return easy() == 7328, hard() == 1289413

if __name__ == '__main__':
  print(easy())
  print(hard())
