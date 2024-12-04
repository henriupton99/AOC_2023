import re

with open("input.txt","r") as file:
    number_of_cards_per_id = [1 for _ in range(len(file.readlines()))]

with open("input.txt","r") as file:
    for i, line in enumerate(file.readlines()):
        line = line.split(":")[1]
        numbers = line.split("|")
        winning_numbers = re.findall("[0-9]+", numbers[0])
        card_numbers = re.findall("[0-9]+", numbers[1])
        matches = [number for number in card_numbers if number in winning_numbers]
        
        number_of_cards = number_of_cards_per_id[i]
        
        for _ in range(number_of_cards):
            for p in range(len(matches)):
                if i+p+1 < len(number_of_cards_per_id):
                    number_of_cards_per_id[i+p+1] += 1
        

print(sum(number_of_cards_per_id))
        