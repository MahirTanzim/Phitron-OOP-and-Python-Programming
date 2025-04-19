class calculator:
    model = "Casio MS100"
    def add (self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mult(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    

a, b  = map(int, input().split())
mycal = calculator()
print(mycal.add(a, b))
print(mycal.sub(a, b))
print(mycal.mult(a, b))
print(mycal.div(a, b))
