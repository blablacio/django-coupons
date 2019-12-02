from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0008_auto_20190214_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='Arbitrary coupon value', max_digits=10),
        ),
    ]
