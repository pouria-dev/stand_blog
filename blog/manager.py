from django.db import models


class Model_Manager(models.Manager):  # New manager for custom queryset
    def counter(self):
        return len(self.all())

    def get_queryset(self):
        return super().get_queryset().filter(status=True)
        # This method can be overridden to customize the base_queryset   
        # For example, you can add additional filters or annotations here


