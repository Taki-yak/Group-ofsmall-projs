# import re

# try :
#     email=input("Enter Your email:")
#     rule=re.search(r"[A-z0-9\.]+@[A-z0-9\.][com|net|fr]",email)
#     if rule:
#      user_name=email[:email.index("@")]
#      address=email[email.index("@")+1:]
#      print(user_name)
#      print(address)
# except  :
#     print(f"there is an error  ")
# print(email.split("@")[0])
# print(email.split("@")[1])
# #takiyalhlef49@gmail.com
import re

try:
    email=input("Email:")
    rule=re.search(r"[A-z0-9\.]+@[\w0-9\.][com|net|fr]",email)
    if rule:
      username=email[:email.index("@")]
      address=email[email.index("@")+1:]
      print(username)
      print(address)
except:
    print("Invalid email")