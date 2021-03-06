# Generated by Django 2.2.1 on 2019-05-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=100)),
                ('bpub_date', models.DateTimeField(db_column='pub_date')),
                ('bread', models.IntegerField()),
                ('bcommet', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.BooleanField(default=True)),
                ('hcontent', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete='on_delete=models.CASCADE', to='booktest.BookInfo')),
            ],
        ),
    ]
