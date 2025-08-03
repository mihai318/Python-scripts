import os
import shutil

folder_download = os.path.expanduser("C:/Users/Mihai/Downloads")

files_types = {
    "PDF" : ["pdf"],
    "Images" : ["png","jpg","jpeg","bmp"],
    "Documents" : ["doc","docx"],
    "Archives" : [".rar",".7z"]
}

for folder in files_types:
    folder_path = os.path.join(folder_download, folder)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(folder_download):
    file_path = os.path.join(folder_download, filename)

    if os.path.isfile(file_path):
        continue

    _, ext = os.path.splitext(filename)

    for folder,extensions in files_types.items():
        if ext.lower() in extensions:
            dest_folder = os.path.join(folder_download, folder)
            shutil.move(file_path, os.path.join(dest_folder, folder))
            print(" Mutat: {filename) -> {folder}/")
            break

