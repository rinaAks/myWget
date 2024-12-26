import requests 
import os
import threading
import time
from urllib.request import urlretrieve


def download_file():
    
    # первый вариант через urlretrieve
    '''
    path, headers = urlretrieve(url, filename)
    for name, value in headers.items():
        print(name, value)
    '''
    
    # второй вариант через запись файла writing binary (wb)    
    with open(filename, mode="wb") as file:
        file.write(r.content)


def print_size():
    while not os.path.exists(filename):
        time.sleep(1) # если файла ещё не существует, ждём 
    
    current_size = os.path.getsize(filename)
    while current_size < filesize:
        print(f"Скачано {round(current_size / 1024 / 1024, 2)} мб")
        time.sleep(1)  
    
    if current_size == filesize:
        print(f"Скачано {round(current_size / 1024 / 1024, 2)} мб")


url = input("Ссылка на файл: ")
r = requests.get(url) 

filename = r.url[url.rfind('/')+1:]
print("Имя файла: ", filename)

filesize = int(r.headers.get('content-length', 0))
print("Размер файла: ", filesize)
    
thread = threading.Thread(target=print_size)
thread.start()
download_file() 

print_size()
