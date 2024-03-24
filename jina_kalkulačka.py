def scitani(a, b):
    return a + b

def odcitani(a, b):
    return a - b

def nasobeni(a, b):
    return a * b

def deleni(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b

print("Vítejte v jednoduché kalkulačce!")

cislo1 = float(input("Zadejte první číslo: "))
cislo2 = float(input("Zadejte druhé číslo: "))

print("Vyberte operaci:")
print("1. Sčítání")
print("2. Odčítání")
print("3. Násobení")
print("4. Dělení")

volba = input("Zadejte číslo operace (1/2/3/4): ")

if volba in ('1', '2', '3', '4'):
    if volba == '1':
        print("Výsledek sčítání je:", scitani(cislo1, cislo2))
    elif volba == '2':
        print("Výsledek odčítání je:", odcitani(cislo1, cislo2))
    elif volba == '3':
        print("Výsledek násobení je:", nasobeni(cislo1, cislo2))
    elif volba == '4':
        print("Výsledek dělení je:", deleni(cislo1, cislo2))
else:
    print("Neplatná volba.")
