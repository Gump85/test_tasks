from django.contrib import admin

from .models import Investor, PassportData, QualificationDocuments, QualificationStatus


class PassportDataInline(admin.TabularInline):
    """ добавление информации о паспортных данных на панель администратора"""
    model = PassportData
    extra = 0  # убираем лишние свободные поля


class QualificationDocumentsInline(admin.TabularInline):
    """ добавление информации о документах для квалификации на панель администратора"""
    model = QualificationDocuments
    extra = 0  # убираем лишние свободные поля


@admin.register(QualificationStatus)
class QualificationStatusdmin(admin.ModelAdmin):
    """ Регистрация модели инвестора на панели администратора """
    list_display = ('qualification_status',)


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    """ Регистрация модели инвестора на панели администратора """
    list_display = ('nick_name',)
    # добавляем отображение паспортных данных на сранице инвестора
    inlines = [PassportDataInline, QualificationDocumentsInline]


@admin.register(PassportData)
class PassportDataAdmin(admin.ModelAdmin):
    """ Регистрация модели паспортных данных на панели администратора """
    list_display = ('last_name', 'first_name', 'passport_number')


@admin.register(QualificationDocuments)
class QualificationDocumentsAdmin(admin.ModelAdmin):
    """ Регистрация модели квалификационных данных на панели администратора """
    list_display = ('qualification_refuse',)
