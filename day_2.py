def get_inp():
  with open('input/day_2.txt') as f:
    arr = list(map(int, f.read().split(',')))
    return {i: n for i, n in enumerate(arr)}

def prn(state):
  for _, v in sorted(state.items()):
    print(v, end=',')
  print()

def easy(noun=12, verb=2):
  state = get_inp()
  state[1] = noun
  state[2] = verb

  idx = 0
  while state[idx] != 99:
    # print(idx)
    # prn(state)
    a, b, c = (state[idx+i] for i in range(1, 4))
    if state[idx] == 1:
      state[c] = state[a] + state[b]
    elif state[idx] == 2:
      state[c] = state[a] * state[b]
    else:
      assert False, 'Command is not 1 or 2'
    idx += 4
  return state[0]

def hard():
  for noun in range(100):
    for verb in range(100):
      if easy(noun, verb) == 19690720:
        return 100*noun + verb

print(easy())
print(hard())
