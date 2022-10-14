from ctypes.wintypes import WORD
from tokenize import Number
from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta
@app.route('/dojo')
def dojo():
  return "¡Dojo!"
@app.route('/say/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def say(name):
    print(name)
    return "Hola, " + name

@app.route('/repeat/<int:number>/<word>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def repeat(number, word):
    print(word*number)
    return word * number
    #return f"{word }*{number}"

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
