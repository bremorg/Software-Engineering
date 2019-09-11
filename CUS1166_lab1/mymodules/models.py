class Student:
	def __init__(self, name="", grade=0):
		self.name = name
		self.grade = grade


	def set_grade(self, grade):
		self.grade = grade

	def get_grade(self):
		return self.grade

	def print_student_info(self):
		print("Name: " + str(self.name) + "\nGrade: " + str(self.grade))


