import PySimpleGUI as sg
from random import randint

mega_sena = []

for i in range(1, 7):
    mega_sena.append(randint(1, 60))

text = sg.PopupGetText('Qual loteria você quer?', 'LOTERIAS!')
# layout the Window
layout = [[sg.Text('Calculando os melhores números')],
          [sg.ProgressBar(5000, orientation='h', size=(20, 20), key='progbar')],
          [sg.Cancel()]]

# create the Window
window = sg.Window('Progresso', layout)
# loop that would normally do something useful
for i in range(5000):
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=0)
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
        # update bar with loop value +1 so that bar eventually reaches the maximum
    window['progbar'].update_bar(i + 1)
# done with loop... need to destroy the window as it's still open
window.close()
#for i in range(1,1000):
#    sg.OneLineProgressMeter('Calculando chances', i+1, 1000, ' ', 'Acessando banco de dados...')
sg.Popup('Seus números da sorte são: ', f'{mega_sena}')
