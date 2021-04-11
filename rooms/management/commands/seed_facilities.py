from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import Facility


class Command(BaseCommand):
    help = "hello friends"
    print("hello")

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="this is number function")

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
        # print(args, options)
        # times = options.get("times")

        # for t in range(int(times)):
        #     self.stdout.write(self.style.SUCCESS("I love you"))
        # print("i love you")
