import requests
import logging

def cifrar_mensaje(mensaje, key):
  universo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
  logging.info("Nuestro universo es: " + universo)
  logging.info("Cifrando mensaje...")
  
  translated = ''

  for symbol in mensaje:
    if symbol in universo:
        symbolIndex = universo.find(symbol)
        translatedIndex = symbolIndex + key
        
        if translatedIndex >= len(universo):
            translatedIndex = translatedIndex - len(universo)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(universo)

        translated = translated + universo[translatedIndex]
    else:
        translated = translated + symbol

  logging.info(translated)        
  return(translated)


def descifrar_mensaje(mensaje, key):
 universo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
 logging.info("Nuestro universo es: " + universo)
 logging.info("Descifrando mensaje...")

 translated = ''


 for symbol in mensaje:
    if symbol in universo:
        symbolIndex = universo.find(symbol)
        translatedIndex = symbolIndex - key
        
        if translatedIndex >= len(universo):
            translatedIndex = translatedIndex - len(universo)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(universo)

        translated = translated + universo[translatedIndex]
    else:
        translated = translated + symbol

 logging.info(translated)
 return(translated)

def cifrar_github(usuario, clave):
  logging.info("Estamos en cifrar_github")
  i = 0
  try:
    urlrepos = "https://api.github.com/users/" + usuario + "/repos"
    nombre = usuario
    resp1 = requests.get(urlrepos)
    dic1 = (resp1.json())
    if len(dic1) == 0:
      return None
    try:
      if dic1['message'] == 'Not Found':
        print (dic1['message'])
        return (dic1['message'])
    except:
      pass
    escritura = open(nombre + "_cifgithub.txt", "a")
    for element in dic1:
      i = i + 1
      adios =("Repositorio " + str(i) + "\n\n")
      titulo = cifrar_mensaje(adios, clave)
      escritura.write(titulo)
      for key in element:
        hello = (str(key) + " = " + str(element[key]) + "\n")
        msj2 = cifrar_mensaje(hello, clave)
        escritura.write(msj2)
      escritura.write("\n\n")
    print('Hecho!')
    logging.info("Hecho!")
    escritura.close()
  except Exception as e:
    logging.error(str(e))
    print(e)

def descifrar_txt(path, clave):

  logging.info("Descifrando un txt")
  nom = path.split('/')
  nomb = nom[len(nom)-1]
  nombr = path.split('.txt')
  nombre =  nombr[0]
  lectura = open(path, "r")
  escritura = open(nombre + "_descifrado.txt", "a")
  for linea in lectura:
    mensaje = descifrar_mensaje(linea, clave)
    escritura.write(mensaje)
    logging.info(mensaje)
  print("Hecho!")
  logging.info("Hecho!")
  escritura.close()
  lectura.close()

def cifrar_txt(path, clave):

  logging.info("Cifrando un txt")
  lectura = open(path, "r")
  nom = path.split('/')
  nomb = nom[len(nom)-1]
  nombr = path.split('.txt')
  nombre =  nombr[0]
  escritura = open(nombre + "_cifrado.txt", "a")
  for linea in lectura:
    mensaje = cifrar_mensaje(linea, clave)
    logging.info(mensaje)
    escritura.write(mensaje)
  print("Hecho!")
  logging.info("Hecho!")
  escritura.close()
  lectura.close()
