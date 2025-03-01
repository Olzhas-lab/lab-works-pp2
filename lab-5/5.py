import re
txt = input("Enter the word: ")
pattern = r"^a.*b$"
a = re.fullmatch(pattern, txt)
if a: 
    print("YES, this word correct. Word is: ", txt)
else: 
    print("NO, this word incorrect. Word is: ", txt)