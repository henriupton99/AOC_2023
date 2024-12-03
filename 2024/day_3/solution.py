import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input_part_1 = 'test_input_part_1.txt'
  filename_test_input_part_2 = 'test_input_part_2.txt'
  
  def __init__(self, test=False, part=1):
    if test:
      if part == 1:
        self.filename = self.filename_test_input_part_1
      else:
        self.filename = self.filename_test_input_part_2
    else:
      self.filename = self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.line = ''.join(self.file.splitlines())
    
    self.regex_mul = re.compile(r"mul\([0-9]+,[0-9]+\)")
    self.regex_instruction = re.compile(r"do\(\)|don't\(\)")
    
    self.score = 0
  
  def increase_score(self, matches: list) -> None:
    for match in matches:
        l,r = list(map(int, re.findall(r"[0-9]+",match)))
        self.score += l*r
    
  def part1(self):
    matches = self.regex_mul.findall(self.line)
    self.increase_score(matches)
    return self.score
  
  def part2(self):
    line = "do()" + self.line + "don't()"
    instructions = list(self.regex_instruction.finditer(line))
    for i in range(len(instructions)-1):
      if instructions[i].group() == "don't()":
        continue
      scope = line[instructions[i].end():instructions[i+1].start()]
      matches = self.regex_mul.findall(scope)
      self.increase_score(matches)
    return self.score
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  part = args.part
  solution = Solution(test=test, part=part)
  result = solution.part1() if part == 1 else solution.part2()
  print(f'Result for Part=={part} & Test=={test} : {result}')
