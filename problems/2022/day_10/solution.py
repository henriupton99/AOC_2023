import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
  
  @staticmethod
  def update_CRT(CRT, cycle, X):
    CRT += '#' if X-1 <= cycle % 40 <= X+1 else '.'
    return CRT
  
  def execute_program(self, program):
      X = 1
      cycle = 0
      target_cycles = [20, 60, 100, 140, 180, 220]
      signal_strength_sum = 0
      CRT = ''
      
      for instruction in program:
        if instruction == "noop":
          CRT = self.update_CRT(CRT, cycle, X)
          cycle += 1
          if cycle in target_cycles:
              signal_strength_sum += cycle * X
              
        elif instruction.startswith("addx"):
          value = int(instruction.split()[1])
          for _ in range(2):
            CRT = self.update_CRT(CRT, cycle, X)
            cycle += 1
            if cycle in target_cycles:
              signal_strength_sum += cycle * X
          X += value
      
      return signal_strength_sum, CRT
  
  def part1(self):
    return self.execute_program(self.lines)
  
  def part2(self):
    _, CRT = self.execute_program(self.lines)
    for k in range(6):
      print(f'{CRT[k*40:(k+1)*40]}')
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
