class Employee :
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary
    
    def getSalary(self):
        return self.salary


vivek = Employee("Vivek","2500")

print(vivek.salary)
print(vivek.name)
# print(vivek)

ram = Employee("Ram",3972)
print(ram.salary)
print(ram.name)