# Generated by Django 4.2.5 on 2023-09-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas1', '0006_delete_login_usuario_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=50)),
            ],
        ),
    ]
