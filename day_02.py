def get_inp():
  with open('input/day_02.txt') as f:
    arr = list(map(int, f.read().split(',')))
    return {i: n for i, n in enumerate(arr)}


def easy(noun=12, verb=2):
  state = get_inp()
  state[1] = noun
  state[2] = verb

  idx = 0
  while state[idx] != 99:
    a, b, c = (state[idx+i] for i in range(1, 4))
    if state[idx] == 1:
      state[c] = state[a] + state[b]
    elif state[idx] == 2:
      state[c] = state[a] * state[b]
    else:
      assert False, 'Command is not 1 or 2'
    idx += 4
  return state[0]

def easy2(noun=12, verb=2):
  return noun*405000 + verb + 250673

def test_easy():
  for n in range(100):
    for v in range(100):
      assert easy(n, v) == easy2(n, v), (n, v, easy(n, v), easy2(n, v))

def hard():
  for noun in range(100):
    for verb in range(100):
      if easy(noun, verb) == 19690720:
        return 100*noun + verb

def hard2():
  r = 19690720 - 250673
  verb = r % 405000
  noun = r // 405000
  return 100*noun + verb

def test_hard():
  assert hard() == hard2()

print(easy2())
print(hard2())
test_easy()
test_hard()
