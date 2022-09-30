x = 10
for contar in range(x, 0, -1):
    print(contar)

def return_print(lista):
    for i in lista:
        print(lista[0])
        return lista[1]
i= return_print([10, 22])
print (i)

def return_print(lista):
    for i in lista:
        print(lista[0])
        return len(lista)
i = return_print([10, 22, 5, 14])
print (i)

def valores_mayores_que_el_segundo(dato_entrada):
    nueva_lista = []
    contador = 0
    for iterador in dato_entrada:
        if iterador > dato_entrada[1]:
            nueva_lista.append(iterador)
            contador =+ contador
        else:
            print(iterador)
    print(contador)
    return nueva_lista

resultado = valores_mayores_que_el_segundo([5,2,3,2,1,4])
print(resultado)
