from django.db import models

# Create your models here.

class CustomUser(models.Model):
	user_id = models.CharField(max_length=254,default=0, blank=True)
	real_name = models.CharField(max_length=254,default=0, blank=True)
	tz = models.CharField(max_length=254,default=0, blank=True)


class ActivityPeriod(models.Model):
	member = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='member_info',)
	start_time = models.DateTimeField(blank=True)
	end_time = models.DateTimeField(blank=True)
