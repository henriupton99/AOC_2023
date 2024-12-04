
## PART ONE : 
# Allows to get sum of all calibrations values :
digits=[str(k) for k in range(0,10)]
print(digits)

sum_digits_lines = 0
with open("input.txt") as file:
    for line in file.readlines():
        line_chars = [char for char in line]
        line_digits = [d for d in line_chars if d in digits]
        first_digit = line_digits[0]
        last_digit = line_digits[-1]
        line_number = int(f"{first_digit}{last_digit}")
        sum_digits_lines += line_number

print("Sum of all calibration values of instructions line : ", sum_digits_lines)

   
        