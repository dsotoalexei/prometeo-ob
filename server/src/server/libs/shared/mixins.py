from django.db import models


class AuditMixin(models.Model):
    """A class that provides method implementations for reuse by multiple related child classes"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True
