# coding=utf-8
from collections import OrderedDict

__author__ = 'alfioemanuele'

# Tipologie di applicativi esistenti

PRESIDENTE = 'PR'
UFFICIO_SOCI = 'US'
UFFICIO_SOCI_UNITA = 'UU'
UFFICIO_SOCI_TEMPORANEO = 'UT'
DELEGATO_AREA = 'DA'
DELEGATO_OBIETTIVO_1 = 'O1'
DELEGATO_OBIETTIVO_2 = 'O2'
DELEGATO_OBIETTIVO_3 = 'O3'
DELEGATO_OBIETTIVO_4 = 'O4'
DELEGATO_OBIETTIVO_5 = 'O5'
DELEGATO_OBIETTIVO_6 = 'O6'
RESPONSABILE_AREA = 'RA'
REFERENTE = 'RE'
REFERENTE_GRUPPO = 'GR'
DELEGATO_CO = 'CO'
RESPONSABILE_FORMAZIONE = 'RF'
RESPONSABILE_AUTOPARCO = 'AP'
RESPONSABILE_PATENTI = 'PA'
RESPONSABILE_DONAZIONI = 'DO'
DIRETTORE_CORSO = 'DC'

# Nomi assegnati
PERMESSI_NOMI = (
    (PRESIDENTE,                "Presidente"),
    (UFFICIO_SOCI,              "Ufficio Soci"),
    (UFFICIO_SOCI_UNITA,        "Ufficio Soci Unità Territoriale"),
#    (UFFICIO_SOCI_TEMPORANEO,   "Ufficio Soci Temporaneo"),
    (DELEGATO_AREA,             "Delegato d'Area"),
    (DELEGATO_OBIETTIVO_1,      "Delegato Obiettivo I (Salute)"),
    (DELEGATO_OBIETTIVO_2,      "Delegato Obiettivo II (Sociale)"),
    (DELEGATO_OBIETTIVO_3,      "Delegato Obiettivo III (Emergenze)"),
    (DELEGATO_OBIETTIVO_4,      "Delegato Obiettivo IV (Principi)"),
    (DELEGATO_OBIETTIVO_5,      "Delegato Obiettivo V (Giovani)"),
    (DELEGATO_OBIETTIVO_6,      "Delegato Obiettivo VI (Sviluppo)"),
    (RESPONSABILE_AREA,         "Responsabile d'Area"),
    (REFERENTE,                 "Referente Attività"),
    (REFERENTE_GRUPPO,          "Referente Gruppo"),
    (DELEGATO_CO,               "Delegato Centrale Operativa"),
    (RESPONSABILE_FORMAZIONE,   "Responsabile Formazione"),
    (DIRETTORE_CORSO,           "Direttore Corso"),
    (RESPONSABILE_AUTOPARCO,    "Responsabile Autoparco"),
    #(RESPONSABILE_PATENTI,      "Responsabile Patenti"),
    #(RESPONSABILE_DONAZIONI,    "Responsabile Donazioni Sangue"),
)

DELEGHE_RUBRICA = (
    PRESIDENTE, UFFICIO_SOCI, UFFICIO_SOCI_UNITA,
    DELEGATO_OBIETTIVO_1, DELEGATO_OBIETTIVO_2, DELEGATO_OBIETTIVO_3,
    DELEGATO_OBIETTIVO_4, DELEGATO_OBIETTIVO_5, DELEGATO_OBIETTIVO_6,
    RESPONSABILE_FORMAZIONE, DELEGATO_CO, RESPONSABILE_AUTOPARCO,
)

PERMESSI_NOMI_DICT = dict(PERMESSI_NOMI)

DELEGHE_INFORMAZIONI = OrderedDict((
    ('presidenti', (PRESIDENTE, 'Presidenti')),
    ('delegati_us', (UFFICIO_SOCI, 'Delegati Ufficio Soci')),
    ('delegati_us_unita', (UFFICIO_SOCI_UNITA, 'Delegati Ufficio Soci Unità Territoriale')),
    ('delegati_area', (DELEGATO_AREA, 'Delegati Ufficio Soci Unità Territoriale')),
    ('delegati_obiettivo_1', (DELEGATO_OBIETTIVO_1, 'Delegati Obiettivo I (Salute)')),
    ('delegati_obiettivo_2', (DELEGATO_OBIETTIVO_2, 'Delegati Obiettivo II (Sociale)')),
    ('delegati_obiettivo_3', (DELEGATO_OBIETTIVO_3, 'Delegati Obiettivo III (Emergenze)')),
    ('delegati_obiettivo_4', (DELEGATO_OBIETTIVO_4, 'Delegati Obiettivo IV (Principi)')),
    ('delegati_obiettivo_6', (DELEGATO_OBIETTIVO_6, 'Delegati Obiettivo VI (Sviluppo)')),
    ('responsabili_area', (RESPONSABILE_AREA, 'Responsabili d\'Area')),
    ('referenti_attivita', (REFERENTE, 'Referenti Attività')),
    ('referenti_gruppi', (REFERENTE, 'Referenti Gruppi')),
    ('centrali_operative', (DELEGATO_CO, 'Referenti Centrale Operativa')),
    ('responsabili_formazione', (RESPONSABILE_FORMAZIONE, 'Referenti Responsabili Formazione')),
    ('direttori_corsi', (DIRETTORE_CORSO, 'Direttori Corsi')),
    ('responsabili_autoparco', (RESPONSABILE_AUTOPARCO, 'Responsabili Autoparco')),
    ('giovani', (DELEGATO_OBIETTIVO_5, 'Giovani')),
))
