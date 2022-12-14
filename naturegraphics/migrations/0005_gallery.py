# Generated by Django 4.1 on 2022-09-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturegraphics', '0004_rename_project_image_portfolio_portfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default='1')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('gallery_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]
