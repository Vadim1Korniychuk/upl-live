from model_utils.choices import Choices

from django.db import models

PRIORITY = Choices(
    ('LOW', 'LOW', 'Low'),
    ('MEDIUM', 'MEDIUM', 'Medium'),
    ('HIGH', 'HIGH', 'High'),
)

STATUS = Choices(
    ('BACKLOG', 'BACKLOG', 'Backlog'),
    ('IN_PROGRESS', 'IN_PROGRESS', 'In Progress'),
    ('DONE', 'DONE', 'Done'),
)


class Tag(models.Model):
    """Tag model"""

    name = models.CharField('Tag', max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Task(models.Model):
    """Task model"""

    title = models.CharField('Title', max_length=256)
    description = models.CharField('Description', max_length=512, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=64, choices=PRIORITY, default=PRIORITY.MEDIUM)
    status = models.CharField(max_length=64, choices=STATUS, default=STATUS.IN_PROGRESS)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
