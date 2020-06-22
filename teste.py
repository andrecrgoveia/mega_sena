import PySimpleGUI as sg
from random import randint

# Mega Sena is the name of a lotery in brazil
mega_sena = []

# Creating a loop
for i in range(1, 7):
    mega_sena.append(randint(1, 60))

# Show the results
text = sg.PopupGetText('Qual loteria você quer?', 'LOTERIAS!')
sg.Popup('Seus números da sorte são: ', f'{mega_sena}', text)
