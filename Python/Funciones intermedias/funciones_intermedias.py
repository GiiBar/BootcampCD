from wsgiref.validate import validator


x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x[1])

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0])

#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes['fútbol'])

#Cambia el valor 20 en z a 30.
z[0]['y'] = 30
print(z[0])

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(data_entrada):
    for iterador in data_entrada:
        valor = list(iterador.items())
        print(valor[0][0], " - ", valor[0][1], ",", valor [1][0], " - ", valor[1][1])

iterateDictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterateDictionary2(data_entrada):
    for iterador in data_entrada:
        valor = list(iterador.items())
        print(valor[0][1])

iterateDictionary2(estudiantes)

def iterateDictionary3(data_entrada):
    for iterador in data_entrada:
        valor = list(iterador.items())
        print(valor[1][1])
        
iterateDictionary3(estudiantes)

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(data_entrada):
    for iterador in data_entrada:
        x = list(dojo.values())
        print(len(dojo["ubicaciones"]), "UBICACIONES")
        print(x[0])
        print(len(dojo["instructores"]), "INSTRUCTORES")
        print(x[1])
        return

printInfo(dojo)
