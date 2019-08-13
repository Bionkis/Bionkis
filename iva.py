def ingresaproducto():
    NB = ''
    NB = input('Nombre Producto:')
    return NB

def ingresacantidad():
    CT = 0
    CT = input('Cantidad:')
    return CT

def ingresaprecio():
    PR = 0
    PR = input('Precio:')
    return PR

def pregunta():
    X = ''
    X = input('Desea Continuar (S/N):')
    return X

tabla = []
i = 0
subtotal = 0
t = 0
iva = 0.13
while (i < 5):
    producto = ingresaproducto()
    cantidad = float(ingresacantidad())
    precio   = float(ingresaprecio())
    if pregunta() == "N":
       break
    i += 1
    t = (cantidad * precio)
    subtotal = subtotal + t
    
total = (subtotal * iva)
print(total)

