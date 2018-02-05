hidden_answer=10
user_guess=int(input("Guess the hidden answer :"))
if (user_guess == hidden_answer):
 print("Your guess is exactly right")
elif (user_guess > hidden_answer):
 print("Your guess is too high")
else :
 print("Your guess is too low")