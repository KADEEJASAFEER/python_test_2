#create class and employee objects

class Employee:
    def __init__(self,eid,name,desig,mail,sal):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.mail=mail
        self.sal=sal

    def printEmp(self):
        print(self.eid,",",self.name,",",self.desig,",",self.mail,",",self.sal)


#read data from file 'employee'
f=open("employee","r")

emp=[]
for data in f:
    #print(data)
    employee = data.rstrip("\n").split(",")
    eid = employee[0]
    name = employee[1]
    desig = employee[2]
    mail = employee[3]
    sal = int(employee[4])
    ob=Employee(eid,name,desig,mail,sal)
    ob.printEmp()
    emp.append(ob)

#maximum salary of employee
for employee in emp:
    salary=employee.sal
    print(max(salary))








