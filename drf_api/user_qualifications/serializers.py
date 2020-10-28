from rest_framework import serializers

from .models import Investor, PassportData, QualificationDocuments


class QualificationStatusSerializer(serializers.ModelSerializer):
    """ представление статуса квалификации пользователя для API """

    class Meta:
        model = Investor
        fields = ('qualification_status', 'platform_roules', 'tax_roles', 'autoinvestor_rules')

class InvestorSerializer(serializers.ModelSerializer):
    """ представление модели пользователя для API """

    class Meta:
        model = Investor
        fields = '__all__'


class PassportDataSerializer(serializers.ModelSerializer):
    """ представление модели пасспорта для API """
    investor = InvestorSerializer()

    class Meta:
        model = PassportData
        fields = '__all__'


class PlatformRulesSerializer(serializers.ModelSerializer):
    """ представление модели статуса присоединения к правилам платформы API """

    class Meta:
        model = Investor
        fields = ('nick_name', 'platform_roules', 'tax_roles', 'autoinvestor_rules')


class QualificationDocumentsSerializer(serializers.ModelSerializer):
    """ представление модели квалификационных документов для API """
    investor = InvestorSerializer()

    class Meta:
        model = QualificationDocuments
        fields = '__all__'
