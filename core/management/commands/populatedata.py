# main/management/commands/populatedata.py
from datetime import datetime
import random
import csv
from django.core.management.base import BaseCommand

from core.models import CustomUser , ActivityPeriod


class Command(BaseCommand):
    help = "Save randomly generated record values."

    def add_arguments(self, parser):
        parser.add_argument('userPath', type=str, help='define path of users csv file.')
        parser.add_argument('periodPath', type=str, help='Define path of periods csv file')

    def handle(self, *args , **kwargs):
        records = []

        usersPath = kwargs['userPath']
        periodPath = kwargs['periodPath']
        
        with open(usersPath) as csv_file:
            reader = csv.reader(csv_file,delimiter=',')
            next(reader)

            for user_data in reader:
                kwargs = {
                    'user_id':user_data[0],
                    'real_name': user_data[1],
                    'tz': user_data[2]
                }
                record = CustomUser(**kwargs)
                records.append(record)
        CustomUser.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('User records saved successfully.'))

        users = CustomUser.objects.all()

        periods = []
        for user in users:
            with open(periodPath) as csv_file:
                period_reader = csv.reader(csv_file,delimiter=',')
                next(period_reader)

                for period_data in period_reader:
                    kwargs = {
                        'member':user,
                        'start_time':datetime.strptime(period_data[0], '%b %d %Y %I:%M%p'),
                        'end_time': datetime.strptime(period_data[1], '%b %d %Y %I:%M%p')
                    }
                    period = ActivityPeriod(**kwargs)
                    periods.append(period)
        ActivityPeriod.objects.bulk_create(periods)
        self.stdout.write(self.style.SUCCESS('Period records saved successfully.'))
