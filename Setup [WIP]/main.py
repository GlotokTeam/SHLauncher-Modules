# Я заебался писать эту залупу, лучше используйте другие программы, но если шило в жопе заиграло (как у меня)
# То пиши, коментов не оставлю, я наверно спать | 11.05.2024 1:51
import winreg as _winreg
import time
directory = "C:/Program Files/SHLaucnher"
REG_PATH = r"SOFTWARE\Ameteroz GitHub\Setup"
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
print("Python Installer\nMade by Ameteroz")
print("App : Лаунчер SHLauncher")
print("Пожалуйста подождите....")
time.sleep(1)
input("Желаете продолжить установку\nЕсли да, то нажмите Enter\nЕсли нет, то закройте программу")
print("Прописка изменений...")
set_reg("README", "This a SHLauncher Directory, please don't change any values!")
set_reg("TimeStamp" , str(time.time()))
set_reg("CurrentVer", "0.1")
set_reg("Branch", "main")
set_reg("Directory", directory)