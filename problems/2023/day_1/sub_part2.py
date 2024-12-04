## PART TWO :

map_letters_to_number = {
    "one" : "1", 
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

sum_digits_lines = 0
with open("input.txt") as file:
    for line in file.readlines():
        line_numbers = []
        for i, string in enumerate(line):
            if string in map_letters_to_number.values():
                line_numbers.append(string)
            else:
                for digit_as_letter, digit_as_number in map_letters_to_number.items():
                    if digit_as_letter.startswith(string):
                        if line[i:i+len(digit_as_letter)] == digit_as_letter:
                            line_numbers.append(digit_as_number)
        first_digit = line_numbers[0]
        last_digit = line_numbers[-1]
        sum_digits_lines += int(f"{first_digit}{last_digit}")

print(sum_digits_lines)