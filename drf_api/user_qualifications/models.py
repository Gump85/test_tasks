from django.db import models
from django.core.validators import FileExtensionValidator


class QualificationStatus(models.Model):
    """ модель общего статуса квалификации пользователя """
    QUALIFICATION_STATUS = (
        ('yes', 'квалификация подтверждена'),
        ('no', 'квалификация не подтверждена'),
        ('check', 'документы на проверке'),
    )

    qualification_status = models.CharField(
        'Общий статус квалификации пользователя',
        max_length=5,
        choices=QUALIFICATION_STATUS,
        default='no',
    )

    class Meta:
        verbose_name_plural = "Qualification status"

    def __str__(self):
        """возвращает строковое значение для представления объекта модели"""
        return f'Статус квалификации: {self.qualification_status}'


class Investor(models.Model):
    """ модель пользоватля для тестирования методов """
    nick_name = models.CharField('Ник инвестора', max_length=100)
    qualification_status = models.ForeignKey(
        QualificationStatus,
        on_delete=models.PROTECT,
        verbose_name='Общий статус квалификации пользователя',
    )

    platform_roules = models.BooleanField(
        'Ознакомление с правилами платформы и принятие рисков',
        default=False
    )
    tax_roles = models.BooleanField(
        'Подтверждение налогового статуса',
        default=False
    )
    autoinvestor_rules = models.BooleanField(
        'Согласие с использованием автоинвестирования',
        default=False
    )

    def __str__(self):
        """возвращает строковое значение для представления объекта модели"""
        return f'Инвестор: {self.nick_name}'
# end class


class PassportData(models.Model):
    """ модель паспортных данных """
    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        verbose_name='Инвестор',
    )
    first_name = models.CharField('Имя пользователя', max_length=50)
    last_name = models.CharField('Фамилия пользователя', max_length=50)
    patronymic = models.CharField('Отчетсво пользователя', max_length=50, null=True, blank=True)
    passport_number = models.CharField('Серия и номер паспорта', max_length=12)
    date_of_birth = models.DateField('Дата рождения')
    place_of_birth = models.CharField('Место рождения', max_length=100)
    passport_issue_date = models.DateField('Дата выдачи пасспорта')
    police_station_code = models.CharField('Код подразделения', max_length=7)
    police_station_name = models.CharField('Кем выдан', max_length=100)
    investor_registration_address = models.CharField('Адрес регистрации', max_length=100)
    passport_first_sheet = models.FileField(
        'Первый разворот паспорта',
        upload_to='files',
        validators=[FileExtensionValidator(['pdf'])]
    )
    passport_second_sheet = models.FileField(
        'Второй разворот паспорта',
        upload_to='files',
        validators=[FileExtensionValidator(['pdf'])]
    )

    def __str__(self):
        """возвращает строковое значение для представления объекта модели"""
        return f'Серия и номер пасспорта: {self.passport_number}'

    class Meta:
        ordering = ['passport_number']
        verbose_name_plural = "Passport data"
# end class


class QualificationDocuments(models.Model):
    """ модель документов для квалификации """
    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        verbose_name='Инвестор',
    )
    qualification_refuse = models.BooleanField(
        'Отказ от квалификации',
        default=False
    )
    economic_education = models.FileField(
        'Высшее экономическое образование с правом аттестации профучастника',
        upload_to='files',
        null=True, blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )
    securities_value = models.FileField(
        'Общая стоимость ценных бумаг',
        upload_to='files',
        null=True, blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )
    economic_work_experience = models.FileField(
        'Опыт работы в финансовой компании',
        upload_to='files',
        null=True, blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )
    deposit_and_metals = models.FileField(
        'Депозитные и металлические счета',
        upload_to='files',
        null=True, blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )
    active_trading = models.FileField(
        'активная торговля ценными бумагами',
        upload_to='files',
        null=True, blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )
    existing_qualifications = models.FileField(
        'активная торговля ценными бумагами',
        upload_to='files',
        null=True, blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )

    class Meta:
        verbose_name_plural = "Qualification Documents"
# enc class
