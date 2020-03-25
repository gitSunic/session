from django.db import models


class Ticket(models.Model):
    num = models.IntegerField(unique=True)
    name = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['num']

    def __str__(self):
        return str(self.num) + '. ' + str(self.name)


class PhysImg(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='physics/')
    pos = models.IntegerField()

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['ticket__num', 'pos']

    def __str__(self):
        return str(self.ticket.num) + '. Страница ' + str(self.pos)
