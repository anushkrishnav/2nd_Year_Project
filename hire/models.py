from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
import uuid

class Job(models.Model):
    title = models.CharField(max_length= 250)
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(null = True)
    requirement = models.TextField(null = True)
    workCondition = models.TextField(null = True)
    posted = models.DateField(null = True, auto_now_add=True)
    category = models.CharField(max_length= 255, default='uncategorised')
    snippet = models.CharField(max_length= 255)
    header_image = models.ImageField(null=True, blank=True, upload_to='job_images/')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length= 250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    experience = models.TextField()

    created_by = models.ForeignKey(CustomUser, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job) + str(" - ") + str(self.first_name) + str(" ") + str(self.last_name)

class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField(null = True)

    created_by = models.ForeignKey(CustomUser, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class Type(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='type', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def get_absolute_url(self):
        return reverse('shop:products_by_type', args=[self.id])
    
    def __str__(self):
        return self.name
