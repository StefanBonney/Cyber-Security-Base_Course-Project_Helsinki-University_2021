# Generated by Django 4.0 on 2021-12-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinMiner', '0003_rename_votes_mineamount_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiningTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_text', models.CharField(max_length=200)),
                ('amount_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]