import datetime
import random
import string

from django.test import TestCase

from anagrafica.models import Delega
from anagrafica.permessi.applicazioni import PRESIDENTE
from base.utils_tests import (crea_appartenenza, crea_persona,
                              crea_persona_sede_appartenenza, crea_sede,
                              crea_utenza, crea_area_attivita, crea_partecipazione, crea_turno)


from articoli.models import Articolo, ArticoloSegmento


def parola_casuale(lunghezza):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(lunghezza))


class ArticoliTests(TestCase):

    def test_articolo(self):

        volontario, _, _ = crea_persona_sede_appartenenza()
        presidente = crea_persona()
        presidente.save()
        presidente, sede, _ = crea_persona_sede_appartenenza(presidente)
        delega_presidente_in_corso = Delega(
            persona=presidente,
            tipo=PRESIDENTE,
            oggetto=sede,
            inizio=datetime.datetime.now() - datetime.timedelta(days=5),
            fine=datetime.datetime.now() + datetime.timedelta(days=5)
        )
        delega_presidente_in_corso.save()


        articolo = Articolo.objects.create(
                titolo='Titolo 1',
                corpo=parola_casuale(3000),
                data_inizio_pubblicazione=datetime.datetime.now() - datetime.timedelta(days=5),
            )


        self.assertEqual(articolo.corpo[:Articolo.DIMENSIONE_ESTRATTO], articolo.estratto)
        self.assertFalse(articolo.termina)

        articolo2 = Articolo.objects.create(
                titolo='Titolo 2',
                corpo='Testo random',
                estratto='estratto qualsiasi',
                data_inizio_pubblicazione=datetime.datetime.now() - datetime.timedelta(days=5),
                data_fine_pubblicazione=datetime.datetime.now() + datetime.timedelta(days=5),
                stato=Articolo.PUBBLICATO
            )

        segmento_presidenti_no_filtri = ArticoloSegmento.objects.create(
            segmento='I',
            articolo=articolo2,
        )

        self.assertNotEqual(articolo2.corpo, articolo2.estratto)
        self.assertEqual(articolo2.estratto, 'estratto qualsiasi')
        self.assertTrue(articolo2.termina)

        articolo3 = Articolo.objects.create(
                titolo='Titolo 3',
                corpo='Testo qualsiasi',
                estratto='estratto random',
                data_inizio_pubblicazione=datetime.datetime.now() - datetime.timedelta(days=5),
                stato=Articolo.PUBBLICATO
            )

        segmento_volontari_no_filtri = ArticoloSegmento.objects.create(
            segmento='B',
            articolo=articolo3
        )

        articolo4 = Articolo.objects.create(
                titolo='Titolo 4',
                corpo='Testo qualsiasi 2',
                estratto='estratto random 2',
                data_inizio_pubblicazione=datetime.datetime.now() - datetime.timedelta(days=5),
                data_fine_pubblicazione=datetime.datetime.now() - datetime.timedelta(days=2),
                stato=Articolo.PUBBLICATO
            )

        pubblicati = Articolo.objects.pubblicati()
        bozze = Articolo.objects.bozze()
        self.assertEqual(pubblicati.count(), 2)
        self.assertEqual(bozze.count(), 1)
        self.assertIn(articolo, bozze)
        self.assertNotIn(articolo, pubblicati)
        self.assertNotIn(articolo2, bozze)
        self.assertIn(articolo2, pubblicati)
        self.assertNotIn(articolo3, bozze)
        self.assertIn(articolo3, pubblicati)
        self.assertNotIn(articolo4, bozze)
        self.assertNotIn(articolo4, pubblicati)

        segmenti_volontario = ArticoloSegmento.objects.all().filtra_per_segmenti(volontario)
        articoli_volontario = segmenti_volontario.oggetti_collegati()
        self.assertNotIn(articolo2, articoli_volontario)
        self.assertIn(articolo3, articoli_volontario)

        segmenti_presidente = ArticoloSegmento.objects.all().filtra_per_segmenti(presidente)
        articoli_presidente = segmenti_presidente.oggetti_collegati()
        self.assertIn(articolo2, articoli_presidente)
        self.assertIn(articolo3, articoli_presidente)
