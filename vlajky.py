from turtle import *
def irsko(startx, starty, sirka=300, vyska=200): 
    seth(0)
    goto(startx + sirka/2 + sirka/6, starty)
    sirka /= 3
    penup()
    pendown()
    fillcolor("#FF8200")
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska)
        left(90)
    end_fill()
 
    # druha
    left(180)
    fd(sirka)
 
    # druha
    for _ in range(2):
        left(-90)
        forward(vyska)
        left(-90)
        forward(sirka)
       
    # treti
    fd(sirka)
    begin_fill()
    fillcolor("#169B62")
 
    # treti
    for _ in range(2):
        left(-90)
        forward(vyska)
        left(-90)
        forward(sirka)
 
    end_fill()
def svycarsko(startx, starty, sirka=300, vyska=300): 
    seth(0)
    goto(startx, starty)
    pencolor('red')
    hideturtle()
    fillcolor('red')
    begin_fill()
 
    for x in range(4):
        forward(sirka)
        left(90)
    end_fill()
    goto(startx + sirka/5, starty + sirka/2.5)
    fillcolor('white')
    begin_fill()
    for x in range(2):
        forward(sirka/1.66666)
        left(90)
        forward(sirka/5)
        left(90)
    end_fill()
    pencolor('red')
    goto(startx + sirka/2.5, starty + sirka/5)
    fillcolor('white')
    begin_fill()
    for x in range(2):
        pencolor('white')
        forward(sirka/5)
        left(90)
        forward(sirka/1.66666666)
        left(90)
    penup()
    end_fill()
def cesko(startx, starty, sirka=300, vyska=200):
    seth(0)
    barvy = [(215, 20, 26), (17, 69, 126), (255, 255, 255)] # červená, modrá, bílá
    goto(startx, starty)
    #bílý obdélník
    fillcolor(barvy[2])
    begin_fill()
    pendown()
    for x in range(2): 
        forward(sirka)
        left(90)
        forward(vyska)
        left(90)
    end_fill()
    penup()
    #červený obdélník
    fillcolor(barvy[0])
    begin_fill()
    forward(sirka)
    left(90)
    forward(vyska / 2)
    left(90)
    forward(sirka / 2)
    goto(startx, starty)
    end_fill()
    # modrý trojúhelník
    fillcolor(barvy[1])
    begin_fill()
    goto(startx + sirka/2, starty + vyska/2)
    goto(startx, starty + vyska)
    goto(startx, starty)
    end_fill()
def benin(startx, starty, sirka=300, vyska=200):
    seth(0)
    penup()
    goto(startx,starty)
    pendown()
    
    fillcolor(0, 135, 81)
    begin_fill()
    forward(0.3*sirka)
    left(90)
    forward(vyska)
    left(90)
    forward(0.3*sirka)
    left(90)
    forward(vyska)
    left(90) 
    end_fill()
    forward(0.3*sirka)

    fillcolor(232,17,45)
    begin_fill()
    forward(0.7*sirka)
    left(90)
    forward(0.5*vyska)
    left(90)
    forward(0.7*sirka)
    left(90)
    forward(0.5*vyska)
    left(90) 
    end_fill()

    left(90)
    forward(0.5*vyska)
    right(90)

    fillcolor(252,209,22)
    begin_fill()
    forward(0.7*sirka)
    left(90)
    forward(0.5*vyska)
    left(90)
    forward(0.7*sirka)
    left(90)
    forward(0.5*vyska)
    left(90)
    end_fill()
    penup()
def dansko(startx, starty, sirka=300, vyska=200):
    seth(0)
    starty += vyska #korekce učitele
    barva = 187,12,47
    dilekx = sirka / 37
    dileky = vyska / 28
    penup()
    goto(startx, starty)
    def cast():
        fillcolor(barva)
        begin_fill()
        for x in range(2):
            forward(dilekx * 12)
            left(270)
            forward(dileky * 12)
            left(270)
        end_fill()
        penup()
        forward(dilekx * 16)
        fillcolor(barva)
        begin_fill()
        for z in range(2):
            forward(dilekx * 21)
            left(270)
            forward(dileky * 12)
            left(270)
        end_fill()
    cast()
    goto(startx, starty - (dileky * 16))
    cast()
    goto(startx, starty - vyska)
    for y in range(2):
        pendown()
        forward(sirka)
        left(90)
        forward(vyska)
        left(90)
def nizozemsko(startx, starty, sirka=300, vyska=200):
    seth(0)
    starty += vyska*2/3 #korekce učitele
    barvy = [(206, 17, 38), (255, 255, 255), (0, 32, 91)] 
    goto(startx, starty)
    
    fillcolor(barvy[0])
    begin_fill()
    for x in range(2): 
        forward(sirka)
        left(90)
        forward(vyska / 3)
        left(90)
    end_fill()
    penup()
    
    goto(startx, starty - vyska / 3)
    fillcolor(barvy[1])
    begin_fill()
    for x in range(2): 
        forward(sirka)
        left(90)
        forward(vyska / 3)
        left(90)
    end_fill()
    penup()

    goto(startx, starty - (vyska / 3) * 2)
    fillcolor(barvy[2])
    begin_fill()
    for x in range(2): 
        forward(sirka)
        left(90)
        forward(vyska / 3)
        left(90)
    end_fill()
