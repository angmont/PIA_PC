#Socket para revisar puertos 
#Ayuda, se me habia olvidado el github JAJSJA SOS

#import Socket

def checoPuertos(dominio)
    resultado = socket.gethostbyname_ex(dominio)
    
    print("el host es" + resultado)
