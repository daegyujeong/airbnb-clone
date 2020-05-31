# 파이선 관련 import
from django.db import models  # 장고 관련 import
from django_countries.fields import CountryField  # third party 관련 import
from core import models as core_models  # 폴더내부 import
from users import models as user_models  # 폴더내부 import


# Create your models here.
class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class RoomType(AbstractItem):
    """RoomType model Definition"""

    class Meta:
        verbose_name = "RoomType"
        ordering = ["name"]


class Amenity(AbstractItem):
    """Amenity model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Deginition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Deginition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE) # 파이썬은 코드를 위에서 아래로 읽으므로 Photo를 아래쪽에 두거나 string화 한다
    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """ Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    House_rules = models.ManyToManyField("HouseRule", blank=True)
    # host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    # amenities = models.ManyToManyField(Amenity, blank=True)
    # facilities = models.ManyToManyField(Facility, blank=True)
    # House_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name
