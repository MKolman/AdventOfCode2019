def get_inp():
  with open('input/day_04.txt') as f:
    return map(int, f.read().split('-'))

def num_gen(depth=6, prev=""):
  if depth == 0:
    yield prev
  else:
    low = int(prev[-1]) if prev else 1
    for d in range(low, 10):
      for r in num_gen(depth-1, prev + str(d)):
        yield r

def easy():
  low, high = get_inp()
  cnt = 0
  for s in num_gen():
    rep = any(a == b for a, b in zip(s, s[1:]))
    cnt += rep and low < int(s) < high
  return cnt

def hard():
  low, high = get_inp()
  cnt = 0
  for s in num_gen():
    rep = any(s.count(c) == 2 for c in s)
    cnt += rep and low < int(s) < high
  return cnt

def test():
  return easy() == 2050, hard() == 1390

if __name__ == "__main__":
  print(easy())
  print(hard())
