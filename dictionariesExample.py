student_properties = {
  "name": "cs",
  "age": 10,
  "class": "Masters"
}
print(student_properties["age"])
print(student_properties["class"])
print(student_properties["name"])
print("**************************")
print("**************************")

ec2_instances_info = [
  {
   "id":"instance-001",
    "type": "t2.micro"   
  },
  {
   "id":"instance-002",
    "type": "t2.medium"   
  },
  {
   "id":"instance-003",
    "type": "t2.macro"   
  }
]

print(ec2_instances_info[1]["type"])