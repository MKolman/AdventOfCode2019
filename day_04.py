def get_inp():
  with open('input/day_04.txt') as f:
    return map(int, f.read().split('-'))

def easy():
  low, high = get_inp()
  cnt = 0
  for n in range(low, high):
    s = str(n)
    inc = all(a <= b for a, b in zip(s, s[1:]))
    rep = any(a == b for a, b in zip(s, s[1:]))
    cnt += inc and rep
  return cnt

def hard():
  low, high = get_inp()
  cnt = 0
  for n in range(low, high):
    s = str(n)
    inc = all(a <= b for a, b in zip(s, s[1:]))
    rep = any(s.count(c) == 2 for c in s)
    cnt += inc and rep
  return cnt

print(easy())
print(hard())