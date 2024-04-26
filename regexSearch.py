import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"fox"

searchedText = re.search(pattern,text);

if searchedText:
    print(pattern + " : " + "is present"+ searchedText.group());
else:
    print(pattern + " : " + "Not present");

