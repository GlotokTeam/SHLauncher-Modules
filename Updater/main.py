# Эта хуйня использует наработки лоадера, но с функцией проверки
# OxiData не подняли ещё, поэтому юзаем pastebin и github
import time
import logging as log # Логирование
import os # Запуск
import winreg as _winreg # Узкое горлышко, поскольку лень делать общие конфиги\
REG_PATH = r"SOFTWARE\Ameteroz GitHub\SHLauncher\Setup"
import requests # Китайская проверка версий
from urllib import request # Обновление
from urllib3 import PoolManager # Обновление
log.basicConfig(level=log.INFO, filename="updater.log",filemode="w",
                    format="%(asctime)s | %(levelname)s | %(message)s")
def get_reg(name):# Cпизженно с Stackoverflow
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

update_server = requests.get("https://pastebin.com/raw/TQXWt999").text
log.info("Connecting to the version server...")
version = requests.get("https://pastebin.com/raw/yfseDiR6").text
upd_version = get_reg("CurrentVer")
print("Checking version...")
log.info(f"Actual (Web) Version : {version}")
log.info(f"Current (RunTime) Version : {upd_version}")
if version != upd_version:
    log.info("Updater not actual. Downloading update")
    filename = 'update.fxa'
    http = PoolManager()
    log.info("Openning PoolManager...")
    response = http.request('GET', update_server)
    image_data = response.data
    with open(filename, 'wb') as file:
        file.write(image_data)
    log.info("Starting installing...")
    os.system("python installer.py")