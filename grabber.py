# Use with python3
# Version 2.0

import random
import socket
import os

try:
    import socks
except ModuleNotFoundError:
    os.system("pip install PySocks")
    os.system("pip install socks")

try:
    import ipapi
except ModuleNotFoundError:
    os.system("pip install ipapi")

import time
try:
    from colorama import Fore

except ModuleNotFoundError:
    os.system("pip install colorama")

from platform import platform
import sys

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
import json

try:
    from stem import SocketError
except ModuleNotFoundError:
    os.system("pip install stem")

from setup.banner import banner , banner2

W = Fore.LIGHTWHITE_EX
R = Fore.RED
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW

yes = ['y' , 'yes']
no = ['n' , 'no']


def clr():
    os.system('cls') if "Windows" in platform() else os.system("clear")

clr()

def cprint(str):
    print(f"{W}[{C}>{W}]{C} {str}")


def error(str):
    print(f"\n{W}[{R}!{W}] {str}\n")


def connection_check():
    s = requests.get("https://www.google.com")
    
    if s.status_code == 200:
        error("Connection found...")
        time.sleep(2)
        clr()
    else:
        error("Internet not found")
        sys.exit(0)

connection_check()

clr()

def main():
    banner()
    print(f"{W}\n\t\tSelect option\n")



    ip_Dict = {1 : "United States" , 2 : "Netherlands"
    , 3 : "China" , 4 : "India" , 5 : "Taiwan" , 6 : "Australia"
    , 7 : "United Kingdom" , 8 : "Pakistan" , 9 : "Nepal" , 10 : "Indonesia"
    , 11 : "Korea" , 12  : "Germany" , 13 : "Colombia" , 14 : "Turkey" , 15 : "South Africa"
     , 16 : "Singapore" , 17 : "Ethiopia" , 18 : "Romania" , 19 : "Japan" , 20 : "Brazil" , 21 : "Saudi Arabia"
     , 22 : "Mauritius" , 23 : "France" , 24 : "Italy" , 25 : "Zambia" , 26 : "Iran" , 27 : "Ireland"
    , 28 : "Portugal" , 29 : "Panama" , 30 : "Russia" , 31 : "Poland" , 32 : "Venezuela" , 33 : "Belgium"
    , 34 : "Finland" , 35 : "Czechia" , 36 : "Kazakhstan" , 37 : "Canada" , 38 : "Austria" , 39 : "Egypt"
    , 40 : "Vietnam" , 41 : "Morocco" , 42 : "Argentina" , 43 : "Tunisia" , 44 : "Thailand" , 45 : "Mexico"
    , 46 : "Spain" , 47 : "Malaysia" , 48 : "Palestine" , 49 : "Switzerland" , 50 : "Greece" , 51 : "Togo"
    , 52 : "Norway" , 53 : "Hong Kong" , 54 : "Denmark" , 55 : "Nigeria" , 56 : "About me"
    }


    ip_info_code = {"US":"United States" , "NL":"Netherlands" , "CN":"China" , "IN":"India" , "TW":"Taiwan"
    , "AU":"Australia" , "GB":"United Kingdom" , "PK":"Pakistan" , "NP":"Nepal" , "ID":"Indonesia" , "KR":"Korea"
    , "DE":"Germany" , "CO":"Colombia" , "TR":"Turkey" , "ZA":"South Africa" , "SG":"Singapore"
    , "ET":"Ethiopia" , "RO":"Romania" , "JP":"Japan" , "BR":"Brazil" , "SA":"Saudi Arabia" , "MU":"Mauritius"
    , "FR":"France" , "IT":"Italy" , "ZM":"Zambia" , "IR":"Iran" ,  "IE":"Ireland" , "PT":"Portugal" , "PA":"Panama"
    , "RU":"Russia" , "PL":"Poland" , "VE":"Venezuela" , "BE":"Belgium" , "FI":"Finland" , "CZ" : "Czechia" 
    , "KZ":"Kazakhstan" , "CA":"Canada" , "AT":"Austria" , "EG":"Egypt" , "VN":"Vietnam" , "MA":"Morocco"
    , "AR":"Argentina" , "TN":"Tunisia" , "TH":"Thailand" , "MX":"Mexico" , "ES":"Spain" , "MY":"Malaysia"
    , "PS":"Palestine" , "CH":"Switzerland" , "GR":"Greece" , "TG":"Togo" ,  "NO":"Norway" , "HK":"Hong Kong"
    , "DK":"Denmark" , "NG":"Nigeria" 
    }
    
    
    even = ""
    odd = ""
    for k , v in ip_Dict.items():
        if k%2 == 1:
            odd = f'{W}[{G}{str(k)}{W}] {C}{v}'
            
        elif k%2 == 0:
            even = f"{W}[{G}{str(k)}{W}] {C}{v}"

            print(odd + "\t" + even)



    try:
        choice = int(input(f"{W}\nEnter:~ "))
    
    except ValueError:
        error("BullShit!!")
        sys.exit()
    if choice == 56:
        banner2()
        exit()

    if choice in ip_Dict.keys():
        ip_country = ip_Dict.get(choice)

        filename = ip_country + '.txt'

        print(f"{W}Country selected: {G}{ip_country}\n")



        if os.path.exists(filename):
            del_file = input(f"{C}\nDo you want to delete previous {W}{filename}{R}(y/n): ").lower()
            if del_file in yes:
                os.remove(filename)

            else:
                error("File can't be deleted")


    else:
        error("Invalid option")
        sys.exit()

    ip_gen = []
    
    ip_range = int(input(C +"\nHow many ip's do you want: "))

    value = []

    while len(value) != ip_range:
        ip1 = random.randint(1 , 255)
        ip2 = random.randint(1 , 255)
        ip3 = random.randint(1 , 255)
        ip4 = random.randint(1 , 255)
        ip = str(ip1)+'.'+str(ip2) + '.' + str(ip3) + '.' +str(ip4)
        print(f"\n{C}Ip generated : {W}{ip}")
        ip_gen.append(ip)


        cprint(f"Trying to find country...{W}{ip}")



        try:
            ip_cont = ipapi.location(ip)

            if ip_cont['country_name'] == ip_country:
                print(f"{Y}IP {ip} is of {W}{ip_country}\n")
                
                value.append(ip)
                with open(filename , "a+") as file:
                    file.write(ip + "\n")

            else:
                print(f"{R}{ip} is not valid :{W} {ip_cont['country_name']}\n")
                with open("AllCountriesIP.txt" , "a+") as ipp:
                    ipp.write(ip)

        except KeyError:
            print(R + "Not valid ip")

        except KeyboardInterrupt:
            cprint("Exiting...")
            sys.exit()
        except Exception:
            error("\nSwitching ip scanner...\n")

            try:
                ipinfosec = "https://www.ipinfo.io/"


                ip_resp = requests.get(ipinfosec+ip+'/json')

                for key , val in ip_info_code.items():
                    if val == ip_country:
                        new_country_code = key

                else:
                    pass

                ip_resp = json.loads(ip_resp.text)

                if ip_resp['country'] == new_country_code:
                    print(f"{Y}IP {ip} is of {W}{ip_country}\n")
                    filename = ip_country + '.txt'
                    value.append(ip)
                    with open(filename , "a+") as file:
                        file.write(ip + "\n")

                else:
                    print(f"{R}{ip} is not valid : {W}{ip_cont['country_name']}\n")

            except KeyError:
                error(R + "Not valid ip")

            except KeyboardInterrupt:
                cprint("Good Bye")
                sys.exit()
            
            except Exception as e:
                error(e)
                

            

    print("Ip's generated and saved in " + filename)
    tr = True
    px = 0

    # Using proxy

    while tr == True:
        port = random.randint(1000,9999)
        port = str(port)
        try:
            print(f"{W}\nChanging proxy:{C} {value[px]}:{port}")
            socket.socket = socks.socksocket
            socks.set_default_proxy(socks.SOCKS5,value[px],port)
            
            time.sleep(300)
            px = px +1
        except SocketError:
            error("Something went wrong!")

        except KeyboardInterrupt:
            error("Exitiing.....")
            tr = False
        except KeyError:
            cprint(f"{R}Fixing error....")


        
        if len(value) == px:
            clr()
            cprint(f"{C}\nEstablishing connection again...")
            px = 0
        else:
            pass
        

main()



    


        

