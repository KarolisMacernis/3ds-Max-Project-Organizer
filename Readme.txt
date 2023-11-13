An app with a GUI interface to organize and archive 3Ds Max project files.

The workflow which this app is designed to work with contains 3Ds Max project folders with the name "Package",
followed by an underscore, then the project name, another underscore and the date for when it is to be archived (For
example: Package_Kitchen_Interior_20210111 or Package_Chair057_20200920). Each project folder contains the 3ds Max
file(s) and two folders named "Visuals" and "Textures". The "Visuals" folder contains the visualizations of the
project while the "Textures" folder has all the textures used in the 3ds Max model.

The purpose of the script is to create a zip file of the project which contains all the same files and folders
but name the 3ds Max scene files and the visualizations found in the "Visuals" folder by the name of the project.

Example:

If the folder chosen by the user in the GUI interface is: C:/Users/John/Desktop/Package_Kitchen_Interior_20231030, the
script will extract "Kitchen_Interior" as the project name and assign it to all the 3ds Max files and the
visualizations in the "Visuals" folder, followed by an underscore and a number if there is more than one file
(Kitchen_Interior_1.max, Kitchen_Interior_2.max and Kitchen_Interior_1.jpeg, Kitchen_Interior_2.jpeg,
Kitchen_Interior_3.jpeg, etc.). After renaming the files, the script will make a zip file in the project folder by the
name of the project (Kitchen_Interior.zip in this case).