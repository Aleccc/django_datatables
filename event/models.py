from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


class Event(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name


class Result(models.Model):
    name = models.CharField('Event Name', max_length=64)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, blank=False,
                              limit_choices_to={'event_type': 'Race'})
    time = models.CharField(blank=True, null=True,
                            max_length=9, help_text='MM:SS.mmm',
                            validators=[RegexValidator(r'^(\d){2}:(\d){2}.(\d){3}$')])
    distance = models.IntegerField(blank=True, null=True, help_text='meters',
                                   validators=[MinValueValidator(0)])

    def __str__(self):
        return '%s (%s)' % (self.name, self.event)
