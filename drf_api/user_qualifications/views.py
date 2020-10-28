from rest_framework import generics

from .models import Investor, PassportData, QualificationDocuments
from .serializers import (
    InvestorSerializer,
    PassportDataSerializer,
    QualificationStatusSerializer,
    PlatformRulesSerializer,
    QualificationDocumentsSerializer
)


class InvestorRetrieveView(generics.RetrieveAPIView):
    """ API для просмотра только статуса квалификации инвестора """
    queryset = Investor.objects.all()
    serializer_class = QualificationStatusSerializer


class InvestorCreateListView(generics.ListCreateAPIView):
    """ API для создания инвестора и просмотра общих данных"""
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class PassportDataRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ API для создания модели паспоратных данных и просмотра информации """
    queryset = PassportData.objects.all()
    serializer_class = PassportDataSerializer


class PlatformRulesRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ API для присоединения к правилам платформы и просмотра статуса """
    queryset = Investor.objects.all()
    serializer_class = PlatformRulesSerializer

class QualificationDocumentsCreateListView(generics.ListCreateAPIView):
    """ API для создания модели паспорат и просмотра всех паспортов """
    queryset = QualificationDocuments.objects.all()
    serializer_class = QualificationDocumentsSerializer
