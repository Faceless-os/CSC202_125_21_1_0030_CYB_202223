#Day 4 -Randomization and Python Lists
# #Day 4 -Randomization and Python Lists
#Randomization 
#Heads or Tails Exercise
import random
random.seed()
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_int = random.randint(0, 1)
if random_int == 1:
    print("Heads")
else:
    print("Tails")

# Who go Pay?
import random
random.seed()
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Drop una names, separated by a comma. ")
names = namesAsCSV.split(", ")
na_him_go_pay = random.choice(names)
print(na_him_go_pay, "go pay for wetin una chop")
