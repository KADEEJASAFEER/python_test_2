#validate mail from employee file
import re

f=open("employee","r")

emp=[]
for data in f:
    #print(data)
    employee = data.rstrip("\n").split(",")
    mail = employee[3]
    print(mail)
    x = '[a-zA-Z]\w*@gmail[.]com'
    match = re.fullmatch(x, mail)
    if (match != None):
        print("valid")
    else:
        print("invalid")