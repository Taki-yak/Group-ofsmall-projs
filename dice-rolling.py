import random,time
def roll_dice(sides):
  """resposible of giving random number for dice """
  rolling=random.randint(1,sides)
  return rolling

sides=int(input(("how many sides do u want in your dice:")))
rolls_number=int(input("how many time for rolling your dice:"))
results=[]
for i in range(rolls_number): 
    results.append(roll_dice(sides))
for i in range (len(results)):
    print(f" {i+1} roll={results[i]}")
print(dir(roll_dice))
print(roll_dice.__doc__)
help(roll_dice)


