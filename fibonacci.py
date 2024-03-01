num1 = 0
num2 = 1
next_num = num2

terms = int(input("How many terms do you want to print?: "))

for i in range(terms):
    print(num1)
    num1 = num2
    num2 = next_num
    next_num = num1 + num2
