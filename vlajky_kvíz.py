from turtle import *
from vlajky import *
from funkce import *
import random

colormode(255)
speed(100)
setup(1280, 800)

# dictionary
vlajky = {
    "česko": cesko,
    "švýcarsko": svycarsko,
    "irsko": irsko,
    "benin": benin,
    "dánsko": dansko,
    "nizozemsko": nizozemsko,
    "mauritius": mauritius,
    "lucembursko": lucembursko,
    "banglades": banglades,
    "rusko": rusko,
    "anglie": anglie,
    "itálie": italie
}
skore = 0
poradi_otazky = 1


soucasne_kolo_vlajky = []
pokracovat_ve_hre = True

while pokracovat_ve_hre:
    # náhodně vyberu 3 vlajky, pokud bude stejná, budu hledat dál
    vyber_vlajky_k_vykresleni(soucasne_kolo_vlajky, vlajky)

    # nakreslím text nahoře
    vlajka_k_hadani = hadame_vlajku(soucasne_kolo_vlajky)
    nakresli_text(poradi_otazky, skore, vlajka_k_hadani)

    # nakreslím 3 vlajky
    nakresli_3_vlajky(vlajky, soucasne_kolo_vlajky)
    print(soucasne_kolo_vlajky)

    # textinput
    odpoved = textinput("Otázka", "Zadejte odpověď: ")
    moznosti = ["A", "B", "C"]
    spravny_index = soucasne_kolo_vlajky.index(vlajka_k_hadani)
    if odpoved.upper() == "KONEC":
        print("Ukončuji hru.")
        pokracovat_ve_hre = False   
    elif moznosti.index(odpoved) == spravny_index:
        skore += 1
    poradi_otazky += 1

soucasne_kolo_vlajky = []
for vlajka in list(vlajky.keys()):
    # náhodně vybere vlajky
    # přidá do soucasne_kolo_vlajky
    if vlajka in soucasne_kolo_vlajky:
        continue
    else:
        soucasne_kolo_vlajky.append(vlajka)


