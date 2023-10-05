"""Nellie Rosén, Elina Ek, Helena Salwén
2023-09-19
DD1310: Labb3"""

class Student:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __str__(self):
            return "Namn: "+ self.förnamn + " " + self.efternamn + " " + "Personnummer: " + self.personnummer

class Skola:
    def __init__(self):
        self.studenter = []

    def addera_ny_student(self, student):
        self.studenter.append(student)


def inmatning_av_ny_student():
    while True:
        förnamn = input("Vad är studentens förnamn? ")
        efternamn = input("Vad är studentens efternamn? ")
        personnummer = input("Vad är studentens personnummer? ")

        if personnummer.isdigit():
            return Student(förnamn, efternamn, personnummer)
        else:
            print("Personnumret får bara innehålla siffror, försök igen!")


def huvudprogram():
    skola = Skola()

    while len(skola.studenter) < 3:
        print("Information om studenten: ")
        student = inmatning_av_ny_student()
        skola.addera_ny_student(student)
        print("Studenten är tillagd!")

    print("Här är alla studenter på KTH:")
    for student in skola.studenter:
        print(student)

huvudprogram()
