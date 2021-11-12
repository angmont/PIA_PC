from bs4 import *
import requests 
import os 
from googlesearch import search
import re

# esta variable contiene el paramentro o consulta de busqueda
def busqueda_google(busqueda):
    # ahora ejecutamos la busqueda con la funcion search y pasamos como parametro la consulta
    results = search(busqueda)
    # hacemos un recorrido de los resultados, cada resultado es una URL
    for ra in results:
        print(ra)




def download_images(url):  
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser') 
    images = soup.findAll('img') 
    try: 
        folder_name = input("Nombre de la Carpeta Donde Desea Guardar Las Imagenes:- ")
        os.mkdir(folder_name) 
  
    except: 
        print("Ya existe esa carpeta!") 
        folder_create()
    
    count = 0
    print(f"{len(images)} Imagenes encontradas!") 
    
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
            print("Imagenes Descargadas!") 

        else: 
            print(f"Total {count} Images Downloaded Out of {len(images)}") 




def descargar_pdfs(url):  
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




def find_mails(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Pagina no encontrada!")
        exit()

    regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

    new_emails = set(re.findall(regExMail, response.text, re.I))

    name = input("Ingresa el nombre del archivo (sin el .txt): ")
    fo = open(name + ".txt", "w")
    c = 0
    for i in new_emails:
        c += 1
        fo.write(i)
        fo.write("\n")

