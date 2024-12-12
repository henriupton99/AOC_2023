import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'

  def dfs(self, node, color, dir):
      if self.graph[node] != color:
          if self.graph[node + dir * 1j] == color or self.graph[node - dir + dir * 1j] != color:
              return 0, 1, 1
          else:
              return 0, 1, 0
      if node in self.visited:
          return 0, 0, 0
      self.visited.add(node)
      area, perimeter, sides = 1, 0, 0
      for d in (1, -1, 1j, -1j):
          a, p, s = self.dfs(node + d, color, d)
          area, perimeter, sides = area + a, perimeter + p, sides + s
      return area, perimeter, sides
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    self.nrows, self.ncols = len(self.lines), len(self.lines[0])
    self.graph = {i + j * 1j: c for i, r in enumerate(self.lines) for j, c in enumerate(r)}

    for i in range(-1, self.nrows + 1):
        self.graph[i - 1 * 1j] = self.graph[i + self.ncols * 1j] = "#"
    for j in range(-1, self.ncols + 1):
        self.graph[-1 + j * 1j] = self.graph[self.nrows + j * 1j] = "#"
    self.visited = set()
    self.result = 0
    
  def part1(self):
    for node in self.graph:
        if node not in self.visited and self.graph[node] != "#":
            area, perimeter, sides = self.dfs(node, self.graph[node], 1)
            self.result += area * perimeter
    return self.result
  
  def part2(self):
    for node in self.graph:
        if node not in self.visited and self.graph[node] != "#":
            area, perimeter, sides = self.dfs(node, self.graph[node], 1)
            self.result += area * sides
    return self.result
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
