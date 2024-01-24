import random

# Generování náhodného čísla mezi 1 a 10
tajne_cislo = random.randint(1, 10)

# Vstup od uživatele
tip = int(input("Hádej číslo mezi 1 a 10: "))

# Kontrola, zda je tip správný
if tip == tajne_cislo:
    print("Skvělé, uhádl(a) jsi to!")
else:
    print(f"Bohužel, tajné číslo bylo {tajne_cislo}. Zkus to znovu!")
1