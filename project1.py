
import os
# assignment :- list all the files in list of folders that’s user provides and find maximum size

# Read iput from user
# for loop , folder - list files
# identify module
# print file
# handle any known erros



def main():
 folders = input("please provide list of folder names").split()
for folder in folders:
  try:
    files = os.listdir(folder)
  except FileNotFoundError:
   print(" Please provide a valid folder name")  
   break
  except PermissionError:
    print(" No access to this folder ")  
    break
  
  print(" list files in the folder ")  
  for file in files:
    print(file)




