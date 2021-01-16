from CustomCI import CustomInput, CustomPrint
import os

def InstallTermuxDependencies() : 
    CustomPrint("Installing dependencies...")
    CustomPrint("Updating Termux")
    os.system('apt update')
    CustomPrint("Allow storage permission for storing extraced whatsapp.ab in interal storage.")
    os.system('termux-setup-storage')
    CustomPrint("Done. Installing various required components.")
    os.system('apt install curl grep fish tar proot wget -y')
    CustomPrint("Done. Installing ADB for Termux")
    os.system('wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh')
    CustomPrint("Done. Installing Java for termux.")
    os.system('wget https://raw.githubusercontent.com/Hax4us/java/master/installjava && sh installjava')
    CustomPrint("Done installing all dependencies. Now running proot.")
    os.system('fish')
    os.system('proot login')

InstallTermuxDependencies()