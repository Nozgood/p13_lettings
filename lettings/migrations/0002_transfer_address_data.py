# Generated by Django 3.0 on 2024-06-03 13:38

from django.db import migrations


def transfer_address_data(apps, schema_editor):
    try:
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
    except LookupError:
        return
    NewAddress = apps.get_model('lettings', 'Address')

    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_address_data),
    ]
