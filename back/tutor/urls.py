from django.urls import path
from tutor import views
from tutor.views import TutorList, TutorCreate, TutorDetail, TutorProfileEdit

urlpatterns = [
    path('', views.say_hello),
    path('list/', TutorList.as_view()),
    path("list/<int:pk>", TutorDetail.as_view()),
    path('create/', TutorCreate.as_view()),
    path('profile/', TutorProfileEdit.as_view()),
]
