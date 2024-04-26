import re

text ="apple,banana,orange,grape"
pattern= r","

split_result = re.split(pattern,text)
print("Split result:", split_result)
print("print orange from Split result:", split_result[2])



