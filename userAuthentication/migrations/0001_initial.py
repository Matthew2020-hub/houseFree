# Generated by Django 3.2.10 on 2022-02-07 21:45

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import userAuthentication.models
import userAuthentication.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('entry', models.CharField(choices=[('Tenant', 'Tenant'), ('Agent', 'Agent')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='Last Name')),
                ('home_address', models.CharField(max_length=30, null=True, verbose_name='Home Address')),
                ('balance', models.FloatField(default=0, validators=[userAuthentication.validators.minimum_amount])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', models.CharField(max_length=14, null=True, unique=True, verbose_name='phone number')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', userAuthentication.models.CustomUserManager()),
            ],
        ),
    ]
