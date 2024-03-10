from rest_framework import serializers


class ContentFormBooleanField(serializers.BooleanField):
    TRUE_VALUES = {"Да"}
    FALSE_VALUES = {"Нет"}
