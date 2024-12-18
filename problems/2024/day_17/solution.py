import argparse
import re

def get_combo(operand, a, b, c):
    if 0 <= operand <= 3:
      return operand
    elif operand == 4:
      return a
    elif operand == 5:
      return b
    elif operand == 6:
      return c
    return None 

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.registers_content, self.program_content = self.file.split("\n\n")
    self.program = self.get_nums(self.program_content)
    self.registers = {}
    for line in self.registers_content.split('\n'):
      register_name = line.replace('Register ','')[0]
      self.registers[register_name] = self.get_nums(line)[0]    
  
  @staticmethod
  def run(program, a, b, c):
    output = []
    ip = 0
    while ip < len(program):
      opcode, operand = program[ip], program[ip+1]
      combo = get_combo(operand, a, b, c)
      ip += 2
      if opcode == 0:
        a = a // (2**combo)
      elif opcode == 1:
        b ^= operand
      elif opcode == 2:
        b = combo % 8
      elif opcode == 3:
        if a != 0:
          ip = operand
      elif opcode == 4:
        b = b ^ c
      elif opcode == 5:
        output.append(combo % 8)
      elif opcode == 6:
        b = a // (2**combo)
      elif opcode == 7:
        c = a // (2**combo) 
    return output
  
  def get_best_input(self, program, cursor, sofar):
    for candidate in range(8):
      if self.run(program, sofar * 8 + candidate, 0, 0) == program[cursor:]:
        if cursor == 0:
            return sofar * 8 + candidate
        ret = self.get_best_input(program, cursor - 1, sofar * 8 + candidate)
        if ret is not None:
            return ret
    return None
    
  def part1(self):
    output = self.run(program=self.program, a=self.registers['A'], b=self.registers['B'], c=self.registers['C'])
    output = list(map(str, output))
    return ",".join(output)
  
  def part2(self):
    return self.get_best_input(self.program, len(self.program)-1, 0)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
