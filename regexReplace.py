import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"
replace = "RED"
new_text = re.sub(pattern,replace,text);

print(new_text);
