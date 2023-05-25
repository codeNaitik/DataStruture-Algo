from Employee import employee;

class FullEmp(employee):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary= salary
        
    def salary(self):
        return self.salary
    
    