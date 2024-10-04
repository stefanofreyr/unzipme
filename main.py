import FreeSimpleGUI as sg
import extract

sg.theme('Dark Blue 15')

file_label = sg.Text("File to unzip: ")
file_input = sg.Input(tooltip="Enter a file path")
button1 = sg.FilesBrowse("Choose", key='zip')

folder_label = sg.Text("Destination folder: ")
folder_input = sg.Input(tooltip="Enter a folder path")
button2 = sg.FolderBrowse("Choose", key='folder')

unzip_button = sg.Button("Unzip")
output_label = sg.Text(key='output')

window = sg.Window("Unzipme", layout=[
    [file_label,file_input,button1],
    [folder_label,folder_input,button2],
    [unzip_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case "Unzip":
            try:
                filepaths = values["zip"]
                folder = values["folder"]
                extract.extract_archive(filepaths, folder)
                window["output"].update(value="Files unzipped successfully.")
            except AttributeError:
                sg.popup("Something's not quite right...")

window.close()