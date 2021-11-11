import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from PIL.ExifTags import TAGS
from PIL import Image
import argparse
from PyPDF2 import PdfFileReader
import docx
import eyed3

#Extraer todos los MetaDatos de una ruta
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    return ret  
def printAllMetaImg(path, MetaPath):
    os.chdir(path)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
        	if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        		splitName = name.split(".",1)
        		oname =splitName[0]
        		fo = open(MetaPath + "\\" + name + "_Metadata.txt","w")
        		print ("[+] Metadata for file: %s " %(name))
        		try:
        			exif = get_exif_metadata(name)
        			for metadata in exif:
        				fo.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]) + "\n")
        		except:
        			import sys, traceback              
        			fo.write("No Medata were founded")
        			#traceback.print_exc(file=sys.stdout)
    fo.close()
"""
path = input("Ingresa la ruta de la carpeta estan almacenadas las imagenes: ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printAllMetaImg(path,MetaPath)
"""
def printOneMetaImg(image_path, MetaPath):
	name = os.path.basename(image_path)
	fo = open(MetaPath + "\\" + name +".txt","w")
	print ("[+] Metadata for file: %s " %(name))
	try:
		exif = get_exif_metadata(image_path)
		for metadata in exif:
			fo.write("Metadata: %s - Value: %s " %(metadata, exif[metadata]) + "\n")
	except:
		import sys, traceback              
		fo.write("No Medata were founded")
        #traceback.print_exc(file=sys.stdout)
	fo.close()
"""
image_path = input("Ingresa la ruta de la imagen: ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printOneMetaImg(path,MetaPath)
"""
def printAllMetaPDf(path,MetaPath):
    os.chdir(path)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
        	if name.lower().endswith(('.pdf')):
        		splitName = name.split(".",1)
        		oname =splitName[0]
        		fo = open(MetaPath + "\\" + oname +"_Metadata.txt","w")
        		with open(name, 'rb') as f:
        			file = PdfFileReader(f)
        			info = file.getDocumentInfo()
        			number_of_pages = file.getNumPages()       
        	fo.write("Numero de paginas: ")
        	fo.write((str(number_of_pages)) + '\n')
        	fo.write("Autor: ")
        	fo.write((str(info.author)) + '\n')
        	fo.write("Creador: ")
        	fo.write((str(info.creator)) + '\n')
        	fo.write("Productor: ")
        	fo.write((str(info.producer)) + '\n')
        	fo.write("Sujeto: ")
        	fo.write((str(info.subject)) + '\n')
        	fo.write("Titulo: ")
        	fo.write((str(info.title)) + '\n')
        	fo.close()
        	print("Los Metadatos del archivo "+ name +" si es que existen se han generado en un txt.")
"""
path = input("Ingresa la ruta de la carpeta donde estan almacenadas los pdf ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printAllMetaPDf(path,MetaPath)
"""
def printOneMetaPDf(pdf_path,MetaPath):
	name = os.path.basename(pdf_path)
	with open(pdf_path, 'rb') as f:
		file = PdfFileReader(f)
		info = file.getDocumentInfo()
		number_of_pages = file.getNumPages()
	splitName = name.split(".",1)
	oname =splitName[0]
	fo = open(MetaPath + "\\" + oname + "_Metadata.txt","w")
	fo.write("Numero de paginas: ")
	fo.write((str(number_of_pages)) + '\n')
	fo.write("Autor: ")
	fo.write((str(info.author)) + '\n')
	fo.write("Creador: ")
	fo.write((str(info.creator)) + '\n')
	fo.write("Productor: ")
	fo.write((str(info.producer)) + '\n')
	fo.write("Sujeto: ")
	fo.write((str(info.subject)) + '\n')
	fo.write("Titulo: ")
	fo.write((str(info.title)) + '\n')
	fo.close()
	print("Los Metadatos del archivo " + name + " si es que existen se han generado en un txt.")
