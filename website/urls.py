from django.conf.urls import patterns, url
from website import views

urlpatterns = [
	url(r'^$', views.home, name = home),
	# about
	url(r'^about/vision/', views.vision, name = vision),
	url(r'^about/success_stories/', views.success_stories, name = success_stories),
	# events
	url(r'^events/talks', views.talks, name = talks),
	url(r'^events/hackathons', views.hackathons, name = hackathons),
	url(r'^events/Workshops', views.workshops, name = workshops),
	# associates
	url(r'^associates/associates/', views.associates, name = associates),
	url(r'^associates/patners/', views.patners, name = patners),
	url(r'^associates/sponsors/', views.sponsors, name = sponsors),
	# gallery
	url(r'^gallery/', views.gallery, name = gallery),
	# mentors
	url(r'^mentors/industry/', views.industry, name = industry),
	url(r'^mentors/students/', views.students, name = students),
	url(r'^mentors/faculty/', views.faculty, name = faculty),
	# e resources
	url(r'^e-resources/', views.e-resources, name = e-resources),
	# team
	url(r'^team/', views.team, name = team),
]