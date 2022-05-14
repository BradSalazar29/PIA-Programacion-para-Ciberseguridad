from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime

date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)

def get_exif_metadata(image_path):
    try:
        ret = {}
        image = Image.open(image_path)
        if hasattr(image, '_getexif'):
            exifinfo = image._getexif()
            if exifinfo is not None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
        decode_gps_info(ret)
        return ret
    except Exception as e:
        print('Error:', e)

def PrintMeta(dire):
    with open('metadata.txt', 'a') as f:
        with open('logs.info', 'a') as j:
            print("\n-------------Ruta de imágenes: "+dire+"-------------\n")
            f.write(f"\n{date}s\n-------------Ruta de imágenes: " + dire + "-------------\n")
            j.write(f'[{date} METADATA]: Buscando en {dire}\n')
            os.chdir(dire)
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    print('\n',os.path.join(root, name))
                    f.write('\n' + os.path.join(root, name))
                    print ("[+] Metadata for file: %s \n" %(name))
                    f.write("[+] Metadata for file: %s \n" %(name))
                    try:
                        j.write(f'[{date} METADATA]: Extrayendo metadata para {name}\n')
                        exifData = {}
                        exif = get_exif_metadata(name)
                        for metadata in exif:
                            print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                            f.write("Metadata: %s - Value: %s \n" %(metadata, exif[metadata]))
                        print ("\n")
                        j.write(f'[{date} METADATA]: Metadata recuperada\n')
                    except Exception as e:
                        j.write(f'[{date} METADATA ERROR]: {e}\n')
