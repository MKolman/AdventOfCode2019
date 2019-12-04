DIRS = {
  'U': (0, 1),
  'D': (0, -1),
  'R': (1, 0),
  'L': (-1, 0),
}

def get_inp():
  result = []
  with open('input/day_03.txt') as f:
    for line in f:
      result.append([(0, 0, 0)])
      for step in line.split(','):
        d, n = step[0], int(step[1:])
        for i in range(n):
          p = result[-1][-1]
          result[-1].append((p[0]+DIRS[d][0], p[1]+DIRS[d][1]))
  return result

def easy():
  l1, l2 = get_inp()
  cross = set(l1[1:]) & set(l2[1:])
  return min(abs(x) + abs(y) for x, y in cross)

def hard():
  l1, l2 = get_inp()
  cross = set(l1[1:]) & set(l2[1:])
  d1, d2 = ({p: i for i, p in list(enumerate(l))[::-1]} for l in [l1, l2])
  return min(d1[p] + d2[p] for p in cross)

print(easy())
print(hard())