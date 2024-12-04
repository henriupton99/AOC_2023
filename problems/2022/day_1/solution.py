import argparse

class Solution:
  filename_input = 'input.txt'
  filename_test = 'test.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test,'r').read() if test else open(self.filename_input,'r').read()
    self.lines = self.file.splitlines()
    
    self.counts = {0 : 0}
    index = 0
    for line in self.lines:
      if len(line) == 0:
        index += 1
        self.counts[index] = 0
        continue
      self.counts[index] += int(line)
    
  def part1(self):
    return max(self.counts.values())
  
  def part2(self):
    values = list(self.counts.values())
    values.sort()
    return sum(values[-3:])
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
