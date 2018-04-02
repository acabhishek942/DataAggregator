# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Applicant(models.Model):
	studentName = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	undergradInstittute = models.TextField()
	undergradDegree = models.CharField(max_length=255)
	undergradBranch = models.CharField(max_length=50)
	undergradGPA = models.FloatField()
	GREScore = models.IntegerField()
	GMATScore = models.IntegerField()
	email = models.EmailField()


class SocialWorkDetails(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
	socialWork = models.TextField()

class RecommendationDetails(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
	recommendation = models.CharField(max_length=255)

class ScholarshipDetails(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
	scholarship = models.CharField(max_length=255)

class AwardsDetails(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
	award = models.CharField(max_length=255)

class ApplicationStatusDetails(models.Model):
	applicationStatusChoices = (
		('Applied', 'Applied'),
		('Admit', 'Admit'),
		('Reject', 'Reject'))
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
	applicationUniversity = models.CharField(max_length=255)
	applicationStatus = models.CharField(max_length=10, choices=applicationStatusChoices)



