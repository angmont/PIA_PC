# PIA_PC

_Documentación para el PIA de Programación en ciberseguridad_
![alt text](https://www.mejorconweb.com/images/programacion-web-barcelona.jpg)

## Comenzando 🚀

_Este programa esta hecho con el propósito de realizar tareas para ciberseguridad, tales como: escaneo de puertos, webscraping, envío de correos, cifrado y descifrado, sacar metadata de archivos, entre otros._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Se requiere tener instalado python en su versión de 3.9 y tambien los siguientes módulos de manera manual:_

```
pip install python_docx
```
```
pip install requests
```
```
pip install pyhunter
```
```
pip install openpyxl
```
```
pip install tqdm
```
```
pip install googlesearch_python
```
```
pip install beautifulsoup4
```
```
pip install eyed3
```
```
pip install Pillow
```
```
pip install PyPDF2
```

_O simplemente se puede clonar éste repositorio y realizar:_
```
pip install -r requirements.txt 
```

### Instalación 🔧

_Escriba lo siguiente en su terminal_

```
git clone https://github.com/angmont/PIA_PC.git
```
Se puede clonar desde windows con git bash o git desktop


_Recuerde instalar los módulos_

```
pip install -r requirements.txt
```

## Aclaraciones
_Argumentos para cada tarea_

Nota: la información de cada argumento se encuentra en:
```
py main.py -h
```


### Cifrar

-m (cifgithub / cifmensaje / destxt / ciftxt / desmensaje)

-msj Necesario para la funcion (cifmensaje / desmensaje)

-key Necesario para todos

-user Necesario para la funcion cifgithub

-ru Necesario para (ciftxt / destxt)

### Envio de correos
-rem

-des

-url

-cont

-asu

_Todos son necesarios para la tarea_

_Se debe tener en cuenta que el remitente debe ser un correo con cuenta de **Microsoft**_

### Puertos
-ip

-ports

_Todos son necesarios para la tarea_

### Metadata
-a (imagen / imagenes / pdf / pdfs / word / words / mp3 / mp3s)

-mp 

-ru

_Todos son necesarios para la tarea_

### Web Scraping

-m (busqueda / emails / pdf / img)

-url Necesario para (emails / pdf / img)

-bus Necesario para busqueda



## Ejecutando el programa ⚙️

_Primeramente, es necesario aclarar la tarea a usar con el argumento "-t"_
```
py main.py -t dns
```
_Ya de ahí, se puede ir elegiendo cualquiera de las tareas previamente mencionadas:_

Ejemplos para las otras funciones
```
py main.py -t cifrar -m ciftxt -ru C:\User\user\Path -key 3
```
```
py main.py -t web -m busqueda -bus chips
```
```
py main.py -t metadata -a imagen -ru C:\Users\user\Path\hacia\archivo -mp C:\Users\user\Path\a\guardar
```
```
py main.py -t correos -rem tucorreo@microsoft.com -des sucorreo@(gmail/hotmail/outlook).com -url uanl.mx -cont "Hola a Todos" -asu "Ejemplo"
```
```
py main.py -t puertos -ip 111.111.111.11 -ports 80,50
```
```
py main.py -t hash
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️


* [Python](https://www.python.org/) - Lenguaje de programación
* [Powershell](https://docs.microsoft.com/en-us/powershell/?view=powershell-7.2) - Automatizador de tareas multiplataforma

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.


## Versionado 📌

Usamos [Python](https://www.python.org/) para el versionado. Para la versión 3.9.

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Ángela Montoya** - [angmont](https://github.com/angmont)
* **Dariela Hurtado** - [DariHT8](https://github.com/DariHT8)
* **Ian Leija** - [ianisra](https://github.com/ianisra)
* **E-mmanuel Manzanarez** - [EmanuelManzanarez](https://github.com/EmanuelManzanarez)
* **Emiliano Leal** - [DariHT8](https://github.com/DariHT8)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE](LICENSE) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
