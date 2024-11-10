from django.db import models
from django.core.validators import RegexValidator

class CollaborateRequest(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\s-]*$',
                message='Name can only contain letters, spaces, and hyphens'
            )
        ]
    )
    email = models.EmailField()
    message = models.TextField(
        max_length=1000,
        help_text='Maximum 1000 characters'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
