from unittest.mock import patch

from django.db import DatabaseError, connection
from django.test import TestCase, TransactionTestCase
from django.urls import reverse

from . import services
from .models import Cobro, Pedido


class Dia4FlujoTests(TestCase):
    def test_alta_crea_pedido_y_cobro(self):
        with self.captureOnCommitCallbacks(execute=True):
            pedido = services.registrar_pedido("Monterrey", "Guadalajara", 2.5)

        self.assertTrue(Pedido.objects.filter(id=pedido.id).exists())
        self.assertEqual(pedido.cobro.estado, "Aprobado")

    @patch("entregas.services.calcular_eta_con_ia", side_effect=TimeoutError)
    def test_si_falla_ia_el_get_del_pedido_sigue_respondiendo(self, _ia):
        with self.captureOnCommitCallbacks(execute=True):
            alta = self.client.post(
                reverse("crear_pedido"),
                {"origen": "México", "destino": "Puebla", "peso_kg": "1"},
            )

        pedido = Pedido.objects.get()
        self.assertRedirects(alta, reverse("seguimiento", args=[pedido.id]))

        respuesta = self.client.get(reverse("seguimiento", args=[pedido.id]))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Por confirmar")

    def test_seguimiento_y_reporte_reutilizan_el_mismo_servicio(self):
        with self.captureOnCommitCallbacks(execute=True):
            pedido = services.registrar_pedido("Mérida", "Cancún", 3)

        with patch("entregas.views.services.obtener_datos_pedido", wraps=services.obtener_datos_pedido) as tramite:
            self.client.get(reverse("seguimiento", args=[pedido.id]))
            self.client.get(reverse("reporte_pedido", args=[pedido.id]))

        self.assertEqual(tramite.call_count, 2)


class AtomicidadTests(TransactionTestCase):
    @patch("entregas.services.Cobro.objects.create", side_effect=DatabaseError)
    def test_si_falla_el_cobro_tambien_se_revierte_el_pedido(self, _cobro):
        with self.assertRaises(DatabaseError):
            services.registrar_pedido("Toluca", "Querétaro", 2)

        self.assertEqual(Pedido.objects.count(), 0)
        self.assertEqual(Cobro.objects.count(), 0)

    def test_el_aviso_se_hace_despues_del_commit(self):
        estados_de_transaccion = []

        def registrar_estado(_pedido_id):
            estados_de_transaccion.append(connection.in_atomic_block)

        with patch("entregas.services.avisar_repartidor", side_effect=registrar_estado) as aviso:
            services.registrar_pedido("León", "Morelia", 4)

        aviso.assert_called_once()
        self.assertEqual(estados_de_transaccion, [False])
