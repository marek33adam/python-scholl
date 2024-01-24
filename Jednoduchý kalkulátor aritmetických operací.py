def aritmeticke_operace():
    print("Vyber operaci:")
    print("1 - Sčítání")
    print("2 - Odčítání")
    print("3 - Násobení")
    print("4 - Dělení")

    volba = input("Zadej číslo operace (1-4): ")

    if volba in ['1', '2', '3', '4']:
        cislo1 = float(input("Zadej první číslo: "))
        cislo2 = float(input("Zadej druhé číslo: "))

        if volba == '1':
            vysledek = cislo1 + cislo2
            operace = "Sčítání"
        elif volba == '2':
            vysledek = cislo1 - cislo2
            operace = "Odčítání"
        elif volba == '3':
            vysledek = cislo1 * cislo2
            operace = "Násobení"
        else:
            if cislo2 != 0:
                vysledek = cislo1 / cislo2
                operace = "Dělení"
            else:
                print("Chyba: Nelze dělit nulou.")
                return

        print(f"Výsledek {operace}: {vysledek}")

    else:
        print("Chyba: Zadej číslo operace od 1 do 4.")

# Spuštění aritmetických operací
aritmeticke_operace()
