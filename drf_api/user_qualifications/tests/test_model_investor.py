from django.test import TestCase

from user_qualifications.models import Investor, QualificationStatus


class InvestorModelTest(TestCase):
    """ тестируем модель категории книг """

    @classmethod
    def setUpTestData(cls):
        """ создаем объект для тестирования модели """
        status = QualificationStatus.objects.create(qualification_status='no')
        Investor.objects.create(nick_name='Mike', qualification_status=status)

    def test_nick_name_lable(self):
        """ проверяем ярлык поля nick_name"""
        investor = Investor.objects.get(id=1)
        field_lable = investor._meta.get_field('nick_name').verbose_name
        self.assertEquals(field_lable, 'Ник инвестора')

    def test_nick_name_max_length(self):
        """ проверяем длину поля nick_name """
        investor = Investor.objects.get(id=1)
        field_length = investor._meta.get_field('nick_name').max_length
        self.assertEquals(field_length, 100)

    def test_str_method(self):
        """ проверяем строковое представление класса """
        investor = Investor.objects.get(id=1)
        self.assertEquals(str(investor), 'Инвестор: Mike')
