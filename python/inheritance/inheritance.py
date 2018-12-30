class Person(object):

	def __init__(self, first_name, last_name, age, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender

	def print_full_name(self):
		msg = '{first_name} {last_name}'.format(
			first_name=self.first_name, last_name=self.last_name)
		print(msg)


class Teacher(Person):

	def __init__(self, first_name, last_name, age, gender, subject):
		super().__init__(first_name, last_name, age, gender)
		self.subject = subject


	def print_subject(self):
		msg = "Subject: {subject}".format(subject=self.subject)
		print(msg)


class Student(Person):

	def __init__(self, first_name, last_name, age, gender, std_class):
		super().__init__(first_name, last_name, age, gender)
		self.std_class = std_class


	def print_class_name(self):
		msg = 'Class name: {name}'.format(name=self.std_class)
		print(msg)


p = Person('Shera', 'Md', 20, 'Male')
p.print_full_name()


t = Teacher('Gilchrist', 'Adam', 20, 'Male', 'Maths')
t.print_full_name()
t.print_subject()

s = Student('Priya', 'Ch', 20, 'Female', '3rd Class')
s.print_full_name()
s.print_class_name()
