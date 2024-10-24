from ipaddress import ip_address
import socket
import time
import os

def ipTracker():
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(2):
        time.sleep(0.2)
    print("<< ======================================== >>")
    print("||                                         ||")
    print("||      IP Address Tracker                 ||")
    print("||      Made By : Suryo Saputro            ||")
    print("||      Github : SrySptr                   ||")
    print("||      Instagram : www39.srysptr.go.blok  ||")
    print("||                                         ||")
    print("<< ======================================== >>")
    print(" ")
    host = input("Masukkan nama domain : ")
    ip_address = socket.gethostbyname(host)
    for i in range(3):
        time.sleep(0.2)
    print(" ")
    print("<< ======================================== >>")
    print(" ")
    for i in range(3):
        time.sleep(0.2)
    print(f"Nama domain : {host}")
    print(f"IP Address  : {ip_address}")
    print(" ")
    print("<< ======================================== >>")
    print(" ")
    usr = str(input("Ingin melanjutkan? y/N : "))
    if usr == "y" or usr == "Y":
        ipTracker()
    elif usr == "n" or usr == "N":
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()


ipTracker()