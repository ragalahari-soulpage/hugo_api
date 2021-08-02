# Generated by Django 3.2.3 on 2021-06-22 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hugo.db.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_field_operator', models.BooleanField(default=False)),
                ('is_qc', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=256, null=True)),
                ('token_status', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'Users',
            },
            managers=[
                ('objects', hugo.db.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=255)),
                ('degree', models.CharField(blank=True, max_length=255)),
                ('specialization', models.CharField(blank=True, max_length=255)),
                ('institution', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education',
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=10)),
                ('last_name', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('blood_group', models.CharField(blank=True, max_length=255)),
                ('aadhar_number', models.CharField(blank=True, max_length=12)),
                ('pan_number', models.CharField(blank=True, max_length=10)),
                ('permanent_address', models.TextField(blank=True)),
                ('current_address', models.TextField(blank=True)),
                ('personal_email', models.EmailField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=10, unique=True)),
                ('alternate_phone', models.CharField(blank=True, max_length=10)),
                ('emergency_contact_person', models.CharField(blank=True, max_length=255)),
                ('emergency_contact_number', models.CharField(blank=True, max_length=10)),
                ('emp_id', models.CharField(blank=True, max_length=10)),
                ('date_of_joined', models.DateField(blank=True, null=True)),
                ('last_working_date', models.DateField(blank=True, null=True)),
                ('device_serial_number', models.CharField(blank=True, max_length=255)),
                ('reporting', models.CharField(blank=True, max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255)),
                ('division', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('intern_name', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Internship',
                'verbose_name_plural': 'Internship',
                'db_table': 'internship',
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=256, null=True)),
                ('account_no', models.CharField(blank=True, max_length=256, null=True)),
                ('ctc_no', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Salary',
                'verbose_name_plural': 'Salary',
                'db_table': 'saalary',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=10, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.employee')),
            ],
            options={
                'verbose_name': 'Employment',
                'verbose_name_plural': 'Employment',
                'db_table': 'employment',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('docs', models.FileField(upload_to='docs')),
                ('employment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.employment')),
            ],
            options={
                'verbose_name': 'EmployeeDocs',
                'verbose_name_plural': 'EmployeeDocs',
                'db_table': 'employeedocs',
            },
        ),
        migrations.CreateModel(
            name='EducationDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('docs', models.FileField(upload_to='docs')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.education')),
            ],
            options={
                'verbose_name': 'EducationDocs',
                'verbose_name_plural': 'EduactionDocs',
                'db_table': 'educationdocs',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.employee'),
        ),
    ]
