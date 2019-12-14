from collections import defaultdict
import math

def element(s):
  ndest, dest = s.split()
  return dest, int(ndest)

def get_inp():
  with open('input/day_14.txt') as f:
    result = dict()
    for line in f:
      inp, out = line.split('=>')
      dest, ndest = element(out)
      src = list(map(element, inp.split(', ')))
      result[dest] = ndest, src
    return result

def expand(react, start):
  stack = [start]
  result = set()
  while len(stack):
    el = stack.pop()
    for src, _ in react[el][1]:
      if src not in result:
        result.add(src)
        if src in react:
          stack.append(src)
  return result

def get_dag(expans):
  result = ['ORE']
  indag = {'ORE'}
  full = set(expans)
  full.add('ORE')
  while indag < full:
    for src, val in expans.items():
      if val <= indag and src not in indag:
        result.append(src)
        indag.add(src)
  return result

def easy(nfuel=1):
  react = get_inp()
  expans = {src: expand(react, src) for src in react}
  recipe = defaultdict(int)
  recipe['FUEL'] = nfuel
  for el in get_dag(expans)[:0:-1]:
    nel = recipe[el]
    quant, srcs = react[el]
    nbatch = math.ceil(nel/quant)
    for src, nsrc in srcs:
      recipe[src] += nsrc * nbatch
  return recipe['ORE']

def hard():
  nore = 1000000000000
  lo, hi = 1, 10000000
  assert easy(lo) < nore < easy(hi)
  while hi-lo > 1:
    mid = (hi+lo)//2
    if easy(mid) > nore:
      hi = mid
    else:
      lo = mid
  return lo

def test():
  return easy() == 892207, hard() == 1935265

if __name__ == '__main__':
  print(easy())
  print(hard())
