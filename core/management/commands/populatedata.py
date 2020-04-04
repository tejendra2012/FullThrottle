# main/management/commands/populatedata.py
from datetime import datetime
import random

from django.core.management.base import BaseCommand

from core.models import CustomUser , ActivityPeriod


class Command(BaseCommand):
    help = "Save randomly generated record values."

    def handle(self, *args, **options):
        records = []
        user_id_list = ['W012A3CDE' , 'W07QCRPA4']
        real_name_list = ['Egon Spengler', 'Glinda Southgood']
        start_time_list = ['Feb 1 2020  1:33PM','Mar 1 2020  11:11AM' , 'Mar 16 2020  5:33PM']
        end_time_list =  ['Feb 1 2020 1:54PM' , 'Mar 1 2020 2:00PM' , 'Mar 16 2020 8:02PM']
        tz_list = ['America/Los_Angeles' , 'Asia/Kolkata']
        for i in range(len(real_name_list)):
            kwargs = {
                'user_id':user_id_list[i],
                'real_name': real_name_list[i],
                'tz': tz_list[i]
            }
            record = CustomUser(**kwargs)
            records.append(record)
        CustomUser.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('User records saved successfully.'))

        users = CustomUser.objects.all()

        periods = []
        for user in users:
            for i in range(len(start_time_list)):
                kwargs = {
                    'member':user,
                    'start_time':datetime.strptime(start_time_list[i], '%b %d %Y %I:%M%p'),
                    'end_time': datetime.strptime(end_time_list[i], '%b %d %Y %I:%M%p')
                }
                period = ActivityPeriod(**kwargs)
                periods.append(period)
        ActivityPeriod.objects.bulk_create(periods)
        self.stdout.write(self.style.SUCCESS('Period records saved successfully.'))
