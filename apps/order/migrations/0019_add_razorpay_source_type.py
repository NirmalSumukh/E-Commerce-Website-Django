from django.db import migrations

def add_razorpay_source_type(apps, schema_editor):
    """
    Adds the 'Razorpay' SourceType to the database.
    """
    SourceType = apps.get_model('payment', 'SourceType')
    SourceType.objects.get_or_create(code='razorpay', defaults={'name': 'Razorpay'})

def remove_razorpay_source_type(apps, schema_editor):
    """
    Reverses the migration, deleting the SourceType.
    """
    SourceType = apps.get_model('payment', 'SourceType')
    SourceType.objects.filter(code='razorpay').delete()

class Migration(migrations.Migration):

    # This migration depends on the creation of the SourceType model
    # in Oscar's core payment app.
    dependencies = [
        ('payment', '0001_initial'),
        ('order', '0018_alter_line_num_allocated'), # Replace with the actual previous migration file name
    ]

    operations = [
        # This tells Django to run our custom function.
        migrations.RunPython(add_razorpay_source_type, remove_razorpay_source_type),
    ]