import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = [list(map(int,line.split())) for line in self.file.splitlines()]
  
  @staticmethod
  def is_safe(line: list) -> bool:
    if line == sorted(line) or line == sorted(line, reverse=True):
        if all(1<=abs(line[k]-line[k+1])<=3 for k in range(len(line)-1)):
          return True
    return False
    
  def part1(self):
    safe_lines = 0
    for line in self.lines:
        if self.is_safe(line):
            safe_lines += 1
    return safe_lines
  
  def part2(self):
    safe_lines = 0
    for line in self.lines:
       for k in range(len(line)):
          subline = line.copy()
          subline.pop(k)
          if self.is_safe(subline):
             safe_lines +=1
             break
    return safe_lines

if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
