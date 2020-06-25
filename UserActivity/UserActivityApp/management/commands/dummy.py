from django.core.management.base import BaseCommand

from UserActivityApp.factory import MemberFactory,PeriodFactory


class Command(BaseCommand):
    def add_arguments(self,parser):
        """
        Custom management command parsers to populate the data
        """

        parser.add_argument('--populate',
                default=50,
                type=int,
                help='The number of fake data to create.')


    def handle(self, *args, **options):
            for _ in range(options['populate']):
                    PeriodFactory.create()

"""
python manage.py --populate [value]  (which is Custom management command to populate fake datta)

"""
