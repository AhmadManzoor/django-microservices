# Generated by Django 2.2.24 on 2021-12-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
            options={
                'unique_together': {('user_id', 'product_id')},
            },
        ),
    ]
