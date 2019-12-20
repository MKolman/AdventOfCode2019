from collections import defaultdict, deque

def get_inp():
  with open('input/day_20.txt') as f:
    return [line for line in f]

def get_labels(inp):
  label2pos = defaultdict(list)
  for y, line in enumerate(inp):
    for x, c in enumerate(line):
      if c != '.':
        continue
      label = None
      if inp[y-1][x].isupper():
        label = inp[y-2][x] + inp[y-1][x]
      elif inp[y][x+1].isupper():
        label = inp[y][x+1] + inp[y][x+2]
      elif inp[y+1][x].isupper():
        label = inp[y+1][x] + inp[y+2][x]
      elif inp[y][x-1].isupper():
        label = inp[y][x-2] + inp[y][x-1]

      if label:
        label2pos[label].append((x, y))

  portals = dict()
  for label, pos in label2pos.items():
    if len(pos) == 2:
      p1, p2 = pos
      portals[p1] = p2
      portals[p2] = p1
  return label2pos, portals

def get_nei(inp, portals, x, y, depth=0):
  if (x, y) in portals:
    is_outer = y < 4 or y > len(inp) - 5 or x < 5 or x > len(inp[0]) - 5
    ddepth = is_outer * -2 + 1
    a, b = portals[(x, y)]
    if depth + ddepth >= 0:
      yield a, b, depth + ddepth
  for d in [-1, 1]:
    if inp[y][x+d] == '.':
      yield x+d, y, depth
    if inp[y+d][x] == '.':
      yield x, y+d, depth

def easy():
  inp = get_inp()
  label2pos, portals = get_labels(inp)
  start, stop = label2pos['AA'][0], label2pos['ZZ'][0]

  visited = set([start])
  q = deque([(0, start)])
  while q:
    dist, pos = q.popleft()
    for x, y, _ in get_nei(inp, portals, *pos):
      if (x, y) in visited:
        continue
      visited.add((x, y))
      if (x, y) == stop:
        return dist+1
      q.append((dist+1, (x, y)))

def hard():
  inp = get_inp()
  label2pos, portals = get_labels(inp)
  start, stop = label2pos['AA'][0], label2pos['ZZ'][0]

  visited = set([(start, 0)])
  q = deque([(0, start, 0)])
  while q:
    dist, pos, depth = q.popleft()
    for x, y, new_depth in get_nei(inp, portals, *pos, depth=depth):
      if ((x, y), new_depth) in visited:
        continue
      visited.add(((x, y), new_depth))
      if (x, y) == stop and depth == 0:
        return dist+1
      q.append((dist+1, (x, y), new_depth))

def test():
  return easy() == 516, hard() == 5966 

if __name__ == '__main__':
  print(easy())
  print(hard())