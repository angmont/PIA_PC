import requests

def cifrar_mensaje(mensaje, key):
  universo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

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

  return(translated)


def descifrar_mensaje(mensaje, key):
 universo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

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

 return(translated)

def cifrar_github(usuario, clave):
  i = 0
  try:
    urlrepos = "https://api.github.com/users/" + usuario + "/repos"
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
    escritura = open("cifgithub.txt", "a")
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
    escritura.close()
  except Exception as e:
    print(e)

def descifrar_github(path, clave):

  lectura = open(path, "r")
  escritura = open("desgithub.txt", "a")
  for linea in lectura:
    mensaje = descifrar_mensaje(linea, clave)
    escritura.write(mensaje)
  print("Hecho!")
  escritura.close()
  lectura.close()