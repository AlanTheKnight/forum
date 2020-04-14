from django.db import models


class JoinTeamMessages(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    surname = models.CharField(verbose_name="Фамилия", max_length=100)
    age = models.IntegerField(verbose_name="Возраст")
    email = models.CharField(verbose_name="Почта", max_length=100)
    description = models.TextField(verbose_name="Описание")
    phone = models.CharField(verbose_name="Телефон", max_length=50, blank=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['surname', 'name']

    def __str__(self):
        return "{} {}".format(self.surname, self.name)
        