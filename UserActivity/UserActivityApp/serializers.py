from rest_framework import serializers
from .models import Member,ActivityPeriod
import six


"""   Serializing Model Instances for the representation which we can streamable over the network """

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields=('start','end')

class UserSerializer(serializers.ModelSerializer):
    tz= serializers.SerializerMethodField()
    activity_periods =PeriodSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields=('mid','real_name','tz','activity_periods')


    def get_tz(self, obj):
        return six.text_type(obj.tz)
