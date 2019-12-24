def get_inp():
  with open('input/day_24.txt') as f:
    inp = f.read() \
           .replace('\n', '') \
           .replace('.' ,'0') \
           .replace('#', '1')
    return int(inp[::-1], 2)

def get_nei(i):
  x, y = i % 5, i // 5
  if x != 0:
    yield x-1 + 5*y
  if y != 0:
    yield x + 5*(y-1)
  if x != 4:
    yield x+1 + 5*y
  if y != 4:
    yield x + 5*(y+1)

def step(state):
  result = 0
  for i in range(25):
    val = 1 << i
    num_nei = sum(bool(state & (1 << j)) for j in get_nei(i))
    if num_nei == 1 or (state & val, num_nei) == (0, 2):
      result |= val
  return result

def easy():
  state = get_inp()
  visited = set()
  while state not in visited:
    visited.add(state)
    state = step(state)
  return state

def get_nei_all(i):
  x, y = i % 5, i // 5
  # Left neighbors
  if x == 0:
    yield 11, -1
  elif (x, y) == (3, 2):
    yield from [(j, 1) for j in range(4, 25, 5)]
  else:
    yield i-1, 0

  # Right neighbors
  if x == 4:
    yield 13, -1
  elif (x, y) == (1, 2):
    yield from [(j, 1) for j in range(0, 25, 5)]
  else:
    yield i+1, 0

  # Top neighbors
  if y == 0:
    yield 7, -1
  elif (x, y) == (2, 3):
    yield from [(j, 1) for j in range(20, 25)]
  else:
    yield i-5, 0

  # Bottom neighbors
  if y == 4:
    yield 17, -1
  elif (x, y) == (2, 1):
    yield from [(j, 1) for j in range(5)]
  else:
    yield i+5, 0

def step_all(states):
  results = [0 for _ in states]
  n = len(states)
  for depth, state in enumerate(states):
    if state == states[(depth+1)%n] == states[depth-1] == 0:
      continue
    for i in range(25):
      if i == 12:
        continue
      val = 1 << i
      num_nei = sum(bool(states[(depth+d)%n] & (1 << j)) for j, d in get_nei_all(i))
      if num_nei == 1 or (state & val, num_nei) == (0, 2):
        results[depth] |= val
  return results

def hard():
  states = [get_inp()] + [0] * 202
  for i in range(200):
    states = step_all(states)
  return ''.join(map(bin, states)).count('1')

def prn(state):
  def coo2val(x, y):
    return 1 << (y*5 + x)
  for y in range(5):
    for x in range(5):
      print('.#'[bool(state&coo2val(x, y))], end='')
    print()

def prn_all(states):
  n = len(states)//2
  for i in range(-n, n):
    if states[i]:
      print(i)
      prn(states[i])


def test():
  return easy() == 7543003, hard() == 1975

if __name__ == '__main__':
  print(easy())
  print(hard())
