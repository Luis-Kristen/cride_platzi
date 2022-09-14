# Generated by Django 2.0.10 on 2020-05-15 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circles', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='invited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invited_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membership',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='circle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circles.Circle'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='issued_by',
            field=models.ForeignKey(help_text='Circle member that is providing the invitation', on_delete=django.db.models.deletion.CASCADE, related_name='issued_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='used_by',
            field=models.ForeignKey(help_text='User that used the code to enter the circle', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='circle',
            name='members',
            field=models.ManyToManyField(through='circles.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
