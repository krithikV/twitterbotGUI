import sys
import PySimpleGUI as sg
from twython import Twython

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to twitter bot GUI')],
            [sg.Text('Enter Your apiKey: '), sg.InputText(key = 'api')],
            [sg.Text('Enter Your apiSecret: '), sg.InputText(key = 'apis')],
            [sg.Text('Enter Your accessToken: '), sg.InputText(key = 'at')],
            [sg.Text('Enter Your accessToken Secret: '), sg.InputText(key = 'ats')],
            [sg.Text('Please enter your tweet: '), sg.InputText(key = 'post')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Twitter bot', layout)
# your twitter consumer and access information goes here
# note: these are garbage strings and won't work

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

while True:
    event, values = window.read()
    if event == 'Ok':	# if user closes window or clicks cancel
        if values['api'] == "" or values['apis'] == "" or values['at'] == "" or values['ats'] == "":
            api = Twython(values['api'],values['apis'],values['at'],values['ats'])
        api.update_status(status=values['post'])
        print('You posted ', values['post'])
    
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break

window.close()
    
