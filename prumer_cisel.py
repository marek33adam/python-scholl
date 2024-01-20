# Výpočet průměru čísel
pocet_cisel = int(input("Zadejte počet čísel: "))
celkova_suma = 0

for i in range(pocet_cisel):
    cislo = float(input(f"Zadejte číslo {i + 1}: "))
    celkova_suma += cislo

prumer = celkova_suma / pocet_cisel

# Výpis výsledku
print(f"Průměr zadaných čísel je: {prumer}")
