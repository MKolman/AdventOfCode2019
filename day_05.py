def get_inp():
  with open('input/day_05.txt') as f:
    arr = list(map(int, f.read().split(',')))
    return {i: n for i, n in enumerate(arr)}


def run(machineid=1):
  state = get_inp()
  result = 0
  idx = 0
  while state[idx] % 100 != 99:
    params = [state[idx+i] for i in range(1, 4)]
    is_value = ((state[idx]//10**i)%10 for i in range(2, 5))
    a, b, c = [x if val or x not in state else state[x] for x, val in zip(params, is_value)]
    op = state[idx] % 100
    assert 1 <= op <= 8, 'Command {} is not valid on position {} when parsing {}'.format(op, idx, state[idx])
    if op == 1:
      state[params[2]] = a + b
      idx += 4
    elif op == 2:
      state[params[2]] = a * b
      idx += 4
    elif op == 3:
      state[params[0]] = machineid
      idx += 2
    elif op == 4:
      result = a
      idx += 2
    elif op == 5:
      if a != 0:
        idx = b
      else:
        idx += 3
    elif op == 6:
      if a == 0:
        idx = b
      else:
        idx += 3
    elif op == 7:
      state[params[2]] = int(a < b)
      idx += 4
    elif op == 8:
      state[params[2]] = int(a == b)
      idx += 4
  return result

print(run(1))
print(run(5))
