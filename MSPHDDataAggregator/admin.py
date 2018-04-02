# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from MSPHDDataAggregator.models import Applicant
from MSPHDDataAggregator.models import SocialWorkDetails
from MSPHDDataAggregator.models import RecommendationDetails
from MSPHDDataAggregator.models import ScholarshipDetails
from MSPHDDataAggregator.models import AwardsDetails
from MSPHDDataAggregator.models import ApplicationStatusDetails


# Register your models here.

admin.site.register(Applicant)
admin.site.register(SocialWorkDetails)
admin.site.register(RecommendationDetails)
admin.site.register(ScholarshipDetails)
admin.site.register(AwardsDetails)
admin.site.register(ApplicationStatusDetails)
