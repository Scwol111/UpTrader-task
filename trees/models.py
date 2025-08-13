from django.db import models

# Create your models here.

class MenuItem(models.Model):
    """Menu items of all
    """
    name = models.TextField(null=False)
    parent = models.ForeignKey('self', related_name='childs',
                               on_delete=models.CASCADE,
                               null=True, default=None, blank=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'parent'], name='unique_displaysment') ]
    