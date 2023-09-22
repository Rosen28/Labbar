"""Nellie Rosén, Elina Ek, Helena Salwén
2023-09-19
DD1310: Labb3"""
import typed_input

def beräkna_aritmetrisk_summa(första_element, antal_termer, differens):
    """Beräknar den aritmetriska summan av två tal"""
    aritmetrisk_summa = antal_termer * ((första_element + (första_element + differens * (antal_termer - 1))) / 2)
    return aritmetrisk_summa

def beräkna_geometrisk_summa(första_element, antal_termer, kvot):
    """Beräknar den geometriska summan av två tal med en viss kvot"""
    geometrisk_summa = första_element*(((kvot**antal_termer) - 1)/(kvot - 1))
    return geometrisk_summa
    
def huvudprogram():
    """Tar all input till talföljderna från användaren och jämför talföljderna"""
    print("Data för den aritmetriska summan:")
    första_element_a1 = typed_input.inmatning_av_flyttal("Skriv in startvärdet: ")
    differens = typed_input.inmatning_av_flyttal("skriv in differensen: ")

    print("Data för den geometriska summan:")
    första_element_g1 = typed_input.inmatning_av_flyttal("Skriv in startvärdet: ")

    while True:
        kvot = typed_input.inmatning_av_flyttal("skriv in kvoten: ")
        if kvot != 1:
            break
        print("Då kvot = 1 blir nämnaren odefinierad. Jämförelse kan ej göras.")

    print("Antal termer i summorna:")
    while True:
        antal_termer = typed_input.inmatning_av_heltal("skriv in antal termer i följden: ")
        if antal_termer > 0:
            break
        print("Antal termer måste vara större än noll.")

    aritmetrisk_summa = beräkna_aritmetrisk_summa(första_element_a1, antal_termer, differens)
    geometrisk_summa = beräkna_geometrisk_summa(första_element_g1, antal_termer, kvot)

    if aritmetrisk_summa < geometrisk_summa:
        print("Den geometriska summan är störst.")
    elif geometrisk_summa < aritmetrisk_summa:
        print("Den aritmetriska summan är störst.")
    else:
        print("De två summorna är lika stora.")

huvudprogram()