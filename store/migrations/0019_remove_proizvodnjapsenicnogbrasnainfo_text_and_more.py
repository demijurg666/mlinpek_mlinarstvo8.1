# Generated by Django 4.0 on 2022-11-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_proizvodnjapsenicnogbrasnainfo_sadrzaj_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text',
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text1',
            field=models.TextField(blank=True, max_length=999999, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text2',
            field=models.TextField(blank=True, max_length=999998, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text3',
            field=models.TextField(blank=True, max_length=999997, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text4',
            field=models.TextField(blank=True, max_length=999996, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text5',
            field=models.TextField(blank=True, max_length=999995, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text6',
            field=models.TextField(blank=True, max_length=999994, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text7',
            field=models.TextField(blank=True, max_length=999993, null=True),
        ),
        migrations.AddField(
            model_name='proizvodnjapsenicnogbrasnainfo',
            name='text8',
            field=models.TextField(blank=True, max_length=999992, null=True),
        ),
    ]
