# print ("OMNS");
# print (">>>>>>>>>>>>>>>>>");


# s = "chandra shekar Bakam"
# s1 = "Warangal"
# print(s.upper());
# print(s.split()[0]);
# print (s+" "+s1);

arn = " arn:aws:service:region:account-id:resource-id BCS "
print(arn.upper());
print(arn.lower());
print(len(arn));
print(arn.split(":")[2]);
new_text = arn.replace("region","BCS");
print (new_text);
print(arn);
print(arn.strip());
substring = ":"
if substring in arn :
     print(substring , "found in the arn string");
else :
 print(substring , "not found in the arn string");




