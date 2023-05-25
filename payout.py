class Payout:
    def __init__(self) :
        self.employee_list =[]
    def add(self, employee):
        self.employee_list.append(employee)
    
    def show(self):
        for i in self.employee_list:
            print(f"{i.fullname} {i.salary}")
