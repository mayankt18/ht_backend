# Generated by Django 3.2.7 on 2021-09-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthscore',
            name='bloodsugar',
            field=models.IntegerField(choices=[(1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Very High')], default=1),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='bmi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='cholesterol',
            field=models.IntegerField(choices=[(1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Very High')], default=1),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='creatinine',
            field=models.IntegerField(choices=[(1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Very High')], default=1),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='diabp',
            field=models.IntegerField(choices=[(1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Very High')], default=1),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='sysbp',
            field=models.IntegerField(choices=[(1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Very High')], default=1),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='healthscore',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='healthscore',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
