from django.db import models

from datetime import datetime, timedelta


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date']

    def save(self, *args, **kwargs):
        self.date = datetime.now() + timedelta(hours=3)
        return super(Feedback, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + '\t' + str(datetime.strftime(self.date, '%d-%m %H:%M'))
