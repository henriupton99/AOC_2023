import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False, part=1):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    self.rope = [0] * 10
    self.visited = [set([x]) for x in self.rope]
    self.directions = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
    self.sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))
    self.rope_length = 1 if part == 1 else 10

    for line in self.lines:
      direction, steps = line.split(' ')
      for _ in range(int(steps)):
        self.rope[0] += self.directions[direction]

        for n in range(1, self.rope_length):
            dist = self.rope[n-1] - self.rope[n]
            if abs(dist) >= 2:
                self.rope[n] += self.sign(dist)
                self.visited[n].add(self.rope[n])
        
  def part1(self):
    return len(self.visited[-1])
  
  def part2(self):
    return len(self.visited[-1])
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test, part=args.part)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
