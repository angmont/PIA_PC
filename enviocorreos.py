import smtplib
import ssl
import getpass
import logging

from pyhunter import PyHunter
from openpyxl import Workbook
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Busqueda(organizacion):

    apikey = getpass.getpass("Ingresa tu API key: ")
    logging.info("Se agrego la API KEY")
    hunter = PyHunter(apikey)
    resultado = hunter.domain_search(company=organizacion, limit=1,
                                     emails_type='personal')
    return resultado


def GuardarInformacion(datosEncontrados, organizacion, remitente, destinatario, asunto, mensaje):
    libro = Workbook()
    hoja = libro.active
    hoja["A1"] = "Dominio"
    hoja["B1"] = "Organizacion"
    hoja["C1"] = "Pais"
    hoja["D1"] = "Email"
    hoja["E1"] = "Tipo de Email"
    hoja["F1"] = "Nombre"
    hoja["G1"] = "Apellido"
    
    hoja["A2"] = datosEncontrados['domain']
    hoja["B2"] = datosEncontrados['organization']
    hoja["C2"] = datosEncontrados['country']

    
    Email = datosEncontrados['emails']
    diccionarioEmail = Email[0]
    hoja["D2"] = diccionarioEmail["value"]
    hoja["E2"] = diccionarioEmail["type"]
    hoja["F2"] = diccionarioEmail['first_name']
    hoja["G2"] = diccionarioEmail['last_name']
    archivo = "Hunter"+organizacion+".xlsx"
    logging.info(archivo)
    libro.save(archivo)


    email_msg = MIMEMultipart("alternative")
    email_msg["From"] = remitente
    email_msg["To"] = destinatario
    email_msg["Subject"] = asunto

    email_msg.attach(MIMEText(mensaje, "plain"))

    
    filename = archivo   
    with open(filename, "rb") as attachment:
    
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
 
    encoders.encode_base64(part)


    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )


    email_msg.attach(part)

    password = getpass.getpass("Ingrese su contraseña: ")
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        try:
            print("[+] Conectando con el Servidor de Correo.")
            logging.info("Conectando con el servidor")
            print("[+] Iniciando Encriptación de Sesión.")
            logging.info("Iniciando encriptación de sesion")
            server.starttls(context=context)
            print("[+] Iniciando Sesión en el Servidor de Correo.")
            logging.info("Iniciando sesion")
            server.login(remitente, password)
            print("[+] Enviando Correo.")
            logging.info("Enviando correo")
            server.sendmail(
            remitente, destinatario, email_msg.as_string()
            )
            print("[+] Correo Electrónico Enviado con Éxito a: %s" % (destinatario))
            logging.info("Correo electronico enviado con exito")
        except:
            print("[-] Error al Enviar el Correo.")
            logging.error("Error al enviar el correo.")
