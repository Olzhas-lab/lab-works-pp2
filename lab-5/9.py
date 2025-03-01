import re
txt = input("Enter the word: ")
a = re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)
print(a)