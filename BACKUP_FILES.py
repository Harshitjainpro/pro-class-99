import time
import os
import shutil

path = input("plese enter the path of file: ")
list_of_fils = os.listdir(path)
for file in list_of_fils:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.mkdir(path+'/'+ext)        
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)   