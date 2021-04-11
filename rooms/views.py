from django.views.generic import ListView
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse

# from django.shortcuts import render, redirect
# from math import ceil
# from django.http import HttpResponse
# from datetime import datetime
# from django.core.paginator import Paginator, EmptyPage
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context가 비어있다면 Data가 안나타남 !!
        context["now"] = timezone.now()
        # context를 추가할 수 있다 다음과 같이..
        return context


def room_detail(request, pk):
    # try:
    #     room = models.Room.objects.get(pk=pk)
    #     return render(request, "rooms/detail.html", {"room": room})
    # except models.Room.DoesNotExist:
    #     return redirect(reverse("core:home"))
    try:
        room = models.Room.objects.get(pk=pk)
        print(room)
    except Exception:
        print(Exception)
        return redirect(reverse("core:home"))
    return render(request, "rooms/detail.html", {"room": room})
    # url 에서 pk 라는 argument를 보내주므로


# Create your views here.
##------------------- paginator 사용해서 만들기
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     # 쿼리셋은 게으르다 -> 즉시 Data를 불러오지 않음
#     # paginator = Paginator(room_list, 10)
#     # paginator 가 알아서 10개씩 나눠줌
#     # rooms = paginator.get_page(page)
#     # print(vars(rooms), "\n and", vars(rooms.paginator))
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#     except EmptyPage:
#         # rooms = paginator.page(1)
#         # print("redirect..")
#         print(EmptyPage)
#         return redirect("/?page=1")
#     except ValueError:
#         print(ValueError)
#         return redirect("/?page=1")

#     # page는 예외사항 발생시 exception을 발생시킴
#     return render(request, "rooms/home.html", {"page": rooms})

###------------------- 수동으로 만들기

# rooms.paginator 에 paginate 하기 위한 유용한 메소드,속성 들이 있음
# return render(request, "rooms/home.html", {"rooms": rooms})
# page = request.GET.get("page", 1)
# page = int(page or 1)
# page_size = 10
# limit = page_size * page
# offset = limit - page_size
# # print(dir(request))
# # return HttpResponse(content="hello")
# all_rooms = models.Room.objects.all()[offset:limit]
# # print(f"{request.path_info} ,{dir(request.path_info)}")
# if not bool(all_rooms):
#     return redirect("/?page=1")

# # print(all_rooms )
# # now = datetime.now()
# # hungry = True
# # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
# page_count = ceil(models.Room.objects.count() / page_size)
# return render(
#     request,
#     "rooms/home.html",
#     {
#         "rooms": all_rooms,
#         "page": page,
#         "page_count": page_count,
#         "page_range": range(1, page_count),
#         # html은 파이썬 코드가 아니기 때문에 for 문에 쓰일 Range는 여기서 변형 후 보내준다
#     },
# )
# return render(request, "rooms/home.html", context={"rooms": all_rooms})
# url.py 에있는 이름과
