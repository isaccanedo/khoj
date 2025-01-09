# Generated by Django 4.2.7 on 2024-01-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0025_searchmodelconfig_embeddings_inference_endpoint_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="searchmodelconfig",
            name="cross_encoder_inference_endpoint",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="searchmodelconfig",
            name="cross_encoder_inference_endpoint_api_key",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
