from django.db import models
from django.contrib.postgres.fields import JSONField
from users.models import CustomUser


class Document(models.Model):
    SOURCE_CHOICE = (
        ('a', 'A'),
        ('b', 'B'),
    )

    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='exports'
    )
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    source_type = models.CharField(
        choices=SOURCE_CHOICE, blank=True, null=True, max_length=20
    )
    source_id = models.CharField(blank=True, null=True, max_length=50)
    input_meta_data = JSONField(default=dict, null=True, blank=True)
