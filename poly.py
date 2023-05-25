class complexNumber:
    def __init__(self,real,imaginary):
        self.real =real
        self.imaginary = imaginary

    def __lt__(self, complex_num_2):
        if self.real < complex_num_2.real:
            return True
        elif self.real == complex_num_2.real:
            if self.real < complex_num_2.imaginary:
                return True
            else:
                return False
            
        else: 
            return False
        
    def __str__(self):
        return str(self.real)+ ' +' +str(self.imaginary) +'i'

complex_num1 = complexNumber(1,2)
complex_num2 = complexNumber(3,4)

if complex_num1 < complex_num2:
    print(f"complex ({complex_num1}) less than ({complex_num2})")
else :
    print(f"complex ({complex_num1}) less than  not({complex_num2})")
        
        