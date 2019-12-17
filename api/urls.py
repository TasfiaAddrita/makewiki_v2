from django.urls import path

from .views import PageList, PageDetail

urlpatterns = [
    path('page/', PageList.as_view(), name='page-list'),
    # path('page/<slug>', PageDetail.as_view(), name='page-detail')
]