import PySimpleGUI as sg
import requests

sg.theme('DarkAmber')

def GET_IP():
    get_ip = requests.get('https://api.ipify.org') 
    ip = get_ip.text
    return ip

layout = [  [sg.Text('Veja informações de seu IP: ')],
            [sg.Text('', key='text_IP')],
            [sg.Button('Ver IP'), sg.Button('Cancelar')]
]

window = sg.Window('Sobre IP', layout)

while True:
    event, values = window.read()
    if event ==  sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event =='Ver IP': 
        ip_endress = GET_IP()
        window['text_IP'].update(f'Seu endereço de IP é: {ip_endress}')
      
window.close()
