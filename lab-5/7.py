import re 
txt = input("Enter the snake case string: ")
result = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), txt) 
result = result.capitalize() 
print(result)