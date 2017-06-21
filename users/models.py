from django.db import models

from django.utils import timezone

# Create your models here.
class User(models.Model):

    created = models.DateTimeField(default=timezone.now())

    modified = models.DateTimeField(default=timezone.now())
    
    title = models.CharField(max_length=256, blank=False, null=False)

    language = models.CharField(max_length=256, blank=False, null=False)

    snippet = models.CharField(max_length=10000, blank=False, null=False)

    description = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        """ Sensible string representation of a user."""
        return "{0} {1} | {2} | {3}".format(self.title, self.language, 
                self.snippet, self.description)

    def save(self, *args, **kwargs):
        """ Add created_at and updated_at timestamps. """
        if not self.id:
            self.created = timezone.now()

        self.modified = timezone.now()

        return super(User, self).save(*args, **kwargs)

