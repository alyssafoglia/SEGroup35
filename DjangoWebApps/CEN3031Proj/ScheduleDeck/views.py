from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wrapper import apiwrapper
from array import *

def projAbout(request):
	return render(request, 'ScheduleDeck/projAbout.html')

def projHome(request):
	return render(request, 'ScheduleDeck/projHome.html')

def index(request):
	from django.conf import settings
	return render(request, 'ScheduleDeck/index.html')

@csrf_exempt
def simple_function(request):

	#1016~ILBiiO5jAiMdWdVaEUzw8pGHibFuvWLM0TMX2B9K8eLg62u5JR4CQkun4tMZopNw

	if request.method == "POST":
		key = request.POST.get('key')

	canvas = apiwrapper('User')
	canvas.setApiKey(key)

	my_courses = canvas.getCourses()
	
	course_data = []
	

	for i, course in enumerate(my_courses):
		my_assignments=[]
		my_assignments = canvas.getAssignments(my_courses[course], 4, 14)
		current_course_data = []
		
		if len(my_assignments) == 0:
		#if not my_assignments:
			continue

		current_course_data.append(my_courses[course].name)

		for assignment in my_assignments:
			
			#assignmentdate = canvas.getDate(my_assignments[assignment]) #added
			
			current_course_data.append(my_assignments[assignment].name) 
			

		course_data.append(current_course_data)
		#list2=canvas.getDate(current_course_data)
		#course_data[current_course_data]=list2
		

	return render(request, 'ScheduleDeck/result.html', {"course_data": course_data})

def result(request):
	return render(request, 'ScheduleDeck/result.html')