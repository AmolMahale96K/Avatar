# Generated by Django 5.1.2 on 2024-11-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_name', models.CharField(max_length=100)),
                ('shoe_type', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='collection/Image/Shoe/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Hair',
        ),
        migrations.DeleteModel(
            name='Shoes',
        ),
        migrations.AddField(
            model_name='pant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='collection/Image/Pant/'),
        ),
        migrations.AddField(
            model_name='shirt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='collection/Image/Shirt/'),
        ),
        migrations.AlterField(
            model_name='pant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pant',
            name='pant_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='shirt_type',
            field=models.CharField(max_length=100),
        ),
    ]
