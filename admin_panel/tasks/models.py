from django.db import models
from django_quill.fields import QuillField


class TemplatesByTypes(models.TextChoices):
    new_user = 'welcome', 'Письмо новому пользователю о новинках'
    monthly_newsletter = 'monthly', 'Ежемесячная рассылка'
    personal_selection = 'personal', 'Персональная подборка'


class Templates(models.Model):
    title = models.CharField('Заголовок шаблона рассылки', max_length=120)
    type = models.CharField('Тип рассылки', choices=TemplatesByTypes.choices, max_length=50)
    text = QuillField('Сообщение пользователю')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Templates'
        db_table = 'notification_templates'


class NotificationStatus(models.TextChoices):
    sending = 'send', 'Поставить на отправку'
    letter_sent = 'letter_sent', 'Письма отправлены'


class Tasks(models.Model):
    title = models.CharField('Название задачи', max_length=120)
    status = models.CharField('Статус рассылки', choices=NotificationStatus.choices, max_length=50)
    template = models.ForeignKey(Templates, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tasks'
        db_table = 'mailing_list_tasks'
