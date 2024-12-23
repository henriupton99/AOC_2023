import argparse
import re
import networkx as nx

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = [line.split('-') for line in self.file.splitlines()]
    self.graph = nx.Graph()
    self.graph.add_edges_from(self.lines)
    
  def part1(self):        
    triangles = [list(triangle) for triangle in nx.enumerate_all_cliques(self.graph) if len(triangle) == 3]
    triangles_with_t = [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]
    return len(triangles_with_t)
  
  def part2(self):
    longest = max(nx.find_cliques(self.graph), key=len)
    return ','.join(sorted(longest))
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
