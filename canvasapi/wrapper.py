# pip3 install canvasapi
from canvasapi import Canvas


class apiwrapper:

    API_URL = "https://ufl.instructure.com/"
    API_KEY = ""
    canvas = ""

    def __init__(self, name):
        self.name = name

    def setApiKey(self, input):
        self.API_KEY = input
        # Debug
        self.createCanvasObj()
        

    def createCanvasObj(self):
        self.canvas = Canvas(self.API_URL, self.API_KEY)

    def getCourses(self):
        user_courses = {}
        current_year = 2022
        courses = self.canvas.get_courses()
        for i, course in enumerate(courses):
            try:
                current_course = courses[i]
                course_year = current_course.start_at_date.timetuple().tm_year
                if current_year <= course_year:
                    user_courses[current_course.name] = current_course
            except:
                continue
        return user_courses

    def getAssignments(self, course, currentmonth, currentday):
        assignments = course.get_assignments()
        user_assignments = {}
        for i, assignment in enumerate(assignments):
            try:
                current_assignment = assignments[i]
                assignmentmonth = current_assignment.lock_at_date.timetuple().tm_mon
                if assignmentmonth >= currentmonth:
                    assignmentday = current_assignment.lock_at_date.timetuple().tm_mday
                    if assignmentday >= currentday:
                        user_assignments[assignment.name] = assignment.lock_at_date
            except:
                continue











