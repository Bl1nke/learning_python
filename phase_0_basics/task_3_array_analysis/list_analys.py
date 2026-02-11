numbers = [12, 5, -3, 8, 0, 15, -7, 9, 4, -1]
sum_positive = 0
lot_negative = 0
even_numbers = []
max = numbers[0]
min = numbers[0]

for num in numbers:
    if num > 0:
        sum_positive += num
    if num < 0:
        lot_negative += 1
    if num % 2 == 0:
        even_numbers.append(num)

for num in numbers[1:]:
    if num > max:
        max = num
    elif num < min:
        min = num

print(f"Summury of positive {sum_positive}; Lot of negative {lot_negative}; Even numbers {even_numbers}")
print(f"Maximum: {max}; Minimum {min}")