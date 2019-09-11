from models import Student

def average_grade(roster):
	sum = 0
	for student in roster:
		sum += student.get_grade()
	if len(roster) < 1:
		return 0
	return sum/len(roster)
