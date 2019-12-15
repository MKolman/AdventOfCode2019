from collections import defaultdict
class Runner(object):
  def __init__(self, state, stdin=None):
    if isinstance(state, Runner):
      self.state = defaultdict(int, state.state.items())
      self.stdin = state.stdin[:]
      self.idx = state.idx
      self.relative_base = state.relative_base
    else:
      self.state = defaultdict(int, enumerate(state))
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

  def op_sum(self):  # CMD 1
    self.set(3, self.get(1) + self.get(2))
    self.idx += 4

  def op_mul(self):  # CMD 2
    self.set(3, self.get(1) * self.get(2))
    self.idx += 4

  def op_inp(self):  # CMD 3
    assert self.stdin, "I ran out of STDIN while reading at {}".format(self.idx)
    self.set(1, self.stdin[0])
    self.stdin = self.stdin[1:]
    self.idx += 2

  def op_prn(self):  # CMD 4
    result = self.get(1)
    self.idx += 2
    return result

  def op_jit(self):  # CMD 5
    if self.get(1) != 0:
      self.idx = self.get(2)
    else:
      self.idx += 3

  def op_jif(self):  # CMD 6
    if self.get(1) == 0:
      self.idx = self.get(2)
    else:
      self.idx += 3

  def op_les(self):  # CMD 7
    self.set(3, int(self.get(1) < self.get(2)))
    self.idx += 4

  def op_eql(self):  # CMD 8
    self.set(3, int(self.get(1) == self.get(2)))
    self.idx += 4

  def op_chb(self):  # CMD 9
    self.relative_base += self.get(1)
    self.idx += 2

  def op_hlt(self):  # CMD 99
    raise StopIteration

  def __iter__(self):
    return self

  def __next__(self):
    ops = [self.op_sum, self.op_mul, self.op_inp, self.op_prn, self.op_jit, self.op_jif, self.op_les, self.op_eql, self.op_chb]
    while True:
      op = self.state[self.idx] % 100
      assert 1 <= op <= 9 or op == 99, 'Command {} is not valid on position {} when parsing {}'.format(op, self.idx, self.state[self.idx])
      if op == 3 and len(self.stdin) == 0:
        return None
      f = self.op_hlt if op == 99 else ops[op-1]
      if op == 4:
        return f()
      f()
