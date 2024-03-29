# Generated by Django 4.0.6 on 2022-07-07 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='veiculo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='veiculos.marca'),
            preserve_default=False,
        ),
    ]
