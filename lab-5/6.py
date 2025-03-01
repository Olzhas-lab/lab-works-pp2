import re 
txt = input("Enter the string: ")
a = re.sub(r"[ , .]", ":", txt)
print(a)