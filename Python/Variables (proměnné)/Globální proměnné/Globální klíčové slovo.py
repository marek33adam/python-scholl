#Normálně, když vytvoříte proměnnou uvnitř funkce, je tato proměnná lokální a lze ji použít pouze uvnitř této funkce.
#Chcete-li vytvořit globální proměnnou uvnitř funkce, můžete použít klíčové slovo global.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Klíčové slovo global použijte také v případě, že chcete změnit globální proměnnou uvnitř funkce.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)