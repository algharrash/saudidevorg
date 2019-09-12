#Python Dictionries part 2

courses = {
    'coe202' : 'Digital Logic Design',
    'coe242' : 'Data and Computer Communications',
    'coe344' : 'Computer Networks'
}

if 'coe202' in courses:
    print("The course COE 202 is the courses list")

print("the number of courses avaliables:")
print(len(courses))

courses['coe301'] = 'Computer Organization'

print(courses)

del courses['coe242']

print(courses)

