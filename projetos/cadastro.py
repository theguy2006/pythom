from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
        [sg.Text('usuario'),sg.Input(key='usuario')],
        [sg.Text('senha'),sg.Input(key='senha',password_char='*')],
        [sg.Checkbox('Salvar o login?')],
        [sg.Button('entrar')]]

#janela
janela = sg.Window('Tela de login',layout)
#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'cauã' and valores['senha'] == '123456':
            print('Bem-vindo a nosso site!')