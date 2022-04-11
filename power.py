class power():
    def power_number(self):
        x=int(input("Enter the number whose power is find out(x)-"))
        y=int(input("Enter the power(n)-"))
        self.number=x
        self.power=y
        f=pow(self.number,self.power)
        return f
Number=power()
print("Answer-",Number.power_number())
