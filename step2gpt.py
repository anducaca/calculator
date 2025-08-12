result1 = 0
result2 = 0
result3 = 0
result4 = 0
Total = 0

with open("numbers.txt", "r") as file:
    numbers = file.read().splitlines()
    for number in numbers:
        calc, operator, number1, number2 = number.split()
        number1 = int(number1)
        number2 = int(number2)

        if operator == "+":
            result1 += number1 + number2
            print("The result1 is:", result1)
        elif operator == "-":
            result2 += number1 - number2
            print("The result2 is:", result2)
        elif operator == "/":
            result3 += number1 / number2
            print("The result3 is:", result3)
        elif operator == "*":
            result4 += number1 * number2
            print("The result4 is:", result4)

Total = result1 + result2 + result3 + result4
print("The outerloop result is:", Total)
