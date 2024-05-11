import hashlib
import time
actual_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" # здесь хэш, но планируется использование получение данных с инета для избежания обновления инсталлера
name = input("Напишите имя файла : ")
with open(name, 'rb') as f: # Получение хэша
    hsh = hashlib.sha256()
    while True:
        data = f.read(2048)
        if not data:
            break
        hsh.update(data)
    rez = hsh.hexdigest()
    print(rez + " | SHA 256 | Хэш файла") # Хэш предоставленного файла
    if rez != actual_hash: # Если хэш не совпадает
        print(f"Хэш не совпадает, актуальный хэш : {actual_hash}")
        time.sleep(3)
    else: # Хэш совпдает или произошла другая хуйня (лучше заменить на elif)
        print("Хэш совпадает")
        time.sleep(3)