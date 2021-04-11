from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", related_name="converstation")

    def __str__(self):
        usernames1 = []
        for user in self.participants.all():
            usernames1.append(user.username)
        return ", ".join(
            usernames1
        )  # return str(self.created)  # self.created는 string 이 아님

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says:{self.message}"
