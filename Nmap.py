import nmap
import os
import socket
from datetime import datetime

date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def Escaneo(ip,inicio,fin):
    with open('logs.info', 'a') as j:
        try:
            lPath = os.path.dirname(os.path.abspath(__file__))
            scanner = nmap.PortScanner()
            if ip.upper() == 'LOCAL':
                j.write(f'[{date} NMAP]: Obteniendo la ip\n')
                target = socket.gethostbyname(socket.gethostname()) + '/24'
                scanner.scan(target)
                j.write(f'[{date} NMAP]: Escribiendo resultados en {lPath}\\resultados.csv\n')
                with open(f'{lPath}\\resultados.csv', 'w+') as f:
                    f.write(scanner.csv())
            else:
                final = fin + 1
                for i in range(inicio,final):
                    j.write(f'[{date} NMAP]: Escaneando puerto {i}\n')
                    res = scanner.scan(ip, str(i))
                    res = res['scan'][ip]['tcp'][i]['state']
                    print(f'the port {i} is {res}.')
        except Exception as e:
            j.write(f'[{date} NMAP ERROR]: {e}\n')
            print('Error:', e)

