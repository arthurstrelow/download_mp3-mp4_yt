import pyautogui
from pytube import YouTube
from os import rename, remove, path
from time import sleep
from glob import glob
from moviepy.editor import *
from subprocess import run


def reliquia(inicio, fim, variavel):
    strr = str(variavel)
    string2 = strr.split(inicio)
    final = string2[1].split(fim)
    return final[0]


geral = []
while True:
    url = pyautogui.prompt(text='Digite a URL do Vídeo\nExemplo: https://www.youtube.com/watch?v=LXb3EKWsInQ',
                           title='Baixe .mp3/.mp4 do Youtube')
    if url is None:
        quit()
    while url == '':
        url = pyautogui.prompt(
            text='URL informada está vazia!\nDigite novamente a URL!\nExemplo: https://www.youtube.com/watch?v=LXb3EKWsInQ',
            title='Baixe .mp3/.mp4 do Youtube')
    else:
        if url is None:
            quit()
    try:
        teste = YouTube(url)
        minuaturateste = teste.title
    except:
        pass
    else:
        break

video = YouTube(url)
titulo = video.title
titulo = titulo.replace('.', '')
titulo = titulo.replace('|', '')
titulo = titulo.replace(',', '')
titulo = titulo.replace(':', '')
titulo = titulo.replace('"', '')
opcao = pyautogui.confirm(text='Escolha uma opção', title=f'{video.title}', buttons=['.MP4', '.MP3'])

if opcao == '.MP4':
    streaming = video.streams.filter(only_video=True, file_extension="mp4").order_by("resolution")
    for i, e in enumerate(streaming):
        try:
            videos_opcaos = reliquia('mime_type="video/mp4" ', ' vcodec="', streaming[i])
        except:
            pass
        else:
            videos_id = reliquia('itag=', ' mime_type=', streaming[i])
            geral.append([f'''ID: {videos_id} INFO => {videos_opcaos}

            '''])
    pyautogui.alert(geral)
    opcao2 = int(pyautogui.prompt(text='Digite o "ID" do vídeo para baixar', title='Digite o ID!').strip())
    baixar = video.streams.get_by_itag(opcao2)
    audio = video.streams.get_by_itag(140)
    baixar.download()
    rename(f'{titulo}.mp4', 'video.mp4')
    audio.download()
    rename(f'{titulo}.mp4', 'audio.mp4')
    novotitulo = titulo.replace('(', '')
    novotitulo = novotitulo.replace(')', '')
    novotitulo = novotitulo.replace(' ', '_')
    novotitulo = novotitulo.replace('&', '_')
    run(["ffmpeg", '-i', 'video.mp4', '-i', 'audio.mp4', '-c:v', 'copy', '-c:a', 'aac', f'{novotitulo}.mp4'])
    sleep(10)
    remove('video.mp4')
    remove('audio.mp4')
    dir = '.'
    files = glob(path.join(dir, '*.mp4'))
    rename(files[0], ' ' + video.title + '.mp4')
    pyautogui.alert('Video Baixado com Sucesso!')
else:
    audio = video.streams.filter(only_audio=True, file_extension="mp4")
    for i, e in enumerate(audio):
        try:
            musica_opcoes = reliquia('mime_type=', ' acodec="', audio[i])
        except:
            pass
        else:
            musica_id = reliquia('itag=', ' mime_type=', audio[i])
            geral.append([f'''ID: {musica_id} INFO => {musica_opcoes}

                '''])
    pyautogui.alert(geral)
    opcao2 = int(pyautogui.prompt(text='Digite o "ID" do vídeo para baixar', title='Digite o ID!').strip())
    baixar = video.streams.get_by_itag(opcao2)
    baixar.download('')
    clip = AudioFileClip(titulo + '.mp4')
    clip.write_audiofile(titulo + '.mp4'[:-4] + ".mp3")
    clip.close()
    remove(titulo + '.mp4')
    pyautogui.alert('Música Baixado com Sucesso!')