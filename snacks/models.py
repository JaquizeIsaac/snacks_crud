from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    reviewer = models.ForeignKey(get_user_model(), related_name='reviewed_snacks', on_delete=models.CASCADE, null=True, blank=True)
    purchaser = models.ForeignKey(get_user_model(), related_name='purchased_snacks', on_delete=models.CASCADE, null=True, blank=True)
    # reviewer = models.ForeignKey(get_user_model(), related_name='reviewer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name