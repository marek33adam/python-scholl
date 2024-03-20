#Proměnné, které jsou vytvořeny mimo funkci, jsou známé jako globální proměnné.
#Globální proměnné může používat každý, uvnitř funkcí i mimo ně.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Pokud uvnitř funkce vytvoříte proměnnou se stejným názvem, bude tato proměnná lokální a lze ji použít pouze uvnitř funkce.
#Globální proměnná se stejným názvem zůstane tak, jak byla, globální a s původní hodnotou.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

