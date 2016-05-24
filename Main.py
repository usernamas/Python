from Vagonas import vagonas
from Lokomotyvas import lokomotyvas
from Traukinys import traukinys
import json
import tkinter as tk
from tkinter import filedialog

'''
train = traukinys(1, 500, 1500)

#print(train.vagonai, train.lok.lokomotyvo_mase, repr(train), train)
vagonas2 = vagonas(2, 500, 1000)
#print(train)
vagonas2 + 950
vagonas2 - 800
vagonas3 = vagonas(3, 600, 3000)
train += vagonas2
train += vagonas3
print(vagonas2)
print(vagonas2.krovinio_mase)
print(train)
train -= vagonas2
print(train)
train -= vagonas3
print(train)
print(vagonas2)
#vagonai +=
#rz = train + vagonas2
#print(rz, repr(vagonas2.vagono_ID))
#print(train)
#print([train, train])
'''
traukiniai = {}

'''Metodas tikrina ar ivesta reiksme yra teigiamas skaicius, jei ne paprasoma
ivesti dar karta'''


def arTinka():
    x = -1
    while(x <= 0):
        try:
            x = int(input("Enter value: "))
        except ValueError:
            print("Wrong input")
            continue
    return x

'''Metodas surusiuoja traukinius ir grazina juos kaip lista'''


def sorting():
    sort = []
    sort2 = []
    for k, v in traukiniai.items():
        sort.append(k)
    sort.sort()
    for el in sort:
        sort2.append(traukiniai[el])
    return sort2


