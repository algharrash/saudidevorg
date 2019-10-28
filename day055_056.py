#JSON in python

import json

studentInfo = {
    "name" : "Ali",
    "Birthdate" : 1982,
    "Major" : "Computer Engineering",
    "Minor" : None,
    "CurrentCourses" : ("COE-300", "COE-344"),
    "FinishedCourses" : [
        {"Course Code":"COE-202", "Course Name":"Digital Logic Design", "Credit":3,"Grade":"A"},
        {"Course Code":"COE-241", "Course Name":"Data and Computer Communications", "Credit":3,"Grade":"B+"},
    ]
}

print(json.dumps(studentInfo, indent=4, sort_keys=True))

