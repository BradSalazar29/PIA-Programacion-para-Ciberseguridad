from datetime import datetime
from tkinter import E

date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

ALPHABET = {
    'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R',
    'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W',
    'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B',
    'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G',
    'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
    'Z':'M'
    }

def Encriptar(input_phrase):
    with open('logs.info', 'a') as j:
        try:
            input_phrase = input_phrase.upper()
            encrypted_phrase = ''
            j.write(f'[{date} ROT13]: Encriptando {input_phrase}\n')
            for letter in input_phrase:
                found = False
                for x,y in ALPHABET.items():
                    if letter == x:
                        encrypted_phrase += y
                        found = True
                if not found:
                    encrypted_phrase += letter
            print(encrypted_phrase)
            j.write(f'[{date} ROT13]: {input_phrase} encriptada\n')
        except Exception as e:
            j.write(f'[{date} ROT13 ERROR]: {e}\n')
            print('Error:', e)
    
def Desencriptar(input_phrase):
    with open('logs.info', 'a') as j:
        try:
            input_phrase = input_phrase.upper()
            decrypted_phrase = ''
            j.write(f'[{date} ROT13]: Desencriptando {input_phrase}\n')
            for letter in input_phrase:
                found = False
                for x,y in ALPHABET.items():
                    if letter == y:
                        decrypted_phrase += x
                        found = True
                if not found:
                    decrypted_phrase += letter
            print(decrypted_phrase)
            j.write(f'[{date} ROT13]: {input_phrase} desencriptada\n')
        except Exception as e:
            j.write(f'[{date} ROT13 ERROR]: {e}\n')
            print('Error:', e)
