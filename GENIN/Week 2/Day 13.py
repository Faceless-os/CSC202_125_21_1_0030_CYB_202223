    #Take I/O
year = int(input("What's your year of birth?\n"))
if year > 1980 and year < 1994:
    print("You are a Millenial.")
elif year >= 1994:
    print ("You are a Gen Z.")
age = int(input("How old are you?\n"))
if age > 18:
    print(f"You can drive at age {age}.")
elif age < 18:
    print(f"You are underage, You can't drive at age {age}")

pages = 0
word_per_page = 0
pages = int(input("Number of words per paage:\n"))
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)


