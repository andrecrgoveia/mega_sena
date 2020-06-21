import PySimpleGUI as sg

sg.theme('DarkGreen')
layout = [sg.Text('Enter something on Row 2'), sg.InputText()]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()
