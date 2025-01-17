# Generated by Django 3.2.8 on 2021-11-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingWeb', '0010_auto_20211118_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='item_recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_ID', models.IntegerField(default=0, verbose_name='commodity ID')),
                ('commodity_recommended', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user_recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='user ID')),
                ('user_recommended', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.IntegerField(default=0, verbose_name='user ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commodity_ID',
            field=models.IntegerField(verbose_name='commodity_ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=' ', verbose_name='content'),
        ),
    ]
