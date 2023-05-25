from abc import ABC , abstractmethod

class employee(ABC):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    @property
    def fullName(self):
        return f"{self.firstname} {self.lastname}"
    @abstractmethod
    
    def salary(self):
        pass