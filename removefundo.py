import PySimpleGUI as sg
from removebg import RemoveBg

File_types = [
    ('JPEG (*.jpg)', "*.jpg"),
    ('PNG (*.png)','*.png')
]


sg.theme('Dark Green 5')

layout = [

    [sg.Text('Removedor de fundo'),
    sg.Input(size =(25,1), key = 'FILE'),
    sg.FileBrowse(file_types=File_types),
    sg.Button('Remover'),
    sg.Text(key = 'sucess')
    ]
]

win = sg.Window('Removedor de Background', layout)

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Remover':
        pathfile = values['FILE']
        rmbg = RemoveBg('dTa7G3KG3qKP9hVseZEpuKyb', 'error.log')
        rmbg.remove_background_from_img_file(pathfile)
        win['sucess'].update('Feito com sucesso!')
        print (rmbg)
win.close()

