class Runner(object):
  def __init__(self, state, stdin=None):
    self.state = dict(enumerate(state))
    self.stdin = stdin or []
    self.idx = 0
    self.relative_base = 0

  def get(self, n):
    mode = (self.state[self.idx] // 10**(n+1)) % 10
    assert mode in [0, 1, 2], mode
    value = self.state[self.idx + n]
    if mode == 0:
      return self.state[value]
    elif mode == 1:
      return value
    elif mode == 2:
      return self.state[value + self.relative_base]

  def set(self, n, value):
    mode = (self.state[self.idx] // 10**(n+1)) % 10
    assert mode in [0, 2], mode
    if mode == 0:
      self.state[self.state[self.idx+n]] = value
    else:
      self.state[self.state[self.idx+n] + self.relative_base] = value

  def __iter__(self):
    return self

  def __next__(self):
    while True:
      op = self.state[self.idx] % 100
      assert 1 <= op <= 9 or op == 99, 'Command {} is not valid on position {} when parsing {}'.format(op, self.idx, self.state[self.idx])
      if op == 1:
        self.set(3, self.get(1) + self.get(2))
        self.idx += 4
      elif op == 2:
        self.set(3, self.get(1) * self.get(2))
        self.idx += 4
      elif op == 3:
        assert self.stdin, "I ran out of STDIN while reading at {}".format(self.idx)
        self.set(1, self.stdin[0])
        self.stdin = self.stdin[1:]
        self.idx += 2
      elif op == 4:
        result = self.get(1)
        self.idx += 2
        return result
      elif op == 5:
        if self.get(1) != 0:
          self.idx = self.get(2)
        else:
          self.idx += 3
      elif op == 6:
        if self.get(1) == 0:
          self.idx = self.get(2)
        else:
          self.idx += 3
      elif op == 7:
        self.set(3, int(self.get(1) < self.get(2)))
        self.idx += 4
      elif op == 8:
        self.set(3, int(self.get(1) == self.get(2)))
        self.idx += 4
      elif op == 9:
        self.relative_base += self.get(1)
        self.idx += 2
      elif op == 99:
        raise StopIteration
