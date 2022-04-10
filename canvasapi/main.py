from wrapper import apiwrapper

# TEST API KEY: 1016~d5MDqEcPea2Db5TbYdSxPzGtCX4KuKkLJa5H0Xab7Om8wbWUcVgHSljPRKwrMga2
# 1016~NCyUk8Usk5jeSh9CurevMLhg4kIRPUhvtz1VOBbYaHogI8fQyyJrD3KSuDhEZAd1


print("Enter an UFL.INSTRUCTURE API KEY:")
temp_key = str(input())


# This method sets the backend to use the User's canvas API key
canvas = apiwrapper('User')
canvas.setApiKey(temp_key)

# This example grabs the user courses
my_courses = canvas.getCourses()

# This is how to cycle through the courses and access the course name
for course in my_courses:
    # Prints the current course name
    print(my_courses[course].name)
    print("===============================")
    # Grabs all the user assignments due after the current date
    # in this case the month I entered was April (4) and day 9
    canvas.getAssignments(my_courses[course], 4, 9)
    print("\n")




