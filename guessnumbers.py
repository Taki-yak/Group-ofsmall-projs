import random
print("Welcome to gussin the number , if u guess right u win ")
def generate_number (ran):
    guess=random.randint(0,ran)
    return guess
range=int(input("what the range of numbers u want to guess from , make it smaller u little genius boy :) = "))
i_guess=int(input("so whats ur guessing :"))
number=generate_number(range)
 
while i_guess!=number:
 try : 
   if i_guess<number:
     i_guess=int(input("too low , try again :"))
   elif i_guess>number:
     i_guess=int(input("too high , try again :"))
   else:
      print(f"oh hell nah u guess it right its {i_guess}")
 except:
    i_guess=int(input("please enter a valid number"))
if number == i_guess:
    print(f"oh hell nah u guess it right its {i_guess}")

