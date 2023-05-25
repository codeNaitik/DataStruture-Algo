from Employee import employee;
from full import FullEmp;

class Hour(employee):
    def __init__(self, firstname, lastname, rate, hour):
        super().__init__(firstname, lastname)
        self.hour = hour
        self.rate = rate
        
    def salary(self):
        return self.hour*self.rate 
    