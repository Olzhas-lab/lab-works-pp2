import re
txt = input("Enter the word: ")
pattern = r"^[a-z]+(_[a-z]+)*$"
a = re.fullmatch(pattern, txt)
if a: 
    print("Correct")
else: 
    print("Incorrect")
    