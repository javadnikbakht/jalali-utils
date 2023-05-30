import django_filters

from django_toman_time_utils.fields import JalaliDateRangeField, JalaliDateTimeRangeField


class JalaliDateFromToRangeFilter(django_filters.DateFromToRangeFilter):
    """
    An extension on django_filters.IsoDateTimeFromToRangeFilter which accepts Jalali date as input and then
     converts it to datetime instance.
    """
    field_class = JalaliDateRangeField


class JalaliIsoDateTimeFromToRangeFilter(django_filters.IsoDateTimeFromToRangeFilter):
    """
    An extension on django_filters.IsoDateTimeFromToRangeFilter which accepts Jalali datetime as input and then
     converts it to datetime instance.
    """
    field_class = JalaliDateTimeRangeField
