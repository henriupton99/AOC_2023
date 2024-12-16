import argparse
import re
import heapq

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.grid = [list(line) for line in self.file.splitlines()]
    self.nrows, self.ncols = len(self.grid), len(self.grid[0])
    
    for i in range(self.nrows):
      for j in range(self.ncols):
        if self.grid[i][j] == 'S':
          self.start = tuple((i,j))
        elif self.grid[i][j] == 'E':
          self.end = tuple((i,j))

  @staticmethod
  def dijkstra(grid, starts):
    delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    dist = {}
    pq = []
    for sr, sc, dir in starts:
        dist[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))
    while pq:
        (d, row, col, direction) = heapq.heappop(pq)
        if dist[(row, col, direction)] < d:
            continue
        for next_dir in "EWNS".replace(direction, ""):
            if (row, col, next_dir) not in dist or dist[
                (row, col, next_dir)
            ] > d + 1000:
                dist[(row, col, next_dir)] = d + 1000
                heapq.heappush(pq, (d + 1000, row, col, next_dir))
        dr, dc = delta[direction]
        next_row, next_col = row + dr, col + dc
        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] != "#"
            and (
                (next_row, next_col, direction) not in dist
                or dist[(next_row, next_col, direction)] > d + 1
            )
        ):
            dist[(next_row, next_col, direction)] = d + 1
            heapq.heappush(pq, (d + 1, next_row, next_col, direction))
    return dist

  def part1(self):
    dist = self.dijkstra(self.grid, [(self.start[0], self.start[1], "E")])
    best = float('Inf')
    for dir in "EWNS":
        if (self.end[0], self.end[1], dir) in dist:
            best = min(best, dist[(self.end[0], self.end[1], dir)])
    return best
  
  def part2(self):
    from_start = self.dijkstra(self.grid, [(self.start[0], self.start[1], "E")])
    from_end = self.dijkstra(self.grid, [(self.end[0], self.end[1], d) for d in "EWNS"])
    optimal = self.part1()
    flip = {"E": "W", "W": "E", "N": "S", "S": "N"}
    result = set()
    for row in range(len(self.grid)):
        for col in range(len(self.grid[0])):
            for dir in "EWNS":
                state_from_start = (row, col, dir)
                state_from_end = (row, col, flip[dir])
                if state_from_start in from_start and state_from_end in from_end:
                    if (
                        from_start[state_from_start] + from_end[state_from_end]
                        == optimal
                    ):
                        result.add((row, col))
    return len(result)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
