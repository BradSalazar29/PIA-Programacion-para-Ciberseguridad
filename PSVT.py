import subprocess
import os
from datetime import datetime

date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def getVTReport(APIkey, target, result, premium):
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        command = f'{path}\\VTReport.ps1 -apikey "{APIkey}" -target "{target}" -result "{result}" -premium "{premium}"'
        PSline = "powershell -ExecutionPolicy ByPass -File "
        print('\nObteniendo el reporte...\n')
        with open('logs.info', 'a') as j:
            j.write(f'[{date} VTREPORT]: Obteniendo el reporte\n')
        subprocess.check_output(PSline + command)
        print('Reporte recuperado\n')
        with open('logs.info', 'a') as j:
            j.write(f'[{date} VTREPORT]: Reporte recuperado\n')
    except Exception as e:
        print('Error:', e)
        with open('logs.info', 'a') as j:
            j.write(f'[{date} VTREPORT ERROR]: {e}\n')