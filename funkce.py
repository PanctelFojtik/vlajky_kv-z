import random
from turtle import *

def vyber_vlajky_k_vykresleni(list_s_vlajkami, nazev_slovniku_s_vlajkami):
    while len(list_s_vlajkami) < 3:
        nah_vyber = random.choice(list(nazev_slovniku_s_vlajkami.keys()))
        pocet_zbyvajicich_vlajek = len(list(nazev_slovniku_s_vlajkami.keys()))
        if not nah_vyber in list_s_vlajkami:
            list_s_vlajkami.append(nah_vyber)
        elif pocet_zbyvajicich_vlajek < 3:
            print("Konec hry. Nezbylo dost vlajek.")
            break
        else:
            continue

def hadame_vlajku(list_s_vlajkami):
    return random.choice(list_s_vlajkami)

def nakresli_text(poradi_otazky, skore, hadame_vlajku):
    penup()
    goto(-600,310)
    write(f"Která vlajka je {hadame_vlajku}? Napište A, B nebo C: ", font=("Arial", 30))
    goto(-120, -340)
    write(f"Otázka č. {poradi_otazky}. Skóre: {skore}.", font=("Arial", 20))
    return hadame_vlajku

def nakresli_3_vlajky(slovnik_s_vlajkami, list_s_vlajkami):
    startx_vlajky = -450
    starty_vlajky = -150
    for vlajka in list_s_vlajkami:
        slovnik_s_vlajkami[vlajka](startx_vlajky, starty_vlajky)
        startx_vlajky += 320

