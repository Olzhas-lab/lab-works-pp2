import re
txt = ["Almaty", "Regex", "Hello", "PrinT", "KYZYLORDA"]
pattern = r"^[A-Z][a-z]+$"
for i in txt: 
    a = re.findall(pattern, i)
    if a: 
        print("The word that starts with the uppercase letter and ends with lowercase: ", a)