from django.urls import path
from . import views

urlpatterns = [
    path('blocks/', views.blocks, name='blocks'),
    path('blocks/<int:pk>', views.BlockDetailViews.as_view(), name='block_height')
]


