import PySimpleGUI as sg
from random import randint

mega_sena = []

for i in range(1, 7):
    mega_sena.append(randint(1, 60))

text = sg.PopupGetText('Qual loteria você quer?', 'LOTERIAS!')
for i in range(1,1000):
    sg.OneLineProgressMeter('Calculando chances', i+1, 1000, ' ', 'Acessando banco de dados...')
sg.Popup('Seus números da sorte são: ', f'{mega_sena}')
