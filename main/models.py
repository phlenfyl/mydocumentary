from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Documentation(models.Model):
    CATEGORY_CHOICES = [
        ('API', 'API Integrations'),
        ('CHART', 'Charts'),
        ('PAG', 'Pagination Templates'),
        ('DEVOPS', 'Devops Workings'),
        ('WEB3', 'Blockchains Web3'),
    ]

    title = models.CharField(max_length=100, help_text='Title of the documentation')
    description = models.TextField(help_text='Description of the documentation', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, help_text='Category of the documentation')
    version = models.CharField(max_length=50, help_text='Version of the documentation', null=True, blank=True)
    content = models.TextField(help_text='Content of the documentation', null=True, blank=True)
    tags = models.CharField(max_length=100, help_text='Comma-separated tags of the documentation', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')
    updated_at = models.DateTimeField(auto_now=True, help_text='Date and time of last update')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Documentation'
        verbose_name_plural = 'Documentations'

