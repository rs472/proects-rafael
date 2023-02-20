from pytube import YouTube, streams
from pytube.cli import on_progress

#link do video
link = input('Insira o link: ')

#progresso do video
yt = YouTube(link, on_progress_callback=on_progress)

#mostar download execultando
print('Baixando...')

#titulo do video
titulo = yt.title
print('Titulo= ', titulo)

#maior resolução
ys = yt.streams.get_highest_resolution()

#download
ys.download()



