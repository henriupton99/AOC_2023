import argparse
from collections import defaultdict

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    
    self.path, self.dirs = [], defaultdict(int)
    for line in self.lines:
      line = line.split()
      if line[0] == '$':
        if line[1] == 'cd':
          if line[2] == '..':
            self.path.pop()
          else:
            self.path.append(line[2])
      elif line[0] != 'dir':
        for i in range(len(self.path)):
          self.dirs[tuple(self.path[:i+1])] += int(line[0])
    
  def part1(self):
    return sum(size for size in self.dirs.values() if size <= 100000)
  
  def part2(self):
    required = 30000000 - (70000000 - self.dirs[("/",)])
    return min(size for size in self.dirs.values() if size >= required)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
