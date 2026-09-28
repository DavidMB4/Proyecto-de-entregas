from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("entregas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cobro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("monto", models.DecimalField(decimal_places=2, max_digits=10)),
                ("estado", models.CharField(default="Aprobado", max_length=20)),
                ("fecha_cobro", models.DateTimeField(auto_now_add=True)),
                (
                    "pedido",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cobro",
                        to="entregas.pedido",
                    ),
                ),
            ],
        ),
    ]
