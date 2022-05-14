import argparse
import logging
import os
from datetime import datetime

def Main():
    help1 = "Opcion para elegir script a utilizar.  [VTReport | Metadata | \
            Rot13 | Nmap | Hunter | Menu]"
    info = 'PIA PC'

    parser = argparse.ArgumentParser(info)

    # Argumento obligatorio, establece las opciones en el menú
    parser.add_argument('-opt', '--option', required = True, help = help1,
                        dest = 'opt')

    # Argumentos requeridos para VTReport                    
    parser.add_argument('-a', '--api', help = 'Agrega tu API key.')
    parser.add_argument('-t', '--target', help = 'Ingresar direccion absoluta\
                         del directorio con los archivos')
    parser.add_argument('-r', '--result', help = 'Ingresar direccion absoluta\
                        del arhivo de salida')
    parser.add_argument('-pre', '--premium', help = 'Ingresa "y" si tienes una api\
                        premium de VirusTotal, de lo contrario ignorarlo')

    # Argumento requerido para Metadata
    parser.add_argument('-p', '--path', help = 'Ingresar direccion del path \
                        con las imagenes.')

    # Argumentos requeridos para Rot13
    parser.add_argument('-en', '--encriptar', help = 'Frase para encriptar')
    parser.add_argument('-de', '--desencriptar', help = 'Frase para desencriptar')

    # Argumentos requeridos para Nmap
    parser.add_argument('-ip', '--ip',type=str, help = 'Ingresar ip para \
                        escaneo con nmap.')
    parser.add_argument('-in', '--inicio',type=int, help = 'Primer puerto \
                        a analizar.')
    parser.add_argument('-fi', '--fin',type=int, help = 'Ultimo puerto a \
                        analizar.')

    # Argumentos requeridos para Hunter, también se requiere api
    parser.add_argument('-c', '--company', help = 'Nombre de la compañía.')
    parser.add_argument('-n', '--numero', help = 'Numero de correos (Maximo 10\
                        si tienes plan gratuito).')
    
    args = parser.parse_args()


    if args.opt.upper() == 'VTREPORT':
        api = args.api
        target = args.target
        result = args.result
        premium = args.premium
        if premium==None:
            premium = 'n'
        PSVT.getVTReport(api, target, result, premium)

    if args.opt.upper() == 'METADATA':
        path = args.path
        Metadata.PrintMeta(path)

    if args.opt.upper() == 'ROT13':
        if args.encriptar:
            frase = args.encriptar
            Rot13.Encriptar(frase)
        if args.desencriptar:
            frase = args.desencriptar
            Rot13.Desencriptar(frase)

    if args.opt.upper() == 'NMAP':
        ip = args.ip
        inicio = args.inicio
        fin = args.fin
        Nmap.Escaneo(ip,inicio,fin)

    if args.opt.upper() == 'HUNTER':
        api = args.api
        company = args.company
        numero = args.numero
        Hunter.hunter_mail(api,company,numero)
        
    if args.opt.upper() == 'MENU':
        x = '1'
        while x == '1':
            menu_art = """
            ______ _____  ___   ______  _____ 
            | ___ \_   _|/ _ \  | ___ \/  __ \\
            | |_/ / | | / /_\ \ | |_/ /| /  \/
            |  __/  | | |  _  | |  __/ | |    
            | |    _| |_| | | | | |    | \__/\\
            \_|    \___/\_| |_/ \_|     \____/
                                
                                
            """
            print(menu_art)
            print('\t[1] Virus Total Report\n\t[2] Metadata\n\t[3] Rot 13\n\t[4] Nmap\n\t[5] Hunter\n\n\t[0] Salir\n\t')
            option = input('PIA PC> ')
            if option == '1':
                while True:
                    try:
                        api = input('Ingrese la api: ')
                        if api == '0':
                            break
                        target = input('Ingrese la dirección de los archivos objetivo: ')
                        if target == '0':
                            break
                        result = input('Ingrese la dirección del archivo de salida: ')
                        if result == '0':
                            break
                        premium = input('Ingrese "y" si tiene premium, de lo contrario, presione enter: ')
                        if premium=='':
                            premium = 'n'
                        elif premium == '0':
                            break
                        PSVT.getVTReport(api, target, result, premium)
                        break
                    except Exception as e:
                        print('Error:', e)
                        print('Ingrese los datos correctamente.\n')
                
            elif option == '2':
                while True:
                    try:
                        path = input('Ingrese la dirección de la carpeta objetivo: ')
                        if path == '0':
                            break
                        Metadata.PrintMeta(path)
                        break
                    except Exception as e:
                        print('Error:', e)
                        print('Ingrese los datos correctamente.\n')
            elif option == '3':
                while True:
                    try:
                        print('\t[1] Encriptar\n\t[2] Desencriptar\n\t')
                        rot = input('Rot 13> ')
                        if rot == '1':
                            frase = input('Ingrese la frase a encriptar: ')
                            Rot13.Encriptar(frase)
                        elif rot == '2':
                            frase = input('Ingrese la frase a desencriptar: ')
                            Rot13.Desencriptar(frase)
                        elif rot == '0':
                            break
                        else:
                            raise Exception
                        break
                    except Exception as e:
                        print('Error:', e)
                        print('Ingrese los datos correctamente.\n')
            elif option == '4':
                while True:
                    try:
                        ip = input('Ingrese la ip a investigar: ')
                        if ip == '0':
                            break
                        inicio = input('Ingrese el puerto inicial: ')
                        if inicio == '0':
                            break
                        fin = input('Ingrese el puerto final: ')
                        if fin == '0':
                            break
                        Nmap.Escaneo(ip,inicio,fin)
                        break
                    except Exception as e:
                        print('Error:', e)
                        print('Ingrese los datos correctamente.\n')
            elif option == '5':
                while True:
                    try:
                        api = input('Ingrese la api: ')
                        if api == '0':
                            break
                        company = input('Ingrese la compañía: ')
                        if company == '0':
                            break
                        numero = input('Ingrese número de correos: ')
                        if numero == '0':
                            break
                        Hunter.hunter_mail(api,company,numero)
                        break
                    except Exception as e:
                        print('Error:', e)
                        print('Ingrese los datos correctamente.\n')
            elif option == 'clear':
                os.system('cls')
            elif option == '0':
                print('\n¡Que tenga un buen día!\n')
                x = 0
            else:
                print('\nEscoja una opción válida:\n')


if __name__ == '__main__':
    try:
        import Nmap
        import Metadata
        import Hunter
        import Rot13
        import PSVT
        Main()
    except ImportError:
        logging.error('No se tienen instalados todos los modulos. ')
        os.system('pip install -r requirements.txt')
        print("Módulos Instalados...","Ejecuta de nuevo")
        exit()