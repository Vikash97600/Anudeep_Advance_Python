class myClass:
    def __init__(self,value):
        self.protectedVariable=value
    
    def protectedMethod(self):
        return self.protectedVariable

my=myClass(10)
print(my.protectedMethod())