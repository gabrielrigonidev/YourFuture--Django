# Generated by Django 5.1.2 on 2024-12-03 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_usuario_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foto',
            old_name='foto',
            new_name='fotos',
        ),
    ]
