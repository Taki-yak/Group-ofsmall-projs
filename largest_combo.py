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
# class Solution:
#     def large(self, x):
#         """Responsible for ordering the numbers in descending order."""
#         res_temp = []
        
#         # Convert the input to a list of individual digits
#         for digit in x:
#             res_temp.append(digit)
            
#         # Sort the list in descending order
#         for i in range(len(res_temp)):
#             for j in range(i + 1, len(res_temp)):
#                 if res_temp[i] < res_temp[j]:
#                     res_temp[i], res_temp[j] = res_temp[j], res_temp[i]  # Swap
        
#         return ''.join(res_temp)  # Join the sorted list into a string

# number = input("Number: ")
# result = Solution()
# print(f"The Normal ordered number: {result.large(number)}")