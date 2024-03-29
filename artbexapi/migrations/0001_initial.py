# Generated by Django 4.1.6 on 2023-07-31 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtBex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=150)),
                ('type', models.CharField(blank=True, max_length=150)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='artbexapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='ArtBexImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artbex', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='artbex_image', to='artbexapi.artbex')),
                ('image', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_artbex', to='artbexapi.image')),
            ],
        ),
        migrations.AddField(
            model_name='artbex',
            name='images',
            field=models.ManyToManyField(related_name='images_of_artbex', through='artbexapi.ArtBexImage', to='artbexapi.image'),
        ),
    ]
