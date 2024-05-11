import winreg as _winreg
import logging as log
import time
REG_PATH = r"SOFTWARE\Ameteroz GitHub\SHLauncher\Setup"
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
log.basicConfig(level=log.INFO, filename="init.log",filemode="w",
                    format="%(asctime)s | %(levelname)s | %(message)s")
log.info("Inistallezed INIT")
log.info("Installing a new values in register....")
set_reg("README", "This a SHLauncher Directory, please don't change any values!")
set_reg("TimeStamp" , str(time.time()))
stamp = str(time.time())
log.info(f"Time stamping : {stamp}")
set_reg("CurrentVer", "0.1")
set_reg("Branch", "main")
log.info("Done!")
