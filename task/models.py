import datetime

from django.db import models
from django.db import models, transaction
from django.db.models import F


class StepManager(models.Manager):
    """ Manager to encapsulate bits of business logic """

    def move(self, obj, new_order):
        """ Move an object to a new order position """

        qs = self.get_queryset()

        with transaction.atomic():
            if obj.order > int(new_order):
                qs.filter(
                    order__lt=obj.order,
                    order__gte=new_order,
                ).exclude(
                    pk=obj.pk
                ).update(
                    order=F('order') + 1,
                )
            else:
                qs.filter(
                    order__lte=new_order,
                    order__gt=obj.order,
                ).exclude(
                    pk=obj.pk,
                ).update(
                    order=F('order') - 1,
                )

            obj.order = new_order
            obj.save()


def order_number():

    if not Task.objects.all().last():
        return 1

    last_order = Task.objects.all().order_by('order').last()

    order = last_order.order
    print(order)


    return order+1

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField( default=order_number, editable=True)


    class Meta:
        ordering = ['order']

    objects = StepManager()

    def delete(self):
        last_order = Task.objects.all().order_by('order').last()
        Task.objects.move(self, last_order.order)
        super(Task, self).delete()


