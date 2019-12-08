def test():
  for d in range(1, 26):
    result = 'Day {:02d} '.format(d)
    try:
      solution = __import__('day_{:02d}'.format(d))
      e, h = solution.test()
      result += '{} {}'.format(' ✓'[e], ' ✓'[h])
    except ModuleNotFoundError:
      result += '✗ ✗'
    print('{}'.format(result))

if __name__ == '__main__':
  test()