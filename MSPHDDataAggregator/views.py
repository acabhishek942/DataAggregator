# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import datetime

from . import models

# Create your views here.

def viewGrid(request):
	first10Students = models.Applicant.objects.all()[:10]
	socialWorkDetails = {}
	applicationStatusDetails = {}
	awardsDetails = {}
	scholarshipDetails = {}
	recommendationsDetails = {}
	for student in first10Students:
		socialWorkDetails[student.studentName] = models.SocialWorkDetails.objects.filter(applicant=student)
		applicationStatusDetails[student.studentName] = models.ApplicationStatusDetails.objects.filter(applicant=student)
		awardsDetails[student.studentName] = models.AwardsDetails.objects.filter(applicant=student)
		scholarshipDetails[student.studentName] = models.ScholarshipDetails.objects.filter(applicant=student)
		recommendationsDetails[student.studentName] = models.RecommendationDetails.objects.filter(applicant=student)

	return render(request, 'home.html', {'students' : first10Students, 'socialWorkDetails' : socialWorkDetails,
										'applicationStatusDetails' : applicationStatusDetails,
										'awardsDetails' : awardsDetails,
										'scholarshipDetails' : scholarshipDetails,
										'recommendationsDetails' : recommendationsDetails,})