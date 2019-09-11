import sys

from mymodules.models import Student
from mymodules.math_utils import average_grade


def main(args):
	students = [Student("S1", 89)]
	students.append(Student("S2", 67))
	students.append(Student("S3", 74))
	students.append(Student("S4", 93))
        students.append(Student("S5", 50))
	students.append(Student("S6", 65))
        students.append(Student("S7", 77))
        students.append(Student("S8", 39))
        students.append(Student("S9", 100))

	for student in students:
		student.print_student_info()
	print(average_grade(students))


if __name__ == '__main__':
	main(sys.argv)
