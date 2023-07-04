#Conditional Statements, Logical Operators, Code Blocks and Scope
print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller-coaster")
else:
    print("Sorry, you have to grow taller before you can ride")
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#Code to check if any given year  is a leap year
year = int(input("Which year do you want to check? "))
if year % 4== 0:
    if year % 100 == 0:
        if year % 400== 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

#Pizza Order program
size = input("What size pizza do you want? S, M or L ?")
add_pepperoni = input("Do you want to add pepperoni? Y or N? ")
add_extra_cheese = input("Do you want to add extra cheese? Y or N? ")
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price +=3
if add_extra_cheese == "Y":
    price += 1
print(f"Your final bill is ${price}")

#Treasure Land Game
print("Welcome to Treasure Land Game!\nYour mission is to find the treasure!")
path = input("Choose a path between left and right. Type 'left' or 'right' to choose a path \n").lower()
if path == "left":
    main_choice = input("You are at a lake. There is an island at the middle of the lake.\nType 'swim' to swim across or type 'wait' to wait for a boat \n").lower()
    if main_choice == "wait":
        choice2 = input("The boat has arrived and it has three doors colored red, blue and yellow.\nType 'red' to enter through the red door or 'blue' to enter through the blue door \nor type 'yellow' to go through the yellow door  \n").lower()
        if choice2 == "red":
            print("Oops! Game over")
        
        elif choice2 == "blue":
            print("Oops! Wrong choice. Game over")
        else:
            print("Congratulations! You found the treasure")
    else:
        print("Oops, Game Over! The lake is too vast. You'll die if you choose to swim across")
else:
    print("Game over! You fell into a hole")