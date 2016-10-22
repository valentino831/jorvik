from django.contrib.contenttypes.models import ContentType

from ufficio_soci.elenchi import ElencoVistaAnagrafica, ElencoVolontariGiovani
from anagrafica.models import Persona, Delega, Sede


class ElencoDelegati(ElencoVistaAnagrafica):

    def template(self):
        return 'anagrafica_elenchi_delegati.html'

    def risultati(self):
        qs_sedi = self.args[0]
        qs_deleghe = self.kwargs['deleghe']
        me = self.kwargs['me_id']

        delegati = Persona.objects.filter(
            Delega.query_attuale(
                oggetto_tipo=ContentType.objects.get_for_model(Sede),
                oggetto_id__in=qs_sedi,
                tipo__in=qs_deleghe
            ).via("delega")
        ).exclude(pk=me).order_by('nome', 'cognome', 'codice_fiscale')\
            .distinct('nome', 'cognome', 'codice_fiscale')
        return delegati


class ElencoGiovani(ElencoVolontariGiovani):

    def risultati(self):
        me = self.kwargs['me_id']
        return super(ElencoGiovani, self).risultati().exclude(pk=me)
