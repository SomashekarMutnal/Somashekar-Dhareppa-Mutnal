#CALCULATOR
class Calculator:
    def info(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Non zero number will not divided by zero"
        else:
            return self.a/self.b

    def Solution(self):
        if(self.operation == "add"):
            return self.add()
        
        elif(self.operation == "sub"):
            return self.sub()
        
        elif(self.operation == "div"):
            return self.div()
        
        elif(self.operation == "mul"):
            return self.mul()

calc = Calculator()
calc.a = float(input("Enter First value:"))
calc.b = float(input("Enter Second value:"))
calc.operation = input("Enter any one of these add/sub/div/mul:")
print(calc.Solution())