from django.db import models

# Create your models here.

status_choices = [('new', 'новая'), ('in_progress', 'в процессе'), ('done', 'сделано')]


class Task(models.Model):
    description = models.CharField(max_length=50, null=False, verbose_name='Название')
    status = models.CharField(max_length=50, default='new', verbose_name='Статус')
    date = models.DateField(max_length=50, null=False, verbose_name='Дата')

    def __str__(self):
        return f'{self.description} {self.status}'

    class Meta:
        db_table = 'tasks'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'