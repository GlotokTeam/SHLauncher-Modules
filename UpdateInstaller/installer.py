# Это как фильтрация почек. Модуль который обновляться не собирается в угоду нормальной установке обновления
from tkinter import messagebox as mb # Уведы
import logging as log # Логирование
import winreg as _winreg # Узкое горлышко, поскольку лень делать общие конфиги
import zipfile # Распаковка .fxa архивов (псевдо)
import os # Проверка файла
import time # Штамп обновления и ожидание
import hashlib # Проверка хэшей
import requests # Китайская проверка версий
REG_PATH = r"SOFTWARE\Ameteroz GitHub\SHLauncher\Setup" # Путь установки/Конфигураций
def set_reg(name, value): # Cпизженно с Stackoverflow
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
def get_reg(name):# Cпизженно с Stackoverflow
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
# А спизженно, хуй знает с какого вопроса, но типо гугли winreg python, хотя тут более всё понятно
cur_version = get_reg("CurrentVer")
log.basicConfig(level=log.INFO, filename="upd_installer.log",filemode="w",
                    format="%(asctime)s | %(levelname)s | %(message)s")
log.info("Installer log")
log.info("Connecting to the version server...")
print("Происходит установка обновления...")
print("Не выключайте компьютер или не закрывайте программу во время установки")
print("В случае если обновление не установилось, отправте upd_installer.log")
print("    На форум в спец. раздел")
version = requests.get("https://pastebin.com/raw/yfseDiR6").text
hashup = requests.get("https://pastebin.com/raw/a8KcrbbP").text
log.info(f"Actual (Web) Version : {version}")
log.info(f"Current (RunTime) Version : {cur_version}")
log.info(f"Acutal Hash : {hashup}")
if cur_version != version:
    log.warning(f"Current Version : {cur_version} | Web Version : {version}")
    if os.path.exists("update.fxa"):
        with open("update.fxa", 'rb') as f:
         hsh = hashlib.sha256()
         while True:
             data = f.read(2048)
             if not data:
                break
             hsh.update(data)
        rez = hsh.hexdigest()
        log.info("Update found!")
        log.info("Hash checking...")
        if rez != hashup:
            log.error("Update file is corrupted! Restart update download!")
        elif rez == hashup:
            log.info("Hask checked!")
            log.info("Starting a update process...")
            with zipfile.ZipFile("update.fxa") as zf:
                zf.extractall('./')
            log.info("Files unpacked!")
            log.info("Installing update...")
            log.info("Write a new values in register...")
            set_reg("CurrentVer", version)
            set_reg("UpdateStamp", str(time.time()))
            cur_version = get_reg("CurVersion")
            log.warning(f"Current Version : {cur_version} | Web Version : {version}")
            log.info("Installizing done!")
            print("Установка заверешна!")
            os.remove("update.fxa")
            time.sleep(4)
    else:
        log.error("File update.fxa not found. Restart update download!")
elif cur_version == version:
    log.info("I'am not needed in update")
elif cur_version == "NONE" or cur_version == "none" or cur_version == "None":
    log.error("Current version is NONE. Please reinstall or rerun setup/init process")
    
