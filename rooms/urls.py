from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]
# django path 설정한 형식을 입력했을때만 접속가능
