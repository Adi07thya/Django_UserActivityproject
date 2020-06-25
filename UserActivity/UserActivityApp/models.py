from django.db import models
import pytz
from timezone_field import TimeZoneField


"""
Creating member models which contains mid,real_name,timezone as tz
"""
class Member(models.Model):
    mid           = models.CharField(max_length=12)
    real_name    = models.CharField(max_length=60)
    tz           = TimeZoneField(default='Europe/London')


"""
creating Activity period models contains start date and end date

"""    


class ActivityPeriod(models.Model):
     member       = models.ForeignKey(Member, related_name='activity_periods',on_delete =models.CASCADE,null=True)
     start        = models.DateTimeField()
     end          = models.DateTimeField()
