from django.shortcuts import render
from .models import CustomUser , ActivityPeriod
from django.http import JsonResponse
import json
from datetime import datetime

def getUsersViews(request):
	members = []
	users = CustomUser.objects.all()

	for user in users:
		users_dict = {}
		activity_periods_list = []
		print(user)
		users_dict["id"] = user.user_id
		users_dict["real_name"] = user.real_name
		users_dict["tz"] = user.tz
		periods = ActivityPeriod.objects.filter(member = user)

		for period in periods:
			periods_dict = {}
			periods_dict["start_time"] = datetime.strftime(period.start_time, '%b %d %Y %I:%M%p') 
			periods_dict["end_time"] = datetime.strftime(period.end_time, '%b %d %Y %I:%M%p')
			activity_periods_list.append(periods_dict)
		users_dict['activity_periods'] = activity_periods_list
		members.append(users_dict)
	response = {"ok":True , "members":members}
	return JsonResponse(response)

def getUserInfoViews(request,user_id):
	members = []
	users = CustomUser.objects.filter(user_id = user_id)
	for user in users:
		users_dict = {}
		activity_periods_list = []
		print(user)
		users_dict["id"] = user.user_id
		users_dict["real_name"] = user.real_name
		users_dict["tz"] = user.tz
		periods = ActivityPeriod.objects.filter(member = user)

		for period in periods:
			periods_dict = {}
			periods_dict["start_time"] = datetime.strftime(period.start_time, '%b %d %Y %I:%M%p')
			periods_dict["end_time"] = datetime.strftime(period.end_time, '%b %d %Y %I:%M%p')
			activity_periods_list.append(periods_dict)
		users_dict['activity_periods'] = activity_periods_list
		members.append(users_dict)
	response = {"ok":True , "members":members}
	return JsonResponse(response)









