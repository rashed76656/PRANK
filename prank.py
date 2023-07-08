#Created by Md Rashed Mahmud 
#Date : 08-06:2023 01:28:36AM
#Prank with Your Friend++

#_______IMPORT________
import os,sys,random,time
from time import sleep

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.01)

#_______LOGO________
logo = ("""
	\033[1;93m╔═════════════════[\033[1;32m 𝘼𝘿𝙈𝙄𝙉 𝙄𝙉𝙁𝙊 \033[1;32m]═══════════════╗
	\033[1;93m║     \033[1;96m[✓] CREATED BY\33[0;m   : \033[1;96m RASHED               \033[1;32m║
	\033[1;93m║     \033[1;32m[✓] FACEBOK      : \033[1;34m Md Rashed Mahmud     \033[1;32m║
	\033[1;93m║     \033[1;35m[✓] GITHUB       :  \033[1;35mRashed76656         \033[1;32m ║
	\033[1;93m║     \033[1;36m[✓] TOOL STATUS  : \033[1;36m PRANK WITH FRIEND   \033[1;32m ║
	\033[1;93m║     \033[1;35m[✓] TEAM         :  \033[1;35mSR-SECURITY 	       \033[1;32m║
	\033[1;93m║     \033[1;36m[✓] TOOL VIRSION :  \033[1;36m0.1                 \033[1;32m ║
	\033[1;93m║᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱\033[1;32m║
	\033[1;93m║  [\033[1;97m•\033[1;91m]\033[1;32m PLZ SAPPORT ME BRO....                \033[1;32m  ║
	\033[1;93m║  [\033[1;97m•\033[1;91m]\033[1;32m SR SECURITY TEAM....                   \033[1;32m ║
	\033[1;93m╚═══════════════[\033[1;93m SR - SECURITY \033[1;32m]══════════════╝""")

#_______INPUT________
tg = str(input("\033[1;36mTarget account name : "))
os.system("clear")
time.sleep(1)
print("  \033[1;32m✓ \033[1mGetting data please wait....")
time.sleep(2)
os.system("clear")

opn = (""" 
		[\033[1;97m01\033[1;91m] \033[1;31mStart Attack 
		[\033[1;97m02\033[1;91m] \033[1;32mContact Admin
		[\033[1;97m03\033[1;91m] \033[1;30mExit""")
#_____MAIN______
def main():
	print(logo)
	print("\n")
	print("")
	print("	\033[1;32m❊╌──┈⊰᯽⊱\033[1;33mTERGET FACEBOOK ACCOUNT CLONER\033[1;32m⊰᯽⊱┈──╌❊\n")
	print("	\033[1;32mTarget Acc : \033[1;31m10007568464846\n")
	print("	\033[1;32mTarget name : \033[1;36m\033[1m",tg,"\n")
	print("	\033[1;32mSecurity Level : \033[1;35mMedium\n")
	print("	\033[1;32mFile path : \033[1;37m/sdcard/My_spt/Final.txt\n")
	print("	    \033[1;32m❊╌──┈⊰᯽⊱\033[1;33mSR - SECURITY - TEAM\033[1;32m⊰᯽⊱┈──╌❊")
	print(opn)
	Gf = input(" \033[1;32mChoose option : ")
	if Gf in ["1", "01"]:
		Nusrat()
	elif Gf in ["2", "02"]:
		Rashed()
	else:
		exit()
		
N_F = ("""
	\033[1;32m<==================================>
	\033[1;32m[+] Domain : \033[1;33mx.facebook.com
	\033[1;32m[+] Target acc :  \033[1;36m10007568464846
	\033[1;32m[+] Security Level : \033[1;35mMedium
	\033[1;32m[+] Attack has been started
	\033[1;32m[+] Please wait a few minute
	\033[1;32m<==================================>""")

def Nusrat():
	os.system("clear")
	time.sleep(1.5)
	print(logo)
	time.sleep(0.5)
	print(N_F)
	print(" ")
	x = 0

	for x in range(1,51):
		
		time.sleep(0.5)
		c = ["\033[0;37m", "\033[1;37m", "\033[1;31m", "\033[1;35m", "\033[1;33m", "\033[1;32m", "\033[1;34m", "\033[1;36m"]
		o = random.choice(c)
		g = ["6167743","45873771","92090092","83641940","30330469","64992641","86664771","46243662","61250579","27325119","29181012","50804164","76618582","41667030","23282064","31054982","02581684","18104119"]
		f = random.choice(g)
		print("",o,"\n[RASHED] [TG] [",x,"/7665 10007568464846 | ",f,"")
		x =+ 1
	
def Rashed():
	os.system("clear")
	time.sleep(0.5)
	print(" ")
	print("	Thanks For contact me")
	os.system("xdg-open https://www.facebook.com/unavailable1111111111")
	time.sleep(3)
	os.system("clear")
	main()
	
	
main()