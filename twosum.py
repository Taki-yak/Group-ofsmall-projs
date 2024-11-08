max = int(input("How many numbers do you want in your list: "))
my_list = []
print("Enter your numbers:")
for num in range(max):
    number = int(input(f"{num + 1}- "))
    print(f"Number {number} has been added to your list")
    my_list.append(number)
    print(f"Still {max - 1 - num} number(s) to add")

print("Your list:")
print(my_list)

result = int(input("What is the number you want to find the sum for? I'll give you the indices of the numbers that add up to it: "))
found = False

# Finding pairs
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] + my_list[j] == result:
            print(f"Indices {i} and {j} (Numbers: {my_list[i]} + {my_list[j]} = {result})")
            found = True

if not found:
    print("No pairs found that sum to the given number.")