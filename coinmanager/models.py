from django.db import models

import uuid

class ScrapingTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_id = models.UUIDField()
    coin = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.coin} - {self.status}'

