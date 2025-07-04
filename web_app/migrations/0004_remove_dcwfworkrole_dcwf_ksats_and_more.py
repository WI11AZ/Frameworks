# Generated by Django 5.1.6 on 2025-03-02 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0003_remove_dcwfksat_ncwf_2017_ksats_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dcwfworkrole",
            name="dcwf_ksats",
        ),
        migrations.AlterField(
            model_name="dcwfksat",
            name="ncwf_2017_ksat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dcwf_ksats",
                to="web_app.ncwf2017ksat",
            ),
        ),
    ]
