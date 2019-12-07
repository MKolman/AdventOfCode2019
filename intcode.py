class Runner(object):
  def __init__(self, state, stdin=None):
    self.state = state
    self.stdin = stdin or []
    self.idx = 0

  def get(self, n):
    get_value = (self.state[self.idx] // 10**(n+1)) % 10
    value = self.state[self.idx + n]
    return value if get_value else self.state[value]

  def set(self, n, value):
    self.state[self.state[self.idx+n]] = value

  def __iter__(self):
    return self

  def __next__(self):
    while True:
      op = self.state[self.idx] % 100
      assert 1 <= op <= 8 or op == 99, 'Command {} is not valid on position {} when parsing {}'.format(op, self.idx, self.state[self.idx])
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
      elif op == 99:
        raise StopIteration
