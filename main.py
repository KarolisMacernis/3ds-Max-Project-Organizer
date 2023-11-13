import os
import shutil
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QFileDialog, QMessageBox

def search_dir():
    """Choose the directory of the project folder and enable the "Process" button once done."""

    folder_name = QFileDialog.getExistingDirectory()
    output_label.setText(folder_name) # Set the label to the chosen folder directory.
    btn2.setDisabled(False)

def extract_name():
    """Extract the name of the project."""

    global folder_path
    global project_name

    # Change the working directory to the folder chosen by the user and convert it to a Path object.
    folder_path = (output_label.text())
    os.chdir(Path(folder_path))

    # Assign a path variable to the current working directory.
    path = os.getcwd()

    # Get the tail of the path (which will give us only the name of the chosen folder) and assign a current_folder
    # variable to it.
    current_folder = os.path.basename(path)

    # Split the current folder name into parts that are seperated by "_".
    folder_splitted = current_folder.split('_')

    # Get all the items of the folder name without the first ("Package") and the last (date).
    project_name = folder_splitted[1:-1]

    # Join back the items to form the name of the project.
    project_name = '_'.join(project_name)

def rename_max():
    """Rename the 3ds Max files according to the name of the project followed by an underscore and a number."""

    max_file_number = 0

    for max_file in os.listdir():
        max_file_name, ext = os.path.splitext(max_file)
        if ext.lower() == '.max':
            max_file_number += 1
            new_max_name = f"{project_name}_{max_file_number}{ext}"
            max_file_path = ('./' + new_max_name)
            if os.path.isfile(max_file_path):
                continue
            else:
                os.rename(max_file, new_max_name)
        else:
            continue

    # Remove the numbering if there is only one file.
    if max_file_number == 1:
        max_name_no_number = f"{project_name}{ext}"
        os.rename(new_max_name, max_name_no_number)

def rename_renders():
    """Rename the render images according to the name of the project followed by an underscore and a number."""

    os.chdir('./Visuals')

    render_file_number = 0

    global render_file_path

    for render_file in os.listdir():
        render_name, ext = os.path.splitext(render_file)
        render_file_number += 1
        new_render_name = f"{project_name}_{render_file_number}{ext}"
        render_file_path = ('./' + new_render_name)
        if os.path.isfile(render_file_path):
            continue
        else:
            os.rename(render_file, new_render_name)

    render_name_no_number = f"{project_name}{ext}"

    # Remove the numbering if there is only one file.
    if render_file_number == 1:
        os.rename(new_render_name, render_name_no_number)

def create_zip():
    """
    Create a zip file with all the project files with the correct naming in the main project directory.
    Use the name of the project for the zip file.
    """

    os.chdir(Path(folder_path))
    shutil.make_archive(project_name, format='zip', root_dir=render_file_path)

def show_popup():
    """Show "Process finished!" message once done."""

    global msg

    msg = QMessageBox()
    msg.setWindowTitle("Notification")
    msg.setText("Process finished!")
    x = msg.exec()

app = QApplication([])
window = QWidget()
window.setWindowTitle('Poroject Organizer')
window.setMinimumHeight(150)

layout = QVBoxLayout()

# Create a button to choose the project directory.
btn1 = QPushButton('Choose Project Directory')
layout.addWidget(btn1)
btn1.clicked.connect(search_dir)
btn1.setMinimumSize(250, 40)

# Create an output label that will show the chosen directory once the user has selected it.
output_label = QLabel('')
layout.addWidget(output_label)
output_label.setMinimumHeight(40)

# Create a "Process" button and connect it with the functions used for renaming the files and creating the project
# zip file.
btn2 = QPushButton('Process')
layout.addWidget(btn2)
btn2.setDisabled(True) # Set the button disabled until the project directory is chosen.
btn2.setMinimumSize(250, 40)
btn2.setStyleSheet('QPushButton {background-color: rgb(120, 120, 120); font: bold 14px; color: white;}')
btn2.clicked.connect(extract_name)
btn2.clicked.connect(rename_max)
btn2.clicked.connect(rename_renders)
btn2.clicked.connect(create_zip)
btn2.clicked.connect(show_popup)

window.setLayout(layout)
window.show()

app.exec()