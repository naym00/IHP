# Generated by Django 2.2 on 2020-10-09 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registration', '0002_remove_registrationform_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date', models.CharField(max_length=20, verbose_name='Date')),
                ('name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Registration.RegistrationForm')),
            ],
        ),
    ]