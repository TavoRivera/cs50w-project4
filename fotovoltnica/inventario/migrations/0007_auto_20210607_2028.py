# Generated by Django 2.2.10 on 2021-06-08 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_auto_20210607_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='capacity',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='static/images/services')),
                ('disponibility', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=128)),
                ('items', models.ManyToManyField(blank=True, related_name='items', to='inventario.Stock')),
                ('system_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='PrecioSistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('capacity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.Capacidad')),
                ('itemcost', models.ManyToManyField(blank=True, related_name='cost', to='inventario.Sistema')),
            ],
        ),
    ]
