def spocitej_samohlasky(text):
    samohlasky = "aeiouAEIOU"
    pocet = 0
    for znak in text:
        if znak in samohlasky:
            pocet += 1
    return pocet

vstupni_text = input("Zadejte text: ")
pocet_samohlaskek = spocitej_samohlasky(vstupni_text)
print("Počet samohlásek v textu je:", pocet_samohlaskek)
