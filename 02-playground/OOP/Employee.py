class Employee:
	raise_amount = 1.04
	num_of_emps = 0
	def __init__(self , first , last , pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '_' + last + '@gmail.com'
		Employee.num_of_emps += 1 
		'''in this case we don't have to use self keyword 
			and notice we can only access the class variable
			by the class name or instance itself we can't type
			it as num_of_emps += 1'''

	def fullName(self):
		return '{} {} '.format(self.first , self.last)


	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)
		
emp1 = Employee('Corey' , 'Schafer' , 5000)
emp2 = Employee('andrew' , 'george' , 6000)

#print(emp1.pay)
#emp1.apply_raise()

emp1.raise_amount = 1.05
print(Employee.num_of_emps)