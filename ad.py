import funciones
x = int(input("Que desea hacer: 1 Sumar 2 resta 3 multiplicar"))
print("Parametro a")
a = int(input())
print("Parametro b")
b = int(input())
print("Parametro c")
c = int(input())
if x == 1:
   print("Suma")
   print(funciones.suma(a,b))
if x == 2:
   print("Resta")
   print(funciones.resta(c,d))
if x == 3:
   print("Multiplicar")
   print(funciones.multiplicar(b,d))

