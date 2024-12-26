import requests 
import os
import threading
import time
# from urllib.request import urlretrieve
from urllib.parse import urlparse
import http.client

global is_downloading

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
    print(f"Скачано {round(os.path.getsize(filename) / 1024 / 1024, 2)} мб")

def output_size():
    while not os.path.exists(filename):
        time.sleep(1) # если файла ещё не существует, ждём 
    
    while os.path.getsize(filename) < filesize and is_downloading:
        print_size()
        time.sleep(1)  
    
    if os.path.getsize(filename) == filesize:
        print_size()


url = input("Ссылка на файл: ")

parsed_url = urlparse(url)

conn = http.client.HTTPSConnection(parsed_url.netloc)
conn.request("GET", parsed_url.path)
r = conn.getresponse()

filename = url[url.rfind('/')+1:]
print("Имя файла: ", filename)

filesize = int(r.headers.get('content-length', 0))
print("Размер файла: ", filesize)
    

with open(filename, 'wb') as file:
    is_downloading = True

    thread = threading.Thread(target=output_size)
    thread.start()

    while True:
        chunk = r.read(8192) 
        if not chunk:
            break
        file.write(chunk)
        
    # Завершаем скачивание
    is_downloading = False
    thread.join()

print_size() # чтобы конечный размер тоже вывелся
