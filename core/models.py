from django.db import models


class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # model 생성시 자동으로 날짜 추가
    updated = models.DateTimeField(auto_now=True)  # model 업데이트시 자동으로 날짜 추가

    class Meta:
        abstract = True  # db에는 들어가지 않음 AbstractUser도


# Create your models here.
