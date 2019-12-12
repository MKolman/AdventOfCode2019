import math

def get_inp():
  with open('input/day_12.txt') as f:
    result = []
    for line in f:
      coor = []
      for c in line.strip()[1:-1].split(', '):
        coor.append(int(c[2:]))
      result.append(coor)
    return result

def gravity(coor):
  dv = [[0, 0, 0] for _ in coor]
  for i, pos1 in enumerate(coor):
    for j, pos2 in enumerate(coor[:i]):
      for k, (x1, x2) in enumerate(zip(pos1, pos2)):
        if x1 < x2:
          dv[i][k] += 1
          dv[j][k] -= 1
        elif x1 > x2:
          dv[i][k] -= 1
          dv[j][k] += 1
  return dv
def sum_mat(v, dv):
  return [[x+dx for x, dx in zip(p, dp)] for p, dp in zip(v, dv)]

def get_ens(c, v):
  return [sum(abs(x) for x in p) * sum(abs(x) for x in pv)
             for p, pv in zip(c, v)]

def easy():
  coor = get_inp()
  v = [[0, 0, 0] for _ in coor]
  for step in range(1000):
    dv = gravity(coor)
    v = sum_mat(v, dv)
    coor = sum_mat(coor, v)
  return sum(get_ens(coor, v))

def get_keys(c, v):
  return [tuple(x[i] for x in c+v) for i in range(3)]

def lcm(a, b):
    return a*b // math.gcd(a, b)

def hard():
  coor = get_inp()
  v = [[0, 0, 0] for _ in coor]
  started = [key for key in get_keys(coor, v)]
  done = [False] * 3
  for step in range(1000000):
    dv = gravity(coor)
    v = sum_mat(v, dv)
    coor = sum_mat(coor, v)
    keys = get_keys(coor, v)
    for i, (key, st) in enumerate(zip(keys, started)):
      if done[i] is False and key == st:
        done[i] = step+1
    if not sum(d is False for d in done):
      break
  return lcm(lcm(done[0], done[1]), done[2])

def test():
  return easy() == 6678, hard() == 496734501382552

if __name__ == '__main__':
  print(easy())
  print(hard())