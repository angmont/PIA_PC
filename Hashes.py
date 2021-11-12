import hashlib
import sys

def sha512(name,path):
	fo = open("hashed_sha512.txt","a")
	file_obj = open (path, "rb")
	file = file_obj.read()
	#Aplicamos el algoritmo hash sha-256 y lo asignamos a la variable Hash
	Hash = hashlib.sha512(file)
	#Regresamos el algoritmo en cadena hexadicimal
	Hashed = Hash.hexdigest()
	#Escribimos en el archivo resultado el nombre del archivo y enseguida su clave HASH
	fo.write(name + " - " + Hashed + "\n")
#Cerramos el archivo
	fo.close()
	#print("Las claves se han guardado exitosamente en el archivo de resultado")

def sha256(name,path):
	fo = open("hashed_sh256.txt","a")
	file_obj = open (path, "rb")
	file = file_obj.read()
	#Aplicamos el algoritmo hash sha-256 y lo asignamos a la variable Hash
	Hash = hashlib.sha256(file)
	#Regresamos el algoritmo en cadena hexadicimal
	Hashed = Hash.hexdigest()
	#Escribimos en el archivo resultado el nombre del archivo y enseguida su clave HASH
	fo.write(name + " - " + Hashed + "\n")
	#Cerramos el archivo
	fo.close()
	#print("Las claves se han guardado exitosamente en el archivo de resultado")

def md5(name,path):
	fo = open("hashed_md5.txt","a")
	file_obj = open (path, "rb")
	file = file_obj.read()
	#Aplicamos el algoritmo hash sha-256 y lo asignamos a la variable Hash
	Hash = hashlib.md5(file)
	#Regresamos el algoritmo en cadena hexadicimal
	Hashed = Hash.hexdigest()
	#Escribimos en el archivo resultado el nombre del archivo y enseguida su clave HASH
	fo.write(name + " - " + Hashed + "\n")
	#Cerramos el archivo
	fo.close()
	#print("Las claves se han guardado exitosamente en el archivo de resultado")

sha512(sys.argv[2], sys.argv[1])