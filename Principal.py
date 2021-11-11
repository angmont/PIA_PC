import subprocess
import NoPrincipal
import Correos_Modulo
import argparse
import os, time


if __name__ == "__main__":
  description= ("Este script realiza una gran diversa cantidad de tareas " +
  "las cuales son las siguientes: realizar cifrados, obtener metadata, " +
  "escaneo de puertos, envio de correos y ")
  parser = argparse.ArgumentParser(description="PIA", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-t", metavar='TAREA', dest="tarea", choices=['cifrar','correos', 'dns'] , help='Se elige la tarea a realizar', required=True)
  parser.add_argument("-m", metavar='MODO', dest="modo", choices=['cifmensaje', 'desmensaje', 'cifgithub', 'desgithub'] , help='Si desea utilizar la tarea de cifrado/descifrado, es necesario especificiar el modo')
  parser.add_argument("-msj", metavar='MENSAJE', dest="mensaje", type=str, help='Se debe poner un mensaje el cual se quiera cifrar o descifrar.')
  parser.add_argument("-key", metavar='LLAVE', dest="llave", type=int, help='Se utiliza para saber a base de cual llave se cifra o descifra el mensaje')
  parser.add_argument("-user", metavar='USUARIO', dest="usuario", type=str, help='Es un argumento necesario para la funcion de cifrar los resultados obtenidos de la API de Github')
  parser.add_argument("-ru", metavar='RUTA', dest="ruta", type=str, help='Ruta necesaria para el txt que se va a descifrar')
  parser.add_argument("-rem", type=str, help='Correo del que se enviará el mensaje.')
  parser.add_argument("-des", type=str, help='Correo que recibirá el mensaje.')
  parser.add_argument("-dom", type=str, help='Dominio a investigar.')
  parser.add_argument("-cont", type=str, help='Se debe poner un mensaje el cual se quiera enviar.', default="Hola mundo mundial")
  parser.add_argument("-topic", type=str, help='Se utiliza para poner el titulo que tendrá el correo.', default="Hola!")
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
            usuario = (params.usuario)
            NoPrincipal.cifrar_github(usuario, llave)
        else:
            ruta = (params.ruta)
            NoPrincipal.descifrar_github(ruta, llave)
    except Exception as e:
        print(e)
        exit
elif tarea == 'correos':
    try:
        remitente = (params.remitente)
        destinatario = (params.destinatario)
        mensaje = (params.contenido)
        asunto = (params.asunto)
        orga = (params.dominio)

        datos_encontrados = Correos_Modulo.Busqueda(orga)
        if datos_encontrados is None:
            print("No se encontró nada")
            exit()
        else:
            Correos_Modulo.GuardarInformacion(datos_encontrados, orga, remitente, destinatario, asunto, mensaje)
    except Exception as e:
        print(e)
        exit
elif tarea == 'dns':  
    try:
	    print()
	    script_p = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy', 'Unrestricted', './DNS.ps1'], cwd=os.getcwd())
    
	    script_p.wait()
    except Exception as e:
	    print(e)
