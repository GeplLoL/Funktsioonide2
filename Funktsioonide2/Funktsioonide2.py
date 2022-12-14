from math import *
from random import *
#1
print("")
print("Puu läbimõõdu arvutamine")
try:
    C = float(input("mis on ümbermõõt: "))
    if C>0:
        d = C / pi 
        print("Puu läbimõõt: ",round(d,2))
    else:
        print("C peab olema suurem kui 0")    
except:
    print("Andmetüüp on vale!")
#2
print("")
try:
    print("pikk on ristkülikukujulise maatüki diagonaal")
    N = float(input("Sisestage number N: "))
    M = float(input("Sisestage number M:"))
    if N>0 and M>0:
        d = sqrt(N**2+M**2)
        print(" pikk on ristkülikukujulise maatüki diagonaal", round(d,2), "m")
    else:
        print("N ja M peab olema suurem kui 0")
except:
    print("Andmetüüp on vale!")
#3
print("")
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    if aeg>0 and teepikkus>0:
        kiirus = teepikkus / aeg
        print("Sinu kiirus oli " + str(kiirus) + " km/h")
    else:
        print("tundi ja kilomeetrit peab olema suurem kui 0")
except:
    print("Andmetüüp on vale!")
#4
try:
    print("")
    firstNum = int(input("First number: "))
    secondNum = int(input("Second number: "))
    thirdNum = int(input("Third number: "))
    fourthNum = int(input("Fourth number: "))
    fifthNum = int(input("Fifth number: "))
    average = (firstNum+secondNum+thirdNum+fourthNum+fifthNum)/5
    print("keskmine:",average)
except:
    print("Andmetüüp on vale!")
#5
print("")
print('   @..@\n  (----)\n ( \__/ )\n^^ "" ^^')
#6
print("")
try:
    a = float(input("sisestage esimene pool: "))
    b = float(input("sisestage teise pool: "))
    c = float(input("sisestage kolmas pool: "))
    if a>0 and b>0 and c>0:
        print(a+b+c)
    else:
        print("a, b, c peab olema suurem kui 0")

except:
    print("Andmetüüp on vale!")
#7
print("")
try:
    friend = int(input("kui palju sõpru? "))
    hind = float(input("kui palju on pizza? "))/friend
    protsent = float(input("protsent? "))
    if friend>0 and hind>0 and protsent>0:
        allahindlust = hind*protsent/100
        total = allahindlust+hind
        print("total hind: ", round(total,2))
    else:
        print("pizza,sõpru,protsent peab olema suurem kui 0")
except:
    print("Andmetüüp on vale!")
#random #6
print("")
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
#8
print("")
try:
    läbitudVahemaa = float(input("läbitud vahemaa: "))
    täidetudKütuseKogus = float(input("täidetud kütuse kogus: "))
    if läbitudVahemaa>0 and täidetudKütuseKogus>0:
        kütust = täidetudKütuseKogus/läbitudVahemaa*100
        print(kütust,"km/l")
    else:
        print("läbitud ja täidetud peab suurem kui 0")
except:
    print("Andmetüüp on vale!")
#9
print("")
try:
    killometr = float(input("teie kiirus km/h: "))
    if killometr>0:
        total = killometr*1000/60
        print("keskmine kiirus:", round(total,2),"m/m")
    else:
        print("kirrus peab suurem kui 0")
except:
    print("Andmetüüp on vale!")
#10
print("")
try:
    M = int(input("sisestage minutid: "))
    if M>0:
        H = M//60
        M = M%60

        print(f"{H}:{M}")
    else:
        print("min peab suurem kui 0")
except:
    print("Andmetüüp on vale!")
print("")
print("Ema roobot")
print("mis hinde sa koolis said?")
laps = int(input(""))
if laps==1:
    print("Ema: sa oled  väga halb")
elif laps==2:
    print("sa oled halb")
elif laps==3:
    print("sa oled normalse")
elif laps==4:
    print("sa oled hästi")
elif laps==5:
    print("sa oled väga hästi") 
elif laps>=6:
    print("miks sa mulle valetad?")
elif laps<=0:
    print("miks sa mulle valetad?")
else:
    print("error")