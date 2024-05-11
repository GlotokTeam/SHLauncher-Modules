import hashlib
import time
print("SHLauncher update-warmup module")
name = input("Напишите имя файла : ")
with open(name, 'rb') as f:
    hsh = hashlib.sha256()
    while True:
        data = f.read(2048)
        if not data:
            break
        hsh.update(data)
    rez = hsh.hexdigest()
    print(rez + " | SHA 256")
time.sleep('20')