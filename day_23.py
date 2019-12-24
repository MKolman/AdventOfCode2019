import intcode
from collections import deque

def get_inp():
  with open('input/day_23.txt') as f:
    return list(map(int, f.read().split(',')))

class Queue(object):
  def __init__(self, start=None):
    self.data = start or []
  def __len__(self):
    return 1
  def __getitem__(self, key):
    if isinstance(key, slice):
      return self
    if self.data:
      result, self.data = self.data[0], self.data[1:]
      return result
    raise StopIteration

def easy():
  state = get_inp()
  computers = [intcode.Runner(state[:], Queue([i])) for i in range(50)]
  while True:
    for num, comp in enumerate(computers):
      sent = list(comp)
      for i in range(0, len(sent), 3):
        dest, x, y = sent[i:i+3]
        if dest == 255:
          return y
        computers[dest].stdin.data += [x, y]
      if len(sent):
        break
    else:
      for comp in computers:
        comp.stdin.data.append(-1)

def hard():
  state = get_inp()
  computers = [intcode.Runner(state[:], Queue([i])) for i in range(50)]
  last_sent_y = None
  nat = None
  is_idle = False
  while True:
    for num, comp in enumerate(computers):
      sent = list(comp)
      for i in range(0, len(sent), 3):
        dest, x, y = sent[i:i+3]
        if dest == 255:
          nat = [x, y]
        else:
          computers[dest].stdin.data += [x, y]
      if len(sent):
        is_idle = False
        break
    else:
      if is_idle:
        if nat[1] == last_sent_y:
          return last_sent_y
        computers[0].stdin.data += nat
        last_sent_y = nat[1]
      else:
        is_idle = True
        for comp in computers:
          comp.stdin.data.append(-1)

def test():
  return easy() == 19040, hard() == 11041

if __name__ == '__main__':
  print(easy())
  print(hard())
