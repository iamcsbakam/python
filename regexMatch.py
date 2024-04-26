import re

text = "The quick brown fox"
pattern = r"quick"
pattern1 = r"The"

match = re.match(pattern1,text);
if match:
    print("match found:-",match.group());
else:
    print("no match found");