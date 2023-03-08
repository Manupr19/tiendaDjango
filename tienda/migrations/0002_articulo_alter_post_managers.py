# Generated by Django 4.1.5 on 2023-03-08 09:39

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('pvp', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagen', models.ImageField(blank=True, upload_to='articulos/')),
            ],
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
