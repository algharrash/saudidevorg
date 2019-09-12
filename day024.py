#Python Dictioneries Part 3

coe_courses = {
    'coe202' : 'Digital Logic Design',
    'coe242' : 'Data and Computer Communications',
    'coe344' : 'Computer Networks'
}

swe_courses = dict(swe205='Introduction to Software Engineering', swe215='Software Requirements Engineering', swe311='Principles of Software Engineering')

ics_courses = {
    'ics101' : 'Computer Programming',
    'ics102' : 'Introduction to Computing I',
    'ics103' : 'Computer Programming in C'
}

majors = {
    'COE' : coe_courses,
    'SWE' : swe_courses,
    'ICS' : ics_courses
}

print(majors)

for x, y in majors.items():
    print(x, y)