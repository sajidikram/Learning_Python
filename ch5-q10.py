import random
comp_guess=random.randint(1,10)
print(comp_guess)
user_guess=0
while user_guess!=comp_guess:
    user_guess=int(input("Guess a number bw 1 to 10 :"))
print("You are right")