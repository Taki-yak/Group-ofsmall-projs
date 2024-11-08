class solution (object):
    def ispolindrome (self,x):
        str(self.x)=x
      
        if x[::-1]==x:
            return True
        else:
            return False
x=input("give number to test if polindrome : ")
result=solution()
if (result.ispolindrome(x)==True):
     print("number is polindrome")
else:
     print("number is not polindrome")