
import random

# Definujeme funkci pro generování náhodného seznamu čísel
def nahodny_seznam(delka, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(delka)]

# Nastavíme parametry generování seznamu
delka_seznamu = 10
min_cislo = 1
max_cislo = 100

# Generujeme náhodný seznam čísel
seznam = nahodny_seznam(delka_seznamu, min_cislo, max_cislo)

# Vypíšeme vygenerovaný seznam
print("Náhodný seznam čísel:", seznam)
