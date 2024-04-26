import requests
#/repos/{owner}/{repo}/pulls
#https://api.github.com/repos/kubernetes/kubernetes/pulls
#https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls


response  = requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")
print("*********")
complete_details = response.json()

#print(complete_details[0]["id"])


for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])