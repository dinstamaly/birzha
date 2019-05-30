from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    TaskCreateAPIView, TaskViewDelete, TaskViewDetail, TaskViewList, TaskViewUpdate,
    OrderViewList, OrderCreateAPIView, OrderViewDetail, OrderViewDelete, OrderViewUpdate,
)

# API endpoints
urlpatterns = format_suffix_patterns([

    path('task/', TaskViewList.as_view(), name='task'),
    path('task/<int:id>/delete/', TaskViewDelete.as_view(), name='task_delete'),
    path('task/<int:id>/update/', TaskViewUpdate.as_view(), name='task_update'),
    path('task/<int:id>/', TaskViewDetail.as_view(), name='task_details'),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),

    path('order/', OrderViewList.as_view(), name='order'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('order/<int:id>/', OrderViewDetail.as_view(), name='order_details'),
    path('order/<int:id>/delete/', OrderViewDelete.as_view(), name='order_delete'),
    path('order/<int:id>/update/', OrderViewUpdate.as_view(), name='order_update'),

])
