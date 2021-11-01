# Generated by Django 2.2.12 on 2021-10-31 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='name')),
                ('manufacturer', models.CharField(default='', max_length=20, verbose_name='manufacturer')),
                ('amount', models.IntegerField(default=0, verbose_name='amout')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('sales', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='sales')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='', max_length=13)),
                ('birth', models.DateField(default='', verbose_name='birth')),
                ('name', models.CharField(default='', max_length=20, verbose_name='name')),
                ('gender', models.SmallIntegerField(choices=[(0, 'female'), (1, 'male'), (2, 'secrecy')])),
                ('email', models.EmailField(max_length=254)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=15, verbose_name='phone')),
                ('receiver', models.CharField(default='', max_length=20, verbose_name='receiver')),
                ('address_country', models.CharField(default='', max_length=20, verbose_name='country')),
                ('address_detailed', models.CharField(default='', max_length=20, verbose_name='address_detailed')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.User')),
            ],
        ),
        migrations.CreateModel(
            name='sharing_discounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discounting_rate', models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='discounting_rate')),
                ('helped_list', models.TextField(blank=True, null=True)),
                ('commodity_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.Commodity')),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='amount')),
                ('payment_method', models.CharField(default='', max_length=20, verbose_name='payment_method')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.Shopping_address')),
                ('commodities', models.ManyToManyField(to='shoppingWeb.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='group_buying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0, verbose_name='total_price')),
                ('discount', models.FloatField(default=0, verbose_name='discount')),
                ('commodity_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.Commodity')),
                ('participators', models.ManyToManyField(to='shoppingWeb.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', verbose_name='content')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='time')),
                ('commodity_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.User')),
                ('commodity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingWeb.Commodity')),
            ],
        ),
    ]