from playsound import playsound
import os
song = input('Qual o nome da musica a ser tocada? ')
if os.path.exists(song):
    playsound(song)
else:
    print('O arquivo {} não está no diretório do script Python'.format(song))