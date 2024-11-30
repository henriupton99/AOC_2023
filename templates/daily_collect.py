import os, subprocess
import argparse
import shutil

from bs4 import BeautifulSoup
import requests

########### LOAD CONFIG ###########
session_cache_file = '.session_cache.lock'
if not os.path.exists(session_cache_file):
    session = input('Please give session cookies:')
    with open(session_cache_file,'w') as file:
        file.write(session)
    file.close()

session = open(session_cache_file).read()
if not isinstance(session, str):
    raise TypeError('Provided session cookie must be a string')
########### COLLECT ARGUMENTS ###########
try:
    parser = argparse.ArgumentParser(description='Collect input for Advent of Code')
    parser.add_argument('-d',type=str,required=True,help='Day to collect')
    parser.add_argument('-y',type=str,required=True,help='Year to collect')
    args = parser.parse_args()
except:
    raise KeyError('Missing entry for day (-d) or year (-y)')

########### CREATE DIRECTORY ###########
dest = os.path.join(args.y,f'day_{args.d}')
if os.path.isdir(dest):
    raise FileExistsError(f'Destination directory "{dest}" already exists')
os.makedirs(dest)

########### PARSE DAY PROBLEM ###########
url = 'https://adventofcode.com'
line_size = 120
day_url = f'{url}/{args.y}/day/{args.d}'
headers = {'User-Agent': 'https://github.com/henriupton99/AdventOfCode by henriupton99@gmail.com'}
response = requests.get(day_url, headers=headers)
soup = BeautifulSoup(response.text, features="html.parser")
instructions = soup.find('article',attrs={'class':'day-desc'})

########### COLLECT DAY DESCRIPTION ###########
day_desc_title = soup.select_one(".day-desc h2")
title_text = day_desc_title.get_text(strip=True) if day_desc_title else ""
day_desc_path = os.path.join(dest, 'day_desc.md')
with open(day_desc_path, "w", encoding='utf-8') as md_file:
    md_file.write(f"# {title_text}\n\n")
    for section in instructions:
        if section.name == "p":
            md_file.write(section.get_text(strip=True) + "\n\n")
        elif section.name == "pre":
            md_file.write("```shell\n")
            md_file.write(section.get_text(strip=True) + "\n")
            md_file.write("```\n")
    print(f"Content for test input saved at : {day_desc_path}")
    md_file.close()

########### COLLECT TEST INPUT ###########
test_input_path = os.path.join(dest, 'test_input.txt')
for i, section in enumerate(instructions):
    if section.name == 'p' and 'example' in section.text.lower():
        next_section = section.find_next_sibling()
        if next_section and next_section.name == "pre":
            pre_content = next_section.text.strip()
            with open(test_input_path, "w", encoding="utf-8") as file:
                file.write(pre_content)
                print(f"Content for test input saved at : {test_input_path}")
            break

########### COLLECT REAL INPUT ###########
real_input_path = os.path.join(dest, 'real_input.txt')
with open(real_input_path,"w") as file:
    output = subprocess.check_output(f'curl {day_url}/input --cookie "session={session}"', shell=True)
    output = output.decode('utf-8')
    file.write(output)
    print(f"Content for real input saved at : {real_input_path}")
    file.close()

########### CLONE SOLUTION TEMPLATE ###########
template_solution = os.path.join('templates','solution.py')
shutil.copyfile(template_solution, os.path.join(dest,'solution.py'))