"""
pdf_path = input("Ingresa la ruta del pdf ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printOneMetaPDf(pdf_path,MetaPath)
"""
def printOneMetaDocx(doxc_path, MetaPath):
	doc = docx.Document(doxc_path)
	prop = doc.core_properties
	name = os.path.basename(doxc_path)
	splitName = name.split(".",1)
	oname =splitName[0]
	fo = open(MetaPath + "\\" + oname + "_Metadata.txt","w")
	fo.write("author: " + (str(prop.author)+ '\n'))
	fo.write("category: " + (str(prop.category)+ '\n'))
	fo.write("modified : " + (str(prop.modified )+ '\n'))
	fo.write("created: " + (str(prop.created)+ '\n'))
	fo.write("last_modified_by: " + (str(prop.last_modified_by)+ '\n'))
	fo.write("language: " + (str(prop.language)+ '\n'))
	fo.write("modified: " + (str(prop.modified)+ '\n'))
	fo.write("subject: " + (str(prop.subject)+ '\n'))
	fo.write("title: " + (str(prop.title)+ '\n'))
	fo.write("version: " + (str(prop.version)+ '\n'))
	fo.close()
	print("El archivo con los MetaDatos a sido creado de manera exitosa")
"""
doxc_path = input("Ingresa la ruta del archivo word: ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printOneMetaDocx(doxc_path,MetaPath)
"""
def printAllMetaDocx(path,MetaPath):
	os.chdir(path)
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			if name.lower().endswith(('.docx', '.doc', '.docm')):
				doc = docx.Document(name)
				prop = doc.core_properties
				splitName = name.split(".",1)
				oname =splitName[0]
				fo = open(MetaPath + "\\" + oname + "_Metadata.txt","w")
				fo.write("author: " + (str(prop.author)+ '\n'))
				fo.write("category: " + (str(prop.category)+ '\n'))
				fo.write("modified : " + (str(prop.modified )+ '\n'))
				fo.write("created: " + (str(prop.created)+ '\n'))
				fo.write("last_modified_by: " + (str(prop.last_modified_by)+ '\n'))
				fo.write("language: " + (str(prop.language)+ '\n'))
				fo.write("modified: " + (str(prop.modified)+ '\n'))
				fo.write("subject: " + (str(prop.subject)+ '\n'))
				fo.write("title: " + (str(prop.title)+ '\n'))
				fo.write("version: " + (str(prop.version)+ '\n'))
				fo.close()
				print("El archivo con los MetaDatos a sido creado de manera exitosa")
"""
path = input("Ingresa la ruta de la carpeta con los archivos de word: ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printAllMetaDocx(path,MetaPath)
"""
def printOneMetaMp3(mp3_path, MetaPath):
	name = os.path.basename(mp3_path)
	splitName = name.split(".",1)
	oname =splitName[0]
	fo = open(MetaPath + "\\" + oname + "_Metadata.txt","w")
	audio=eyed3.load(mp3_path)
	fo.write("title: " + str(audio.tag.title) + '\n')
	fo.write("artist: " + str(audio.tag.artist) + '\n')
	fo.write("album_artist: " + str(audio.tag.album_artist) + '\n')
	fo.write("composer: " + str(audio.tag.composer) + '\n')
	fo.write("publisher: " + str(audio.tag.publisher) + '\n')
	fo.write("genre name: " + str(audio.tag.genre.name) + '\n')
	fo.close()
"""
mp3_path = input("Ingresa la ruta del archivo mp3: ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printOneMetaMp3(mp3_path,MetaPath)
"""
def printAllMetaMp3(path, MetaPath):
	os.chdir(path)
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			if name.lower().endswith('.mp3'):
				audio=eyed3.load(name)
				splitName = name.split(".",1)
				oname =splitName[0]
				fo = open(MetaPath + "\\" + oname + "_Metadata.txt","w")
				fo.write("title: " + str(audio.tag.title) + '\n')
				fo.write("artist: " + str(audio.tag.artist) + '\n')
				fo.write("album_artist: " + str(audio.tag.album_artist) + '\n')
				fo.write("composer: " + str(audio.tag.composer) + '\n')
				fo.write("publisher: " + str(audio.tag.publisher) + '\n')
				fo.close()
"""
path = input("Ingresa la ruta de la carpeta donde estan los mp3: ")
MetaPath = input("Ingresa la ruta para guardar los Metadatos: ")
printAllMetaMp3(path,MetaPath)
"""