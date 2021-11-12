from bs4 import *
import requests 
import os 
from googlesearch import search
import re
import logging

# esta variable contiene el paramentro o consulta de busqueda
def busqueda_google(busqueda):
    logging.info("Entro en la función busqueda_google" )
    # ahora ejecutamos la busqueda con la funcion search y pasamos como parametro la consulta
    logging.info("Los resultados son: ")
    results = search(busqueda)
    # hacemos un recorrido de los resultados, cada resultado es una URL
    for ra in results:
        logging.info(ra)
        print(ra)




def download_images(url):
    loggin.info("Entra a la función downloads_images" )
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser') 
    images = soup.findAll('img') 
    try:
        folder_name = input("Nombre de la Carpeta Donde Desea Guardar Las Imagenes:- ")
        os.mkdir(folder_name) 
        logging.info("Nombre de la Carpeta Donde Desea Guardar Las Imagenes:- ")
        logging.info(folder_name)
    except:
        logging.error("Ya existe esta carpeta")
        print("Ya existe esa carpeta!") 
        folder_create()
    
    count = 0
    print(f"{len(images)} Imagenes encontradas!")
    logging.info(f"{len(images)} Imagenes encontradas!")
    logging.info("Iniciando descarga")
    
    if len(images) != 0: 

        for i, image in enumerate(images): 

            try: 
                image_link = image["data-srcset"] 
            except: 
                try: 
                    image_link = image["data-src"] 
                except: 
                    try: 
                        image_link = image["data-fallback-src"] 
                    except: 
                        try: 
                            image_link = image["src"] 
                        except: 
                            pass
 
            try: 
                r = requests.get(image_link).content 
                try:  
                    r = str(r, 'utf-8') 
                except UnicodeDecodeError: 
  
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f: 
                        f.write(r) 

                    count += 1
            except: 
                pass

        if count == len(images):
            logging.info("Todas las imagenes han sido descargadas")
            print("Imagenes Descargadas!") 

        else: 
            print(f"Total {count} Images Downloaded Out of {len(images)}")
            logging.info(f"Total {count} Images Downloaded Out of {len(images)}")




def descargar_pdfs(url):
    logging.info("Entra en la función descargar_pdfs" )
    response = requests.get(url)   

    soup = BeautifulSoup(response.text, 'html.parser') 

    links = soup.find_all('a')   

    i = 0
      
    for link in links: 
        if ('.pdf' in link.get('href', [])): 
            i += 1
            print("Downloading file: ", i, "...")
     
            
            response = requests.get(link.get('href')) 
      
            
            pdf = open("pdf"+str(i)+".pdf", 'wb') 
            pdf.write(response.content) 
            pdf.close() 
            print("File ", i, " Downloaded!") 
      
    print("Todos los PDF descargados!")
    logging.info("Todos los PDF descargados")



def find_mails(url):
    logging.info("Entra en la función find_emails" )
    response = requests.get(url)
    logging.info("Busca la pagina: " + url)
    if response.status_code != 200:
        logging.error("Pagina no encontrada")
        print("Pagina no encontrada!")
        exit()

    regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

    new_emails = set(re.findall(regExMail, response.text, re.I))
    logging.info("emails encontrados: " + new_emails)

    name = input("Ingresa el nombre del archivo (sin el .txt): ")
    logging.info("El nombre del archivo será: " + name)
    fo = open(name + ".txt", "w")
    logging.info("Abre el archivo: " + name + ".txt")
    c = 0
    for i in new_emails:
        c += 1
        fo.write(i)
        logging.info("Escribiendo el email... " + i + " en: " + name + ".txt")
        fo.write("\n")
        logging.info("Finalizado")
