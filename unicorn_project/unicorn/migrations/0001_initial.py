# Generated by Django 4.0.4 on 2022-05-06 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.TextField(default='https://www.komar.de/en/media/catalog/product/cache/5/image/9df78eab33525d08d6e5fb8d27136e95/S/H/SHX8-133_1568286487.jpg', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GriefStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('help', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', models.TextField(default='https://img.freepik.com/free-vector/silhouette-unicorn-hologram-gradient-background_1048-12923.jpg?w=2000', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.TextField()),
                ('grief_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grief_stage', to='unicorn.griefstage')),
            ],
        ),
        migrations.CreateModel(
            name='GriefImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='unicorn.griefstage')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(max_length=2000)),
                ('content', models.TextField()),
                ('upvotes', models.PositiveIntegerField()),
                ('comments', models.TextField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community', to='unicorn.community')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_creator', to='unicorn.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='unicorn.user')),
            ],
        ),
        migrations.CreateModel(
            name='DirectMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sent_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_from', to='unicorn.user')),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_to', to='unicorn.user')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='unicorn.user'),
        ),
        migrations.AddField(
            model_name='community',
            name='grief_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_grief_stage', to='unicorn.griefstage'),
        ),
        migrations.AddField(
            model_name='community',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='unicorn.user'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('upvotes', models.PositiveIntegerField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='unicorn.user')),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to='unicorn.discussion')),
            ],
        ),
    ]
