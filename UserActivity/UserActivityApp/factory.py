import factory
import factory.django
from .models import Member,ActivityPeriod

from django.utils import timezone
class MemberFactory(factory.django.DjangoModelFactory):
    """
    Factory Faker of MemberFactory class
    """
    class Meta:
        model = Member

    mid = factory.Faker('pystr')
    real_name = factory.Faker('first_name')
    tz = factory.Faker('timezone')


class PeriodFactory(factory.django.DjangoModelFactory):
    """
    Factory Faker of PeriodFactory class
    """
    class Meta:
        model = ActivityPeriod
    member  = factory.SubFactory(MemberFactory)
    start   = factory.Faker('date_time',tzinfo=timezone.get_current_timezone())
    end     = factory.Faker('date_time',tzinfo=timezone.get_current_timezone())
