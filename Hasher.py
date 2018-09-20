# coding=utf-8
import sys
import os
import hashlib
from colorama import Fore, Back, Style

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=25, cols=95))

T_G_Color = Fore.LIGHTGREEN_EX
T_R_Color = Fore.RED

cls = lambda: os.system('clear')
cls()

logo =  Fore.YELLOW + """
  ██░ ██  ▄▄▄        ██████  ██░ ██ ▓█████  ██▀███      ▄▄▄      
 ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒   ▒████▄    
 ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒   ▒██  ▀█▄  
 ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄     ░██▄▄▄▄██ 
 ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒    ▓█   ▓██▒
  ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░    ▒▒   ▓▒█░
  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░     ▒   ▒▒ ░
  ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░     ░░   ░      ░   ▒   
  ░  ░  ░      ░  ░      ░   ░  ░  ░   ░  ░   ░              ░  ░
                                                                                                                
"""
print logo
print """
 1) MD5 Encrypt
 2) SHA1 Encrypt
 3) SHA224 Encrypt
 4) SHA256 Encrypt
 5) SHA384 Encrypt
 6) SHA512 Encrypt
"""

ans=True
ans = raw_input(T_G_Color + " [" + Fore.BLUE + "X" + T_G_Color + "]> ")

if ans == "1":
    cls()
    print (T_R_Color + logo)
    IMP_Encrypt = raw_input(T_G_Color + " Text To Encrypt : ")
    Encrypt = (hashlib.md5(IMP_Encrypt.encode('utf-8')).hexdigest())
    print(T_G_Color + " Encrypted : " + Encrypt)
    try:
        input(Fore.CYAN + "\n\n\n\n\n\n\n\n\n [ Press Enter To Continue ]")
    except SyntaxError:
        pass
    cls()
elif ans == "2":
    cls()
    print (T_R_Color + logo)
    IMP_Encrypt = raw_input(T_G_Color + " Text To Encrypt : ")
    Encrypt = (hashlib.sha1(IMP_Encrypt.encode('utf-8')).hexdigest())
    print(T_G_Color + " Encrypted : " + Encrypt)
    try:
        input(Fore.CYAN + "\n\n\n\n\n\n\n\n\n [ Press Enter To Continue ]")
    except SyntaxError:
        pass
    cls()
elif ans == "3":
    cls()
    print (T_R_Color + logo)
    IMP_Encrypt = raw_input(T_G_Color + " Text To Encrypt : ")
    Encrypt = (hashlib.sha224(IMP_Encrypt.encode('utf-8')).hexdigest())
    print(T_G_Color + " Encrypted : " + Encrypt)
    try:
        input(Fore.CYAN + "\n\n\n\n\n\n\n\n\n [ Press Enter To Continue ]")
    except SyntaxError:
        pass
    cls()
elif ans == "4":
    cls()
    print (T_R_Color + logo)
    IMP_Encrypt = raw_input(T_G_Color + " Text To Encrypt : ")
    Encrypt = (hashlib.sha256(IMP_Encrypt.encode('utf-8')).hexdigest())
    print(T_G_Color + " Encrypted : " + Encrypt)
    try:
        input(Fore.CYAN + "\n\n\n\n\n\n\n\n\n [ Press Enter To Continue ]")
    except SyntaxError:
        pass
    cls()
elif ans == "5":
    cls()
    print (T_R_Color + logo)
    IMP_Encrypt = raw_input(T_G_Color + " Text To Encrypt : ")
    Encrypt = (hashlib.sha384(IMP_Encrypt.encode('utf-8')).hexdigest())
    print(T_G_Color + " Encrypted : " + Encrypt)
    try:
        input(Fore.CYAN + "\n\n\n\n\n\n\n\n\n [ Press Enter To Continue ]")
    except SyntaxError:
        pass
    cls()
elif ans == "6":
    cls()
    print (T_R_Color + logo)
    IMP_Encrypt = raw_input(T_G_Color + " Text To Encrypt : ")
    Encrypt = (hashlib.sha512(IMP_Encrypt.encode('utf-8')).hexdigest())
    print(T_G_Color + " Encrypted : " + Encrypt)
    try:
        input(Fore.CYAN + "\n\n\n\n\n\n\n\n\n [ Press Enter To Continue ]")
    except SyntaxError:
        pass
    cls()
elif ans != "":
    print("\n Not Valid Choice Try again")