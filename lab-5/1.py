import re
txt = ["abc", "ab", "abb", "bb", "bca", "b", "ba", "abbbbbbb", "a", "aaa"]
pattern = r"^ab*"
for i in txt: 
    a = re.fullmatch(pattern, i)
    if a: 
        print(f'"{i}" true')
    else:
        print(f'"{i}" falsew')