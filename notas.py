def ingresanombre():
    NB = ''
    NB = input('Nombre Alumno:')
    return NB

def ingresanota():
    NT = 0
    NT = input('Nota Alumno:')
    return NT

def pregunta():
    X = ''
    X = input('Desea Continuar (S/N):')
    return X

tabla = []
i = 0
while (i < 5):
    Nombre = ingresanombre()
    Nota = ingresanota()
    tabla.append({Nombre,Nota})
    if pregunta() == "N":
       break
    i += 1
    
for n in tabla:
    print(n)
