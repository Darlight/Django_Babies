from django.db import models

# Create your models here.
class Baby(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'parents.Parent',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Parent: {}'.format(self.parent.name)