def mauritius(startx, starty, sirka = 300, vyska = 200):
    seth(0)
    #RGB barvy
    colormode(255)
 
    #Pernamentní nastavení
    shape("turtle")
    hideturtle()
    speed(100)
 
    #Zelená
    penup()
    goto(startx, starty)
    pencolor(0, 134, 88)
    pensize(2)
    pendown()
    fillcolor(0, 134, 88)
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 4)
        left(90)
    end_fill()
 
    #Žlutá
    penup()
    right(-90)
    forward(vyska / 4)
    left(-90)
    pencolor(247,183, 24)
    pensize(2)
    pendown()
    fillcolor(247,183, 24)
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 4)
        left(90)
    end_fill()
   
    # #Modrá
    penup()
    right(-90)
    forward(vyska / 4)
    left(-90)
    pencolor(45, 51, 89)
    pensize(2)
    pendown()
    fillcolor(45, 51, 89)
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 4)
        left(90)
    end_fill()
 
    # #červená
    penup()
    right(-90)
    forward(vyska / 4)
    left(-90)
    pencolor(208, 28, 31)
    pensize(2)
    pendown()
    fillcolor(208, 28, 31)
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 4)
        left(90)
    end_fill()
    penup()
def lucembursko(startx, starty, sirka=300, vyska=200):
    seth(0)
    barvy = [(0, 140, 255), (255, 255, 255), (237, 41, 57)]
    hideturtle()
    penup()
    goto(startx, starty)
    pendown()
    
    fillcolor(barvy[0])
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 3)
        left(90)
    end_fill()
    
    penup()
    goto(startx, starty + vyska / 3)
    pendown()
    
    fillcolor(barvy[1])
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 3)
        left(90)
    end_fill()
    
    penup()
    goto(startx, starty + 2 * (vyska / 3))
    pendown()

    fillcolor(barvy[2])
    begin_fill()
    for _ in range(2):
        forward(sirka)
        left(90)
        forward(vyska / 3)
        left(90)
    end_fill()
    penup()
def banglades(STARTX, STARTY, SIRKA=300, VYSKA=200):
    seth(0)
    # Zelená barva pozadí
    penup()
    barvy = [(0, 106, 78), (206, 32, 41)]  # Zelená, červená
    goto(STARTX, STARTY)
    # Zelený obdélník (pozadí)
    fillcolor(barvy[0])
    begin_fill()
    for x in range(2):
        forward(SIRKA)
        left(90)
        forward(VYSKA)
        left(90)
    end_fill()
    
    penup()
    goto(STARTX + SIRKA / 2, STARTY + VYSKA / 2)
    pendown()
    
    # Červený kruh uprostřed (symbol)
    radius = VYSKA / 5  # Poloměr kruhu
    fillcolor(barvy[1])
    dot(100, 244, 42, 65)
def rusko(startx, starty, sirka=300, vyska=200):
    seth(0)
    starty += vyska # korekce učitele
    pruh_vyska = vyska / 3
    
    penup()
    goto(startx, starty)
    pendown()
    
    begin_fill()
    fillcolor("white")
    forward(sirka)
    right(90)
    forward(pruh_vyska)
    right(90)
    forward(sirka)
    right(90)
    forward(pruh_vyska)
    right(90)
    end_fill()
    
    penup()
    goto(startx, starty - pruh_vyska)
    pendown()
    
    begin_fill()
    fillcolor("blue")
    forward(sirka)
    right(90)
    forward(pruh_vyska)
    right(90)
    forward(sirka)
    right(90)
    forward(pruh_vyska)
    right(90)
    end_fill()
    
    penup()
    goto(startx, starty - 2 * pruh_vyska)
    pendown()
    
    begin_fill()
    fillcolor("red")
    forward(sirka)
    right(90)
    forward(pruh_vyska)
    right(90)
    forward(sirka)
    right(90)
    forward(pruh_vyska)
    right(90)
    end_fill()
    penup()
def anglie(startx, starty, sirka=300, vyska=200):
    seth(0)
    pendown()
    startx += sirka/2
    goto(startx, starty)
    hideturtle()
    pensize(1)
    pencolor("black")
    forward(sirka / 2)
    left(90)
    forward(vyska)
    left(90)
    forward(sirka)
    left(90)
    forward(vyska)
    left(90)
    forward(sirka / 2)

    pencolor("red")
    pensize(30)
    left(90)
    forward(vyska)
    left(180)
    forward(vyska / 2)
    left(90)
    forward(sirka / 2)
    left(180)
    forward(sirka)
    pensize(0)
    penup()
def italie(startx, starty, sirka = 300, vyska = 180):
    seth(0)
    startx += sirka/2 # korekce učitele
    starty += vyska/2 # korekce učitele   
    fillcolor(0, 146, 70)
    penup()
    goto(startx - 150, starty - 90)
    pendown()
    for x in range(2):
        forward(sirka)
        left(90)
        forward(vyska)
        left(90)

    def cast():
        for x in range(2):
            left(90)
            forward(vyska)
            left(90)
            forward(sirka / 3)

    penup()
    goto(startx - 50 , starty - 90)
    pendown()
    begin_fill()
    cast()
    end_fill()
    fillcolor(206, 43, 55)
    penup()
    goto(startx + 150, starty - 90)
    pendown()
    begin_fill()
    cast()
    end_fill()
    penup()