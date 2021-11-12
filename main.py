import subprocess
import cifrado
import Correos_Modulo
import socketpuertos
import MetaDataPIA
import webscraping
import argparse
import os, time
import logging 

logging.basicConfig(filename='app.log', level=logging.INFO)

if __name__ == "__main__":
  description= ("Este script realiza una gran diversa cantidad de tareas " +
  "las cuales son las siguientes: realizar cifrados, obtener metadata, " +
  "escaneo de puertos, envio de correos y ")
  parser = argparse.ArgumentParser(description="PIA", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument("-t", metavar='TAREA', dest="tarea", choices=['cifrar','correos', 'dns', 'puertos', 'metadata', 'web', 'hash'] , help='Se elige la tarea a realizar', required=True)
  parser.add_argument("-m", metavar='MODO', dest="modo", 
  choices=['cifmensaje', 'desmensaje', 'cifgithub', 'destxt', 'ciftxt', 'busqueda', 'emails', 'pdf', 'img'] , help='Si desea utilizar la tarea de cifrado o de web scraping, es necesario especificiar el modo')
  parser.add_argument("-msj", metavar='MENSAJE', dest="mensaje", type=str, help='Se debe poner un mensaje el cual se quiera cifrar o descifrar.')
  parser.add_argument("-key", metavar='LLAVE', dest="llave", type=int, help='Se utiliza para saber a base de cual llave se cifra o descifra el mensaje')
  parser.add_argument("-user", metavar='USUARIO', dest="usuario", type=str, help='Es un argumento necesario para la funcion de cifrar los resultados obtenidos de la API de Github')
  parser.add_argument("-ru", metavar='RUTA', dest="ruta", type=str, help='Ruta necesaria para el txt que se va a descifrar o donde se encuentran los arctivos pata la funcion de metadata')
  parser.add_argument("-rem", metavar='REMITENTE', dest="remitente", type=str, help='Correo del que se enviará el mensaje.')
  parser.add_argument("-des", metavar='DESTINATARIO', dest="destinatario", type=str, help='Correo que recibirá el mensaje.')
  parser.add_argument("-url", metavar= 'URL', dest="dominio", type=str, help='Url a investigar.')
  parser.add_argument("-cont", metavar='CONTENIDO', dest="contenido", type=str, help='Se debe poner un mensaje el cual se quiera enviar.', default="Hola mundo mundial")
  parser.add_argument("-asu", metavar='ASUNTO', dest="asunto", type=str, help='Se utiliza para poner el titulo que tendrá el correo.', default="Hola!")
  parser.add_argument("-ip", metavar='IP', dest="ip", type=str, help='Se debe introducir la ip a consultar, solo el ID de red.', default="172.217.15.")
  parser.add_argument("-ports", metavar='PUERTOS', dest="puertos", help='Introduce los puertos a revisar separados por una coma [80,800]', default= "80,800")
  parser.add_argument("-a", metavar='ARCHIVO', dest="archivo", choices=['imagen', 'imagenes', 'pdf', 'pdfs', 'word', 'words', 'mp3', 'mp3s'] , help='Si desea utilizar la tarea de sacar la metadata, es necesario especificiar el tipo de archivo')
  parser.add_argument("-mp", metavar= 'METAPATH', dest="metapath", type=str, help='Ruta donde se guardarán los metadatas encontrados.')
  parser.add_argument("-bus", metavar='BUSQUEDA', dest="busqueda", type=str, help='Busqueda para realizar en google')
  params = parser.parse_args()
try:
    logging.info("Se escogió la tarea: ")
    logging.info(params.tarea)
    tarea = (params.tarea)
except Exception as e:
    logging.error("Ocurrió un error: " + str(e))
    print(e)
    exit

try:
    if tarea == 'cifrar':

        modo = (params.modo)
        llave = (params.llave)

        if (modo == 'cifmensaje') or (modo == 'desmensaje'):
            mensaje = (params.mensaje)
            if modo == 'cifmensaje':
                print(cifrado.cifrar_mensaje(mensaje, llave))
            else:
                print(cifrado.descifrar_mensaje(mensaje, llave))

        elif modo == 'cifgithub':
            usuario = (params.usuario)
            cifrado.cifrar_github(usuario, llave)
        elif modo == 'destxt':
            ruta = (params.ruta)
            cifrado.descifrar_txt(ruta, llave)
        elif modo == 'ciftxt':
            ruta = params.ruta
            cifrado.cifrar_txt(ruta, llave)
        else:
            print('Opción no válida para cifrado')

    elif tarea == 'correos':

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

    elif tarea == 'dns':  

	    print()
	    script_p = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy', 'Unrestricted', './consulta_dns.ps1'], cwd=os.getcwd())
    
	    script_p.wait()

    elif tarea == 'metadata':

        archivo = (params.archivo)
        if (archivo == 'imagen') or (archivo == 'imagenes'):
            ruta = (params.ruta)
            metapath = (params.metapath)
            if archivo == 'imagen':
                MetaDataPIA.printOneMetaImg(ruta, metapath)
            else:
                MetaDataPIA.printAllMetaImg(ruta, metapath)
        elif (archivo == 'pdf') or (archivo == 'pdfs'):
            ruta = (params.ruta)
            metapath = (params.metapath)
            if archivo == 'pdf':
                MetaDataPIA.printOneMetaPDf(ruta, metapath)
            else:
                MetaDataPIA.printAllMetaPDf(ruta, metapath)
        elif (archivo == 'word') or (archivo == 'words'):
            ruta = (params.ruta)
            metapath = (params.metapath)
            if archivo == 'word':
                MetaDataPIA.printOneMetaDocx(ruta, metapath)
            else:
                MetaDataPIA.printAllMetaDocx(ruta, metapath)
        else:
            ruta = (params.ruta)
            metapath = (params.metapath)
            if archivo == 'mp3':
                MetaDataPIA.printOneMetaMp3(ruta, metapath)
            else:
                MetaDataPIA.printAllMetaMp3(ruta, metapath)

    elif tarea == 'puertos':	

      logging.info("Se introdujo la ip: ")
      ip = params.ip
      logging.info(ip)
      print("Se revisará la ip: " + ip)

      logging.info("Se escanearan los puertos: ")
      puertoss = params.puertos
      logging.info(puertoss)
      portlist = params.puertos.split(',')
      for i in range (len(portlist)):
        print("Con los puertos: " + portlist[i])
        portlist[i] = int(portlist[i])
		
      socketpuertos.checoPuertos(ip, portlist, puertoss)


    elif tarea == 'web':

        logging.info("Con el modo: ")
        modo = params.modo
        logging.info(modo)
        if modo == 'emails' or modo == 'pdf' or modo == 'img':
            url = params.dominio
            logging.info("El dominio es: ")
            logging.info(url)
            if modo == 'emails':
                logging.info("Si el \"modo\" es: emails")
                webscraping.find_mails(url)
            elif modo == 'pdf':
                logging.info("Si el \"modo\" es: pdf")
                webscraping.descargar_pdfs(url)
            else:
                logging.info("Si el \"modo\" es: img")
                webscraping.download_images(url)
        elif modo == 'busqueda':
            logging.info("Se realizara una busqueda en:")
            busqueda = params.busqueda
            logging.info(busqueda)
            webscraping.busqueda_google(busqueda)
        else:
            logging.info("Ninguna opción es valida para hacer Web Scrapping" )
            print('Opcion no válida para web scraping')
    else:

	    print()
	    script_p = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy', 'Unrestricted', './rutas.ps1'], cwd=os.getcwd())
    
	    script_p.wait()       
except Exception as e:
    logging.error("Ha ocurrido un error: " + str(e))
    print(e)
    exit
