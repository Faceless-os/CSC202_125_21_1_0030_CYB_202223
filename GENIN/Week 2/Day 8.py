    #Paint Area Calculator
import math
test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 3
def paint_calc(height, width, cover):
        number_of_cans = (height * width) / cover
        print(f"You need {math.ceil(number_of_cans)} cans of paint to cover the wall")
paint_calc(height = test_h, width= test_w, cover = coverage)
    
    #Checking Prime Number
no = int(input("Check this number: "))
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")
prime_checker(number = no)

    #Caesar Cypher
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']         
direction= input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your mesage:\n").lower()
shift=int(input("Type the shift number:\n"))
def encrypt(plain_text, shift_amount):
    for letter in plain_text:
        position= alphabet.index(letter)
        new_position= position + shift_amount  
        new_letter=alphabet[new_position]
        cipher_text+= new_letter
        print(f"The encoded text is {cipher_text}")
        encrypt(plain_text=text, shift_amount = shift)
def decrypt(cipher_text, shift_amount):
  for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position-shift_amount
      plain_text += alphabet[new_position]     
      print(f"The decoded text is {plain_text}")   
if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":  
  decrypt(cipher_text = text, shift_amount = shift)    