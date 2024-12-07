import argparse
import re
from itertools import product

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    self.final_score = 0

  @staticmethod
  def add(a: int, b: int) -> int:
    return a+b
  
  @staticmethod
  def multiply(a: int, b: int) -> int:
    return a*b

  @staticmethod
  def concatenate(a: int, b: int) -> int:
    return int(f"{a}{b}")

  @staticmethod
  def compute_equation(line: str, operations: list[callable]) -> bool:
    nums = list(map(int, re.findall(r"\d+",line)))
    target, nums = nums[0], nums[1:]
    for combination in list(product(operations, repeat=len(nums)-1)):
      for i, operation in enumerate(combination):
        if i == 0:
          score = operation(nums[i], nums[i+1])
        else:
          score = operation(score, nums[i+1])
      if score == target:
        return target
    return 0
    
  def part1(self):
    for line in self.lines:
      self.final_score += self.compute_equation(line, operations=[self.add, self.multiply])
    return self.final_score

  def part2(self):
    for line in self.lines:
      self.final_score += self.compute_equation(line, operations=[self.add, self.multiply, self.concatenate])
    return self.final_score
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
