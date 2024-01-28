#Funkce print() v Pythonu se často používá k výstupu proměnných.
#Příklad
x = "Python is awesome"
print(x)

#Ve funkci print() vypíšete více proměnných oddělených čárkou
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Pro výstup více proměnných můžete také použít operátor +
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Všimněte si mezery za "Python" a "is", bez nich by byl výsledek "Pythonisawesome"

#U čísel funguje znak + jako matematický operátor
x = 5
y = 10
print(x + y)

#Když se ve funkci print() pokusíte zkombinovat řetězec a číslo s operátorem +, Python vám zobrazí chybu
x = 5
y = "John"
print(x + y)

#Nejlepší způsob, jak ve funkci print() vytisknout více proměnných, je oddělit je čárkami, které dokonce podporují různé datové typy
x = 5
y = "John"
print(x, y)