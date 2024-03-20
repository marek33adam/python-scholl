
cisla = input("Zadejte seznam čísel oddělených mezerou: ").split()


cisla = [int(cislo) for cislo in cisla]


nejvetsi_cislo = max(cisla)


print("Největší číslo ze zadaného seznamu je:", nejvetsi_cislo)
