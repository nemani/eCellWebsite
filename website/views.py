from django.shortcuts import render

# home part
def home(request):
	return render(request,'website/home.html')
# about part
def vision(request):
	return render(request,'website/vision.html')

def successStories(request):
	return render(request,'website/success_stories.html')

# Events part

def talks(request):
	return render(request,'website/talks.html')

def hackathons(request):
	return render(request,'website/hackathons.html')

def workshops(request):
	return render(request,'website/workshops.html')

# associates part

def associates(request):
	return render(request,'website/associates.html')

def patners(request):
	return render(request,'website/patners.html')

def sponsors(request):
	return render(request,'website/sponsors.html')

# gallery

def gallery(request):
	return render(request,'website/gallery.html')

# mentors

def industry(request):
	return render(request,'website/industry.html')

def students(request):
	return render(request,'website/students.html')

def faculty(request):
	return render(request,'website/faculty.html')

# e resources 

def eResources(request):
	return render(request,'website/e-resources.html')

# team

def team(request):
	return render(request,'website/team.html')