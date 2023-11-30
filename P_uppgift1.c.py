"""Nellie Rosén, DD1310
178: Periodiska systemet
2023-12-01"""
import random

class Atom:
    """Klass som beskriver atomer med attributen atomnummer (int),
    atombeteckning (str) och atomvikt (float)"""
    def __init__(self, atomnummer, atombeteckning, atomvikt):
        """Konstruktorn som anropas när vi skapar en atom.
        Parametrar: atomnummer (int), atombeteckning (str) och atomvikt (float)"""
        self.atomnummer = atomnummer
        self.atombeteckning = atombeteckning
        self.atomvikt = float(atomvikt)

    def __str__(self):
        """Returnernar en sträng som skriver ut atomernas information"""
        return f"{self.atomnummer} {self.atombeteckning} {self.atomvikt}"
    
    def __lt__(self, other):
        """Jämförelse mellan atomernas atomvikt (används för att sortera)"""
        return self.atomvikt < other.atomvikt

    def byt_plats_på_ämnen(self, periodiska_systemet, atomslag_1, atomslag_2):
        """Byter plats på två ämnen i listan med alla grundämnen(atomer)
        Parametrar: self, periodiska systemet (lista), ämne 1 (index) och ämne 2 (index)
        Returnerar: periodiska systemet (Uppdaterade listan)"""
        periodiska_systemet[atomslag_1], periodiska_systemet[atomslag_2] = periodiska_systemet[atomslag_2], periodiska_systemet[atomslag_1]
        return periodiska_systemet

def läs_in_fil():
    """Läser in fil med all atomdata, delar upp datan till rätt kategorier 
    och skapar en lista med Atom-objekt. Sedan sorteras listan efter atomvikten.
    Returnerar: Periodiska systemet (Lista)"""
    periodiska_systemet = []
    with open("periodiska_systemet.txt", "r", encoding="utf-8") as fil:
        for rad in fil:
            atombeteckning, atomvikt = rad.strip().split()
            atom = Atom(None, atombeteckning, atomvikt)
            periodiska_systemet.append(atom)
    periodiska_systemet.sort()

    return periodiska_systemet

def applicera_specialfall():
    """Byter plats på de ämnen i listan som inte följer atomvikten.
    Returnerar: Periodiska systemet (Uppdaterad lista)"""
    periodiska_systemet = läs_in_fil()
    atom = Atom(None, None, 0)
    atom.byt_plats_på_ämnen(periodiska_systemet, 17, 18)  # Ar mot K
    atom.byt_plats_på_ämnen(periodiska_systemet, 26, 27)  # Co mot Ni
    atom.byt_plats_på_ämnen(periodiska_systemet, 51, 52)  # Te mot I
    atom.byt_plats_på_ämnen(periodiska_systemet, 89, 90)  # Th mot Pa
    atom.byt_plats_på_ämnen(periodiska_systemet, 91, 92)  # U mot Np

    return periodiska_systemet

def ge_atomer_atomnummer():
    """Ger atomer atomnummer baserat på deras ordning i listan periodiska systemet
    Returnerar: Periodiska systemet (lista med atomnummer)"""
    periodiska_systemet = applicera_specialfall()
    räknare = 1
    for atom in periodiska_systemet:
        atom.atomnummer = räknare
        räknare += 1

    return periodiska_systemet

def slumpa_atomer():
    """Slumpar fram en atom från listan med atomer
    Returnerar: En slumpmässigt vald atom från listan periodiska systemet"""
    periodiska_systemet = ge_atomer_atomnummer()
    slumpad_atom = random.choice(periodiska_systemet)
    return slumpad_atom

def skriv_ut_alla_atomer():
    """Skriver ut informationen om alla atomer som finns i listan"""
    atomer = ge_atomer_atomnummer()
    for atom in atomer:
        print(atom)

def träna_atomnummer():
    """Funktion där användaren kan träna på atomnummer. En atombeteckning slumpas
    och användaren har tre försök på sig att gissa motsvarande nummer innan det avslöjas."""
    slumpad_atom = slumpa_atomer()
    for svar in range(3):
        try:
            svar = int(input(f"Vilket atomnummer har {slumpad_atom.atombeteckning}? "))
        except ValueError:
            print("Felaktig inmatning. Ange ett heltal.")

        if svar == slumpad_atom.atomnummer:
            print("Rätt svar!")
            return
        print("Fel svar, försök igen.")

    print(f"Tyvärr, du har använt dina tre försök. Rätt svar var {slumpad_atom.atomnummer}.")

def träna_atombeteckning():
    """Funktion där användaren kan träna på atombeteckningar. Ett atomnummer slumpas
    och användaren har tre försök på sig att gissa motsvarande beteckning innan det avslöjas."""
    slumpad_atom = slumpa_atomer()
    for svar in range(3):
        try:
            svar = str(input(f"Vilken atombeteckning har atomslaget med atomnumret {slumpad_atom.atomnummer}? "))
        except ValueError:
            print("Felaktig inmatning. Försök igen!")

        if svar == slumpad_atom.atombeteckning:
            print("Rätt svar!")
            return
        print("Fel svar, försök igen.")

    print(f"Tyvärr, du har använt dina tre försök. Rätt svar var {slumpad_atom.atombeteckning}.")

def träna_atomvikt():
    """Funktion där användaren kan träna på atomvikter. Tre atomvikter slumpas, 
    där bara en tillhör motsvarande atombeteckningen. Användaren får tre frågor"""
    for svar in range(3):
        slumpad_atom = slumpa_atomer()

        try:
            slumpat_alternativ_1 = slumpa_atomer().atomvikt
            slumpat_alternativ_2 = slumpa_atomer().atomvikt
            print(f"Vad är {slumpad_atom.atombeteckning}:s atomvikt?")
            svar = float(input(f"Är det 1. {slumpat_alternativ_1}, 2. {slumpad_atom.atomvikt} eller 3. {slumpat_alternativ_2}? "))
        except ValueError:
            print("Felaktig inmatning. Svara med atomvikten!")

        if svar == slumpad_atom.atomvikt:
            print("Rätt svar!")
            continue
        print(f"Tyvärr, fel svar. Rätt svar var {slumpad_atom.atomvikt}")

def huvudmeny():
    """Skriver ut menyn, läser in och returnerar användaren val.
    Returnerar: val (int)"""
    meny = """
    -------------- MENY ---------------
    1. Visa alla atomer
    2. Träna på atomnummer
    3. Träna på atombeteckningar
    4. Träna på atomvikt
    5. Avsluta
    -----------------------------------"""
    print(meny)
    try:
        val = int(input("Vad vill du göra? "))
        return val
    except ValueError:
        print("Ogiltligt val. Ange ett heltal.")

def huvudprogram():
    """Huvudprogrammet som anropar menyn och hanterar inmatningen som har gjorts."""
    while True:
        val = huvudmeny()
        if 1 <= val <= 5:
            if val == 1:
                skriv_ut_alla_atomer()
            elif val == 2:
                träna_atomnummer()
            elif val == 3:
                träna_atombeteckning()
            elif val == 4:
                träna_atomvikt()
            elif val == 5:
                print("Tack för denna gången!")
        else:
            print("Ogiltigt val. Ange en siffra mellan 1 och 5.")
huvudprogram()