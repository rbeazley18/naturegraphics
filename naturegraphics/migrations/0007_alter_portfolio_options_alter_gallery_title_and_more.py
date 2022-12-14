# Generated by Django 4.1 on 2022-09-19 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturegraphics', '0006_alter_gallery_gallery_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Our Projects'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='Title', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='Title', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project1',
            name='category',
            field=models.CharField(default='Category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project2',
            name='category',
            field=models.CharField(default='Category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project3',
            name='category',
            field=models.CharField(default='Category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project4',
            name='category',
            field=models.CharField(default='Category', max_length=255, null=True),
        ),
    ]
