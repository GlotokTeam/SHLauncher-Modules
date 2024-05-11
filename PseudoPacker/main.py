import zipfile # Основная библиотека
import shutil # Основная библиотека
import os # для error()
import time # для error()

file_type = '.fxa' # Псевдо новый формат

try:
    os.mkdir('output')
    os.mkdir('input')
except OSError:
    pass

def error(): # По приколу
    print("Неверный аргумент")
    time.sleep(3)
    os.system("main.py")


print('[1] Создание псевдо архива\n[2] Распаковка псевдоархива')
mode = input("Режим : ")
if mode == '1':
    print("Пример : [fafon, yasha]")
    name = input("Имя архива (БЕЗ РАСШИРЕНИЯ) : ")
    sleeper = input("Положите в папку input все файлы для запаковки\nПосле нажмите Enter")
    shutil.make_archive(name, 'zip', 'input') # Китайский костыль, из-за библиотеки zipfile
    os.rename(name+'.zip', name+file_type) # Китайский костыль, из-за библиотеки zipfile
    
    
elif mode == '2':
    print("Пример : [fafon, yasha]")
    print("Файлы будут находится в папке output")
    name = input("Имя архива (БЕЗ РАСШИРЕНИЯ) : ")
    with zipfile.ZipFile(name+file_type) as zf:
        zf.extractall('output')
else:
    error()
