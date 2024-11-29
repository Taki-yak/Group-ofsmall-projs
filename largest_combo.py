"""largest combination bitwise and greater than zero"""
class solution ():
    def large(self,x):
        """responsibble of ordersing the numbers"""
        self.x=x
        res_temp=[]
        for i in range (len(x)):
            for j in range(i+1,len(x)):
                if x[i]<x[j]:
                    x[i], x[j] = x[j], x[i] 
    
        return x
                
        
number=list(input(" Number:"))
result=solution()
print(f"The Normal ordered number :{result.large(number)}")