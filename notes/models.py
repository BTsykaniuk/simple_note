from django.db import models
import re


class Note(models.Model):
    message = models.TextField(verbose_name='Notes')
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    unique_words = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        cleaned_message = re.sub('[^a-zA-Z0-9]+', ' ', self.message)
        self.unique_words = len(set(cleaned_message.split()))

        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return f'Message - {self.created_date.strftime("%Y-%m-%d %H.%M")}'
