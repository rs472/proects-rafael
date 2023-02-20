from tkinter import *
import  requests
from googletrans import Translator, constants

window = Tk()
window.title('Ler Frases')
window.resizable(0,0)



def phrase():
    api = 'https://api.adviceslip.com/advice'

    GET = requests.get(api)

    FORMAT = GET.json()

    TEXT = FORMAT ['slip'] ['advice']


    translator = Translator()
    translation = translator.translate(TEXT, dest='pt')

    exib = (f"{translation.text} ({translation.dest})")
    phrase_label ['text'] = exib



font = ('Nimbus Sans [URW ]',10,'italic')
font2 = ('segoe ui variable display semibold', 10)

Text1 = Label(window, text='Clique no botão para ler uma frase: ', font=font2)
Text1.grid(column=0, row=2)

phrase_label = Label(window, font=font, text='')
phrase_label.grid(column=0, row=3)

button = Button (window, font=font2, text='Gerar frase',relief='flat',width=10, border=2,bg='#A6A6A6', command=phrase)
button.grid(column=0, row=4)

window.mainloop()