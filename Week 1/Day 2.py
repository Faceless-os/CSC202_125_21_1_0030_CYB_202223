#2
print("Hello"[0])

#Integer
print(123 + 345)

#Float
123.146

#Boolean
True
False

#4
num_char = len(input("What is your name"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

#5
two_digit_number = input("type a two digit number")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print("The sum of the two digitd is")
print(result)
 
#6 Mathemathical Operations
3 + 5
7 - 4
3 * 2
2 ** 2

#PEMDAS
#Parenthesis ()
#Exponents **
#Multiplications *
#Division / 
#Addition +
#Subtraction -

#7
#weight calculator
height = input("enter your height in m:" )
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#8
print(8 / 3)
#removing all numbers after the decimal place
print(int(8 / 3))
#rounding off the answer
print(round(8 / 3))
#rounding to 3 decimal places
print(round(2.6666669342, 3))
#getting integers only
print(8 // 3)
#other operations
result = 4 / 2
result /= 2
print(result)
#f-string
score = 2
height = 2.87
isLosing = True
print(f"your score is {score}, your height is {height}, you are losing is {isLosing}")
#9
