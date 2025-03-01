import re
txt = ["abc", "abb", "bbb", "ccc", "aaa", "abbbb", "abbb"]
pattern = r"^a(bb|bbb)$"
for i in txt: 
    a = re.fullmatch(pattern, i)
    if a: 
        print("The word that finish with two or threee b: ", i)