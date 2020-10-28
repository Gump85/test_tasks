from django.urls import path

from . import views


app_name = 'user_qualifications'

urlpatterns = [
    path('investors/', views.InvestorCreateListView.as_view(), name='create-list-investor'),
    path(
        'passport/<int:pk>/', views.PassportDataRetrieveUpdateAPIView.as_view(),
        name='passpot_data'
    ),
    path(
        'investor/<int:pk>/',
        views.InvestorRetrieveView.as_view(),
        name='investor-qualification-status'
    ),
    path(
        'rules/<int:pk>/',
        views.PlatformRulesRetrieveUpdateAPIView.as_view(),
        name='rules-status'
    ),
    path(
        'qualifications/',
        views.QualificationDocumentsCreateListView.as_view(),
        name='create-list-qualifications'
    ),
]
