total_distancia = 0
nombreStr = input('ingresar nombre ->')
numero_escala = int(input('ingresar numero de escala ->'))

for escala in range(numero_escala):
    distance = int(input('ingresa la distancia de las escalas ->'))
    total_distancia += distance

print('nombre: ', nombreStr)
print('la distancia total es -> ', total_distancia)
print('el numero de escala es -> ', numero_escala)

