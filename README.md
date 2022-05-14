## PIA PROGRAMACION PARA CIBERSEGURIDAD

1. Instalar requirements.txt
2. Correr "python PIA.py -h"

### Correr PIA.py

El programa debe ejecutarse por medio de la termial ubicado en la carpeta del programa usando el codigo dependiendo de la funcion a utilizar
Los modulos que se pueden usar son: vtreport, metadata, ROT13, nmap, hunter, menu
Los modulos deben de escribirse correctamente para ser reconocidos

Por medio del comando 'python PIA.py -opt menu' se depliega un menu en la terminal para facilitar el uso de los Modulos

### Modulo Hunter

Comando: python PIA.py -opt hunter -a ___apikey___ -c ___compañia___ -n ___numero de correos___
	-a	la API key de tu usario
	-c	el nombre de la compañia objetivo
	-n	el numero de correos que deseas extraer

Es necesario teer una api key propia para ejecutar el modulo

### Modulo VTReport

Comando: python PIA.py -opt vtreport -a ___apikey___ -t ___target___ -r ___resultados___
	-a	la API key de tu usario
	-t	La ruta del objetivo
	-r	la ruta para los resultados
	-pre	Si tienes cuenta premium se agrega con el valor 'y', en caso contrario no es necesario agregarlo

Es necesario tener tu api key de virustotal

### Modulo Metadata

Comando: python PIA.py -opt metadata -p ___ruta___
	-p	es la ruta de la carpeta con las fotos

EL modulo solo funciona para imagenes

### Modulo ROT13

Comando: python PIA.py -opt cipher 
	-de	Este argumento se debe agregar para desencriptar seguido del mensaje que se quiere desencriptar
	-en	Este argumento se debe agregar para encriptar seguido del mensaje que se quiere encriptar
	
Es necesario agregar solo uno de los argumentos

### Modulo Nmap
Comando: PIA.py -opt nmap -ip ___ip___ -in ___inicio___ -fi ___fin___
	-ip	Es la ip objetivo
	-in	El puerto en el que iniciar el escaneo
	-fi	El puerto en el que terminar el escaneo