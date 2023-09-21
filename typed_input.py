"""Modul för att kontrollera inmatning av flyttal och heltal"""

def inmatning_av_flyttal(inmatning):
    """ Felhantering av inmatningen av flyttal"""
    while True:
        try:
            inmatning = float(input(inmatning))
            return inmatning
        except ValueError:
            print("Det där var inget flyttal. Försök igen.")

def inmatning_av_heltal(inmatning):
    """Felhantering av inmatningen av heltal"""
    while True:
        try:
            inmatning = int(input(inmatning))
            return inmatning
        except ValueError:
            print("Det där var inget heltal. Försök igen.")
    