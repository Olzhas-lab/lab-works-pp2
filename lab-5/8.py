import re 
txt = input("Enter the word: ")
a = re.split(r'(?=[A-Z])', txt)
print(a)