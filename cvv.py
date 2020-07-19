from colorama import Fore, init
from bs4 import BeautifulSoup
from itertools import cycle
import time
import requests
import json
import threading
import hashlib
import random
import gateway1, os

def Main():
    banner = """
    
  {y}//-------Juses Stripe Chk-------//
  {y}//---------Python Based v3---------//
  
  """.format(g=Fore.GREEN, r=Fore.LIGHTRED_EX, y=Fore.YELLOW)
    print(banner)
    while True:
        try:
            gateway = str(input("Select 1 > "))
        except KeyboardInterrupt:
            print(Fore.RED + '\n[-] ' + Fore.RESET + 'Recieved Exit.')
            exit(1)

        if gateway == "1":
            print()
            print(Fore.YELLOW + "[*] " + Fore.RESET + "Starting Gateway 1...")
            print()
            print("""
{re}      {ly}________________________________________________{re}
{re}     {ly}//----------{y}Stripe Gateway{ly}--------------//{re}
{re}    {ly}//---------------{y}Termux Based v3{ly}---------------//{re}
{re}   {ly}//-------{r}Contact @Derp666{ly}--------//{re}
{re}  {ly}================================================ {re}
			""".format(ly=Fore.GREEN, g=Fore.GREEN, y=Fore.YELLOW, r=Fore.RED, re=Fore.RESET))
            ranges = []
            try:
                with open('cc.txt', 'r') as ccs:
                    for x in ccs.read().split('\n'):
                        ranges.append(x)
                print(Fore.YELLOW + "[*] " + Fore.RESET + 'Checking ' + str(len(ranges)) + ' Credit Cards.')
                #input(Fore.RESET + "PRESS ANY KEY TO CONTINUE")
                print(Fore.BLUE + "Start Checking at " + str(time.ctime()))
                print(Fore.RESET)
                
                cc = open('cc.txt', 'r')
                credit_cards = cc.read()
                ccEntry = 0

                if not os.path.exists("lives.txt"):
                    live = open("lives.txt", "w+")
                    live.write(" -- LIVES -- \n")
                    live.close()

                for x in credit_cards.split('\n'):
                    ccEntry += 1
                    try:
                        gateway1.StripeAutomate(x, ccEntry, 'Jems', "Arno")
                    except KeyboardInterrupt:
                        break
            except KeyboardInterrupt:
                pass
            print()
            print(Fore.GREEN + "[+] " + Fore.RESET + "Done on Gateway 1")
            print()


Main()
