# Generated by Django 5.1.2 on 2024-12-03 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_foto_foto_fotos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foto',
            old_name='fotos',
            new_name='foto',
        ),
    ]
