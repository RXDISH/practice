class student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

ferris = student()

ferris.student_id = 10837
ferris.name = 'Ferris Bueller'
ferris.year = 12
ferris.gpa = 3.81
ferris.enrolled = True

print(vars(ferris))