from tkinter import Y
from matplotlib.style import available
from numpy import number
from selenium import webdriver  
import time
import win32api, win32con
import webbrowser
import os
import os.path


def renameAnime(path, dashplace):
    listofAnime = os.listdir(fr'{path}')
    with open('epList.txt', 'w') as output:
        for episode2 in listofAnime:
            try:
                splitname = episode2.split("-")

                try:

                    sss = splitname[int(dashplace)]
                    ssss = sss[1:]
                    int(ssss[0])
                except:
                    sss = splitname[2]

                ssss = sss[1:]

                numbernamelist = list()

            except:
                time.sleep(0.0001)
                numbernamelist = list()
    
            try:
                int(ssss[0])
                if int(ssss[0]) == 0:
                    time.sleep(0.1)
                else:
                    numbernamelist.append(ssss[0])
                try:
                    int(ssss[1])
                    numbernamelist.append(ssss[1])
                    try:
                        int(ssss[2])
                        numbernamelist.append(ssss[1])
    
                    except:
                        time.sleep(0.1)
                    
                except:
                    time.sleep(0.1)
                
    
            except:
                time.sleep(0.1)
            numbernamelist = ''.join(numbernamelist)
            try:
                os.rename(fr'{path}\{episode2}',fr'{path}\Episode {numbernamelist}.mp4')
                output.write(f"{numbernamelist}\n")
            except:
                time.sleep(0.5)

    output.close()

Coc = True

while Coc == True:
    cc1 = True
    pathOFanimeTOrename = input("Path=")
    DashPlace = int(input("Dash Placement="))
    renameAnime(path=pathOFanimeTOrename,dashplace=DashPlace)
    while cc1 == True:
        ContAns = input("Do You Want To Continue? (Y/N)")
        if ContAns == "Y" or ContAns == "y":
            Coc = True
            cc1 = False
        elif ContAns == "N" or ContAns == "n":
            Coc = False
            cc1 = False
        else:
            print("Invalid Character.\nPlease Try Again.")
            cc1 = True

print("Thanks For Using This App")
