from django.db import models



class Ticket(models.Model):
    class Status(models.TextChoices):
        STATUS_CLOSED = 'close'
        STATUS_OPEN = 'open'
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=Status.choices, default='open')
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts',
                                  on_delete=models.CASCADE)


