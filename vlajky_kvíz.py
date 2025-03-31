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



pokracovat_ve_hre = True

while pokracovat_ve_hre:
    penup()
    pencolor("black")
    soucasne_kolo_vlajky = []
    # náhodně vyberu 3 vlajky, pokud bude stejná, budu hledat dál
    pokracovat_ve_hre = vyber_vlajky_k_vykresleni(soucasne_kolo_vlajky, vlajky) # funkce vrátí True nebo False

    # nakreslím text nahoře
    vlajka_k_hadani = hadame_vlajku(soucasne_kolo_vlajky)
    print(f"Toto je vlajka k hádání: {vlajka_k_hadani}")
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
    elif odpoved.upper() in moznosti and moznosti.index(odpoved.upper()) == spravny_index:
        skore += 1
        odstran_pouzitou_vlajku(vlajky, vlajka_k_hadani)
        clear()
    else:
        poradi_otazky += 1
        odstran_pouzitou_vlajku(vlajky, vlajka_k_hadani)
        clear()


