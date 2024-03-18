import random
import string

def generuj_heslo(delka):
    heslo = ''.join(random.choices(string.ascii_letters + string.digits, k=delka))
    return heslo

delka_hesla = int(input("Zadejte délku hesla: "))
nove_heslo = generuj_heslo(delka_hesla)
print("Vygenerované heslo:", nove_heslo)
