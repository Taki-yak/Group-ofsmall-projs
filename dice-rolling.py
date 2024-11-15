import random
import time 
def roll_dice(sides=6):
    """giving random dice number"""
    roll_result=random.randint(1,sides)
    return roll_result
print("welcome in game of dice rolling ")
rolls=int(input("how many times you want to roll the dice"))
print(f"rolling the dice {rolls}time(S)")
print("rolling . . .")
time.sleep(2)
results=[]
for i in range(rolls):
    roll_re=roll_dice()
    results.append(roll_re)
    
print(f"results:{results}")


