import subprocess
expected_output = {'1':41, '2':6}
day = '6'
year = '2024'

def test_solution():
  for part in ['1','2']:
    command = ['./submit', day, year, part, 'true']
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
    assert result.stdout == f'Result for Part=={part} & Test==True : {expected_output[part]}\n'
