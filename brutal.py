import os,sys,time,os,json,requests,json
from colorama import Fore,Back,init
from requests import get,post
from urllib import request

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
api_visitor='https://api.api-ninjas.com/v1/counter?id=test_id&hit=true'
key_visitor='RFj75+sjo1hyWyBRuAkZhQ==d67tIuLmR53MDfjE'
visitor=requests.get(api_visitor, headers={'X-Api-Key': key_visitor})
getvisit=json.loads(visitor.text)
localtime=time.asctime(time.localtime(time.time()))

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

os.system("clear")
autoketik(f"{ungu}[{merah}Perhatian{ungu}] {W}Jangan Lupa Masuk Discord Real Trading Money")
time.sleep(3)
os.system("xdg-open https://discord.com/invite/z8uCEzrPcG")
autoketik(f"{biru}[{kuning}Warning{biru}] {W}Masuk Memek, Udah Gw Kasih Free Juga")
autoketik(f"{ungu}[{pink}Sekali lagi{ungu}] {W}Jangan Lupa Masuk Discord Real Trading Money")
time.sleep(3)
os.system("xdg-open https://discord.com/invite/z8uCEzrPcG")
autoketik(f"{hitam}[{putih}Warning{merah}] {W}Jangan Lupa Masuk Discord Real Trading Money")
os.system("clear")
autoketik(f"""
{putih}[{biru}•{putih}] {merah}Author {merah}   : NaomyValentiano
{putih}[{hitam}•{hitam}] {abu}GitHub {putih}   : NaomyValen
{putih}[{biru}•{putih}] {hitam}Dis{biru}cord {putih}  : _naomyvalen18
{putih}[{biru}•{putih}] {ungu}Instagram {putih}: @_ryy
