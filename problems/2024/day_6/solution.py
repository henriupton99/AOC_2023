import argparse
from tqdm import tqdm

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def move_in_matrix(matrix, start_position, orientation, directions, tilt_right, obstruction):
    
    # if obstruction mode, generate obstacle in given coordinates 
    if obstruction is not None:
       i,j = obstruction
       matrix[i][j] = '#'
    
    nrows, ncols = len(matrix), len(matrix[0])
    current_position = start_position
    current_orientation = orientation
    delta = directions[current_orientation]
    history = [current_position+delta]
    is_obstruction = False # dummy indicator to save obstructions

    while True:
        # compute next position
        next_position = tuple(map(sum, zip(current_position, delta)))
        i, j = next_position
        # out of bound terminal condition
        if i < 0 or i >= nrows or j < 0 or j >= ncols:
            break
        # handling of obstacles
        if matrix[i][j] == '#':
          current_orientation = tilt_right[current_orientation]
          delta = directions[current_orientation]
          continue
        # move forward
        current_position = next_position
        # position and direction was already observed, we are stuck in a loop = obstruction
        if current_position + delta in history:
          is_obstruction = True
          break
        # save position and direction in the history
        history.append(current_position + delta)
    
    # if obstruction mode, remove obstruction to recover original matrix
    if obstruction is not None:
       i,j = obstruction
       matrix[i][j] = '.'

    return history, is_obstruction
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.matrix = [list(line) for line in self.file.splitlines()]
    self.nrows, self.ncols = len(self.matrix), len(self.matrix[0])
    self.tilt_right = {'^':'>', '>': 'v', 'v':'<', '<':'^'}
    self.directions = {'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}
    self.starting_position = [tuple((i,j)) for i in range(self.nrows) for j in range(self.ncols) if self.matrix[i][j] in self.tilt_right][0]

    self.visited = []
    self.visited.append(self.starting_position)
    self.current_position = self.starting_position
    self.current_orientation = '^'
    self.current_direction = self.directions[self.current_orientation]
      
  def part1(self):
    history, _ = self.move_in_matrix(self.matrix,self.current_position,self.current_orientation,self.directions,self.tilt_right,None)
    visited = [tuple((i,j)) for (i,j,_,_) in history]
    return len(set(visited))
  
  def part2(self):
    results = []
    history, _ = self.move_in_matrix(self.matrix,self.current_position,self.current_orientation,self.directions,self.tilt_right,None)
    visited = [tuple((i,j)) for (i,j,_,_) in history]
    # test all possible coordinates where to put a potential obstruction
    for (i,j) in tqdm(set(visited)):
      _, is_obstruction = self.move_in_matrix(self.matrix, self.starting_position, self.current_orientation, self.directions, self.tilt_right, (i,j))
      results.append(is_obstruction)
    return sum(results)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
