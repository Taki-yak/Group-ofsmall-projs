class solution ():
 def reverse(self,number):
     self.number=number
     res=number[::-1] 
     return  int (res)
number=str(input("give number then we give the inverse :"))
result= solution()
print(f"the reversed number of {number } is : {result.reverse(number)} ")
     