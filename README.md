# PIA_PC

_Documentaci贸n para el PIA de Programaci贸n en ciberseguridad_
![alt text](https://www.mejorconweb.com/images/programacion-web-barcelona.jpg)

## Comenzando 馃殌

_Este programa esta hecho con el prop贸sito de realizar tareas para ciberseguridad, tales como: escaneo de puertos, webscraping, env铆o de correos, cifrado y descifrado, sacar metadata de archivos, entre otros._

### Pre-requisitos 馃搵

_Se requiere tener instalado python en su versi贸n de 3.9 y tambien los siguientes m贸dulos de manera manual:_

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

_O simplemente se puede clonar 茅ste repositorio y realizar:_
```
pip install -r requirements.txt 
```

### Instalaci贸n 馃敡

_Escriba lo siguiente en su terminal_

```
git clone https://github.com/angmont/PIA_PC.git
```
Se puede clonar desde windows con git bash o git desktop


_Recuerde instalar los m贸dulos_

```
pip install -r requirements.txt
```

## Aclaraciones
_Argumentos para cada tarea_

**Nota**: la informaci贸n de cada argumento se encuentra en:
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



## Ejecutando el programa 鈿欙笍

_Primeramente, es necesario aclarar la tarea a usar con el argumento "-t"_
```
py main.py -t dns
```
_Ya de ah铆, se puede ir elegiendo cualquiera de las tareas previamente mencionadas:_

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

## Construido con 馃洜锔?


* [Python](https://www.python.org/) - Lenguaje de programaci贸n
* [Powershell](https://docs.microsoft.com/en-us/powershell/?view=powershell-7.2) - Automatizador de tareas multiplataforma

## Versionado 馃搶

Usamos [Python](https://www.python.org/) para el versionado. Para la versi贸n 3.9.

## Autores 鉁掞笍

_Los autores de 茅ste script son:_

* **脕ngela Montoya** - [angmont](https://github.com/angmont)
* **Dariela Hurtado** - [DariHT8](https://github.com/DariHT8)
* **Ian Leija** - [ianisra](https://github.com/ianisra)
* **E-manuel Manzanarez** - [EmanuelManzanarez](https://github.com/EmanuelManzanarez)
* **Emiliano Leal** - [EmilianoLeal13](https://github.com/EmilianoLeal13)

## Licencia 馃搫

Este proyecto est谩 bajo la Licencia MIT Lincense - mira el archivo [LICENSE](LICENSE) para detalles
