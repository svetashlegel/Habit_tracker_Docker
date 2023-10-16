from django.urls import path
from habits.views import HabitCreateView, HabitListView, HabitDetailView, HabitUpdateView, HabitDeleteView

from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path("list/", HabitListView.as_view(), name='habit_list'),
    path("detail/<int:pk>/", HabitDetailView.as_view(), name='habit_detail'),
    path("update/<int:pk>/", HabitUpdateView.as_view(), name='habit_update'),
    path("delete/<int:pk>/", HabitDeleteView.as_view(), name='habit_delete'),
]
