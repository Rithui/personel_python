class employee:
    def __intit__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@gmail.com'

emp_1=employee('rithuik','prakash',5000)
emp_2=employee('anooja','prakash',10000)

#print(emp_1)
#print(emp_2)


print(emp_1.email)
print(emp_2.email)
