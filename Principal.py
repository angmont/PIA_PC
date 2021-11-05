import NoPrincipal
import Correos_Modulo
import argparse

if __name__ == "__main__":
  description= ("Este script realiza una gran diversa cantidad de tareas " +
  "las cuales son las siguientes: realizar cifrados, obtener metadata, " +
  "escaneo de puertos, envio de correos y ")
  parser = argparse.ArgumentParser(description="PIA", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-tarea", metavar='TAREA', dest="tarea", choices=['cifrar','correos'] , help='Se elige la tarea a realizar', required=True)
  parser.add_argument("-modo", metavar='MODO', dest="modo", choices=['cifmensaje', 'desmensaje', 'cifgithub', 'desgithub'] , help='Si desea utilizar la tarea de cifrado/descifrado, es necesario especificiar el modo')
  parser.add_argument("-mensaje", metavar='MENSAJE', dest="mensaje", type=str, help='Se debe poner un mensaje el cual se quiera cifrar o descifrar.')
  parser.add_argument("-llave", metavar='LLAVE', dest="llave", type=int, help='Se utiliza para saber a base de cual llave se cifra o descifra el mensaje')
  parser.add_argument("-usuario", metavar='USUARIO', dest="usuario", type=str, help='Es un argumento necesario para la funcion de cifrar los resultados obtenidos de la API de Github')
  parser.add_argument("-ruta", metavar='RUTA', dest="ruta", type=str, help='Ruta necesaria para el txt que se va a descifrar')
  parser.add_argument('-remitente', type=str , help='Correo del que se enviará el mensaje.')
  parser.add_argument('-destinatario', type=str , help='Correo que recibirá el mensaje.')
  parser.add_argument('-dominio', type=str , help='Dominio a investigar.')
  parser.add_argument('-mensaje', type=str, help='Se debe poner un mensaje el cual se quiera enviar.',default = "Hola mundo mundial")
  parser.add_argument('-asunto', type=str, help='Se utiliza para poner el titulo que tendrá el correo.', default="Hola!")
  params = parser.parse_args()
try: 
    tarea = (params.tarea)
except Exception as e:
    print(e)
    exit

if tarea == 'cifrar':
    try:
        modo = (params.modo)
        llave = (params.llave)
        if (modo == 'cifmensaje') or (modo == 'desmensaje'):
            mensaje = (params.mensaje)
            if modo == 'cifmensaje':
                print(NoPrincipal.cifrar_mensaje(mensaje, llave))
            else:
                print(NoPrincipal.descifrar_mensaje(mensaje, llave))

        elif modo == 'cifgithub':
            print('hola')
            usuario = (params.usuario)
            NoPrincipal.cifrar_github(usuario, llave)
        else:
            ruta = (params.ruta)
            NoPrincipal.descifrar_github(ruta, llave)
    except Exception as e:
        print(e)
        exit
if tarea == 'correos':
    try:
        Remitente = (params.remitente)
        Destinatario = (params.destinatario)
        Mensaje = (params.mensaje)
        Asunto = (params.asunto)
        password = getpass.getpass("Ingrese su contraseña: ")
        apikey = getpass.getpass("Ingresa tu API key: ")
        hunter = PyHunter(apikey)
        orga = (params.dominio)

        datosEncontrados = Busqueda(orga)
        if datosEncontrados is None:
            exit()
        else:
            GuardarInformacion(datosEncontrados, orga)
     except Exception as e:
        print(e)
        exit
        
