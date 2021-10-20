# Generated by Django 3.2.6 on 2021-10-20 15:30

from django.db import migrations, transaction

from task_manager.models import PRIORITY, STATUS


def init_data(apps, schema_editor):
    Tag = apps.get_model('task_manager', 'Tag')
    Task = apps.get_model('task_manager', 'Task')

    with transaction.atomic():
        Tag.objects.bulk_create([
            Tag(name='Тестове'),
            Tag(name='Пустий Тег'),
            Tag(name='Ще один Пустий Тег')
        ])
        tasks = Task.objects.bulk_create([
            Task(title='List/detail for Tags', description='List/detail for Tags', priority=PRIORITY.HIGH, status=STATUS.IN_PROGRESS),
            Task(title='List/detail for Tasks', description='List/detail for Tasks', priority=PRIORITY.HIGH, status=STATUS.IN_PROGRESS),
            Task(title='Filters for Tags', description='Filters for Tags', priority=PRIORITY.MEDIUM, status=STATUS.BACKLOG),
            Task(title='Filter for Tasks', description='Filter for Tasks', priority=PRIORITY.MEDIUM, status=STATUS.BACKLOG),
            Task(title='Create/edit for Tags', description='Create/edit for Tags', priority=PRIORITY.LOW, status=STATUS.BACKLOG),
            Task(title='Create/edit for Tasks', description='Create/edit for Tasks', priority=PRIORITY.LOW, status=STATUS.BACKLOG),
        ])


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_data),
        migrations.RunSQL("""INSERT INTO task_manager_task_tags (tag_id, task_id) VALUES (1,1), (1,2), (1,3), (1,4), (1,5), (1,6)""")
    ]