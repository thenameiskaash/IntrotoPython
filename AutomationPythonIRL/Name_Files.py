# Automation Script that allows me to get the names of the files in a folder
import os 

def list_of_files(name_of_folder):
    i = 1
    folder = os.listdir(name_of_folder)
    with open("Name of each file.txt", 'w') as f:
        for each_file in folder:
            if i <= 180:
                print(f"photos.google.com/search/{each_file}", file = f)
                i+=1
            else:
                break



folder = 'C:/Users/kaash/Documents/Photos-001'
list_of_files(folder)