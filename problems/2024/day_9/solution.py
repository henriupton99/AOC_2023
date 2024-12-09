import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def generate_sequence(disk_map: list[int]) -> list[int]:
    file_id = 0
    sequence = []
    for i in range(0, len(disk_map)-1, 2):
      file_size, space_size = disk_map[i:i+2]
      sequence += [file_id for _ in range(file_size)]
      sequence += [None for _ in range(space_size)]
      file_id += 1
    sequence += [file_id for _ in range(disk_map[-1])]
    return sequence 
  
  @staticmethod
  def compute_result(sequence: list[int]):
    result = 0
    for i, value in enumerate(sequence):
      if value is not None:
        result += i * value
    return result
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.disk_map = list(map(int, self.file.splitlines()[0]))
    self.sequence = self.generate_sequence(self.disk_map)
    
  def part1(self):
    while None in self.sequence:
      for i, e in enumerate(self.sequence):
        if e is None:
          last_item = self.sequence.pop()
          self.sequence[i] = last_item
          while self.sequence[-1] is None:
            self.sequence.pop()
    return self.compute_result(self.sequence)
  
  def part2(self):
    for id in reversed(range(1,self.sequence[-1]+1)):
      id_indexes = [i for i,e in enumerate(self.sequence) if e == id]
      for i in range(id_indexes[0]):
        if all(e is None for e in self.sequence[i:i+len(id_indexes)]):
          for k in id_indexes:
            self.sequence[k] = None
          self.sequence[i:i+len(id_indexes)] = [id for _ in range(len(id_indexes))]
          break
    return self.compute_result(self.sequence)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
