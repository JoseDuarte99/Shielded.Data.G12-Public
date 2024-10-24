# Generated by Django 5.1.1 on 2024-10-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_tags_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='post',
            field=models.ManyToManyField(to='post.post'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
