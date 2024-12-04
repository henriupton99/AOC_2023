import re
with open("input.txt") as file:
    cards_points = 0
    for i, line in enumerate(file.readlines()):
        line = line.split(":")[1]
        numbers = line.split("|")
        winning_numbers = re.findall("[0-9]+", numbers[0])
        card_numbers = re.findall("[0-9]+", numbers[1])
        matches = [number for number in card_numbers if number in winning_numbers]
        if len(matches)>0:
            cards_points += 2**(len(matches)-1)

print(cards_points)
        