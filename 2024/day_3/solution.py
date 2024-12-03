import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.line = ''.join(self.file.splitlines())
    self.regex_mul = re.compile(r"mul\([0-9]+,[0-9]+\)")
    self.regex_instruction = re.compile(r"do\(\)|don't\(\)")
    
  def part1(self):
    score = 0
    matches = self.regex_mul.findall(self.line)
    for match in matches:
      l,r = list(map(int, re.findall(r"[0-9]+",match)))
      score += l*r
    return score
  
  def part2(self):
    score = 0
    line = "do()" + self.line + "don't()"
    instructions = list(self.regex_instruction.finditer(line))
    for i in range(len(instructions)-1):
      if instructions[i].group() == "don't()":
        continue
      scope = line[instructions[i].end():instructions[i+1].start()]
      matches = self.regex_mul.findall(scope)
      for match in matches:
        l,r = list(map(int, re.findall(r"[0-9]+",match)))
        score += l*r
    return score
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
