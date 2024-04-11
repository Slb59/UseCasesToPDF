from django.urls import path
from .views import StoryListView, StoryDetailView
from .views import StoryCreateView, StoryUpdateView, StoryDeleteView

app_name = "cruducd"

urlpatterns = [
    path('', StoryListView.as_view(), name='all'),

    path('story/<int:pk>/detail',
         StoryDetailView.as_view(),
         name='story_detail'),

    path('story/create/',
         StoryCreateView.as_view(),
         name='story_create'),

    path('story/<int:pk>/update/',
         StoryUpdateView.as_view(),
         name='story_update'),

    path('story/<int:pk>/delete/',
         StoryDeleteView.as_view(),
         name='story_delete'),
]
