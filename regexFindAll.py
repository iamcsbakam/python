import re

text  = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern,text)
if search:
    print (search.group() ,"pattern found" )
else:
    print (search.group() ,"pattern not found" )