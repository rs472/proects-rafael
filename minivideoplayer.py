from tkinter import *
from tkVideoPlayer import TkinterVideo
from tkinter.filedialog import askopenfile

#chamaremos video player de vp
player = Tk()
player.title('VideoMiniPlayer')
player.geometry('280x260+500+200')
player.resizable(0,0)

#funcoes vp

vp = TkinterVideo(player,scaled = True)
vp.load(r'C:\Users\rafae\OneDrive\Documentos\bot project bot_city\imagens do espaço.mp4')
vp.grid(columnspan=4, row=10, sticky='we', ipady=60)
vp.config(background='#3b3c49')

def playervideo():
    global vp
    vp.play()

def pausevideo():
   vp.pause()

def stopvideo():
    vp.stop()


#botão player no video
buttonvp = Button(player, text='Play', relief='flat', width=10, border=2,bg='#A6A6A6', command=playervideo)
buttonvp.grid(row=0, column=1, padx=10, pady=10)

#botão pause 
buttonpuse = Button(player, text='Pause', relief='flat',width=10, border=2,bg='#A6A6A6', command=pausevideo)
buttonpuse.grid(row=0, column=2, padx=10, pady=10)

#botão stop
buttonstop = Button(player, text='Stop', relief='flat',width=10, border=2,bg='#A6A6A6',command=stopvideo)
buttonstop.grid(row=0, column=3, padx=10, pady=10)


player.mainloop()