while(True):
    print(
        "1: Kurti traukiny,             2: Prideti vagona,\n"
        "3: Atimti vagona,              4: Pridedi kroviny,\n"
        "5: Atimti kroviny,             6: Gauti traukinio reprezentacija,\n"
        "7: Isrusiuoti traukinius,      8: Issaugoti traukiny JSON formate,\n"
        "9: Ikelti duomenis is JSON,   10: Tikrinti ar traukinys naudojamas,\n"
        "11: Trinti traukiny,          12: Baigti programa")
    print()
    menu = input("Iveskite varianta: ")
    print()
    if(menu == "1"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot = False
        for k, v in traukiniai.items():
            if(k == temp):
                print("Traukinio ID uzimtas")
                pivot = True

        if(pivot is False):
            print("Iveskite lokomotyvo mase: ")
            lm = arTinka()
            print("Iveskite lokomo maximalia tempiamaja mase: ")
            lm_m = arTinka()
            if(lm <= lm_m):
                traukiniai[temp] = traukinys(temp, lm, lm_m)
            else:
                print("Lokomotyvas per sunkus")
                print()

    elif(menu == "2"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue

        print("Iveskite vagono ID: ")
        temp2 = arTinka()
        pivot = False
        for k, v in traukiniai[temp].vagonai.items():
            if(k == temp2):
                print("Vagono ID uzimtas:")
                pivot = True

        if(pivot is False):
            print("Iveskite vagono mase: ")
            vm = arTinka()
            print("Iveskite vagono maximalia krovinio mase: ")
            vm_m = arTinka()
            try:
                if(traukiniai[temp].traukinio_mase + vm <=
                   traukiniai[temp].lok.max_tempiamoji_mase):
                    traukiniai[temp] += vagonas(temp2, vm, vm_m)
                else:
                    print("Vagonas per sunkus")
            except:
                print("Pridekite vagona su kitu ID")
            print("Traukinio mase: ", traukiniai[temp].traukinio_mase,
                  "| Vagonai: ", len(traukiniai[temp]))

    elif(menu == "3"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue

        print("Iveskite vagono ID: ")
        temp2 = arTinka()
        pivot = False
        for k, v in traukiniai[temp].vagonai.items():
            if(k == temp2):
                print("Vagono ID uzimtas:")
                pivot = True

        if(pivot is True):
            try:
                traukiniai[temp] -= traukiniai[temp].vagonai[temp2]
            except:
                print("Vagonas nerastas")
        else:
            print("Vagonas nerastas")
        print("Traukinio mase: ", traukiniai[temp].traukinio_mase,
              "| Vagonai: ", len(traukiniai[temp]))

    elif(menu == "4"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue

        print("Iveskite vagono ID: ")
        temp2 = arTinka()
        pivot = False
        for k, v in traukiniai[temp].vagonai.items():
            if(k == temp2):
                print("Vagono ID uzimtas:")
                pivot = True
        if(pivot is False):
            print("Vagonas nerastas")
            print()
            continue

        print("Iveskite krovinio mase: ")
        mase = arTinka()
        print()
        if(mase + traukiniai[temp].vagonai[temp2].krovinio_mase <=
           traukiniai[temp].vagonai[temp2].max_krovinio_mase and
           mase + traukiniai[temp].traukinio_mase <=
           traukiniai[temp].lok.max_tempiamoji_mase):
            traukiniai[temp].vagonai[temp2] += mase
            traukiniai[temp].traukinio_mase += mase
        else:
            print("Krovinys per sunkus")
            print()
        print("Krovinio mase: ", traukiniai[temp].vagonai[temp2].krovinio_mase,
              "| Traukinio mase: ", traukiniai[temp].traukinio_mase,
              "\nMax krovinio mase: ",
              traukiniai[temp].vagonai[temp2].max_krovinio_mase,
              "| Max tempiamoji mase: ",
              traukiniai[temp].lok.max_tempiamoji_mase)

    elif(menu == "5"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue

        print("Iveskite vagono ID: ")
        temp2 = arTinka()
        pivot = False
        for k, v in traukiniai[temp].vagonai.items():
            if(k == temp2):
                print("Vagono ID uzimtas:")
                pivot = True

        print("Iveskite krovinio mase: ")
        print()
        mase = arTinka()
        if(mase <= traukiniai[temp].vagonai[temp2].krovinio_mase):
            traukiniai[temp].traukinio_mase -= mase
            traukiniai[temp].vagonai[temp2] -= mase
        else:
            print("Krovinys per sunkus")
            print()
        print("Krovinio mase: ", traukiniai[temp].vagonai[temp2].krovinio_mase,
              "| Traukinio mase: ", traukiniai[temp].traukinio_mase,)

    elif(menu == "6"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        print()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue

        print(repr(traukiniai[temp]))

    elif(menu == "7"):
        listas = sorting()
        print("---------------------------------------------------------")
        for el in listas:
            print(el)
            print("---------------------------------------------------------")

    elif(menu == "8"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue
        name = input("Iveskite failo pavadinima: ")
        train = {}
        vag = {}
        for k, v in traukiniai[temp].vagonai.items():
            vagon = {}
            vagon = {
                    "Vagono_ID": traukiniai[temp].vagonai[k].vagono_ID,
                    "Vagono_mase": traukiniai[temp].vagonai[k].vagono_mase,
                    "Vagono_krovinio_mase":
                    traukiniai[temp].vagonai[k].krovinio_mase,
                    "Vagono_maximali_krovinio_mase":
                    traukiniai[temp].vagonai[k].max_krovinio_mase
                     }
            vag[traukiniai[temp].vagonai[k].vagono_ID] = vagon
        train[temp] = {
            'traukinio_ID': traukiniai[temp].traukinio_ID,
            'traukinio_mase': traukiniai[temp].traukinio_mase,
            'lok': {
                'lokomotyvo_mase': traukiniai[temp].lok.lokomotyvo_mase,
                'max_tempiamoji_mase': traukiniai[temp].lok.max_tempiamoji_mase
            },
            'vagonai': vag
        }
        s = json.dumps(train)
        with open("C://Users//Inspiron//PycharmProjects//untitled5//" + name +
                  ".json", "w") as f:
            f.write(s)

    elif(menu == "9"):
        print("Pasirinkite: 1 - ivesti failo pavadinima,"
              " 2 - jei norite pasirinkti faila ")
        choice = arTinka()
        if(choice == 1):
            name = input("Iveskite failo pavadinima: ")
            f = open("C://Users//Inspiron//PycharmProjects//untitled5//" +
                     name + ".json", "r")
        elif(choice == 2):
            root = tk.Tk()
            root.withdraw()
            f = open(filedialog.askopenfilename(), "r")
        else:
            print("Skaiciu per didelis")
            continue

        s = f.read()
        train = json.loads(s)
        for k, v in train.items():
            traukiniai[int(k)] = traukinys(v['traukinio_ID'],
                                           v['lok']['lokomotyvo_mase'],
                                           v['lok']['max_tempiamoji_mase'])

            for x, y in train[k]['vagonai'].items():
                traukiniai[int(k)] += vagonas(
                        int(y['Vagono_ID']), y['Vagono_mase'],
                        y['Vagono_maximali_krovinio_mase'],
                        y['Vagono_krovinio_mase'])
                traukiniai[int(k)].traukinio_mase += y['Vagono_krovinio_mase']

            print()
            print(traukiniai[int(k)])

    elif(menu == "10"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        print()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue
        if(bool(traukiniai[temp])):
            print("Traukinys naudojamas")
        else:
            print("Traukinys nenaudojamas")
        print()

    elif(menu == "11"):
        print("Iveskite traukinio ID: ")
        temp = arTinka()
        pivot2 = False
        for k, v in traukiniai.items():
            if(k == temp):
                pivot2 = True
        if(pivot2 is False):
            print("Traukinys nerastas")
            print()
            continue
        try:
            del traukiniai[temp]
        except:
            print("Ivyko klaida")

    elif(menu == "12"):
        exit(1)
    else:
        print("Wrong input")

    print()
