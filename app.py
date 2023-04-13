
import PySimpleGUI as sg
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from ImageDuplicateFinder import ImageDuplicateFinder
from VideoDuplicateFinder import VideoDuplicateFinder
file_list_column = [
    [
        sg.Text("Browse"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
        sg.Button("Find")
    ]
]

layout = [
    [
        sg.Column(file_list_column)
    ]
]

window = sg.Window("Duplicate Finder", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Find":
        folder = values["-FOLDER-"]
        ImageDuplicateFinder(folder)
        VideoDuplicateFinder(folder)

window.close()