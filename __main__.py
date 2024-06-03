#Import důležitých knihoven


# from sense_emu import * #Na reálném sense hat
from sense_hat import * #Na trinket.io

from time import sleep
import random
import math

#Funkce kde si uživatel vybýrá kolik chce "kol"
def Zacatek():
    #Pole číšel od 1 do 9
    ONE = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        ]
    TWO = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,
        ]
    THREE = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        ]
    FOUR = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        ]
    FIVE = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        ]
    SIX = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        ]
    SEVEN = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,
        ]
    EIGHT = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        ]
    NINE = [
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,WHITE,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,
        BLACK,BLACK,BLACK,BLACK,BLACK,WHITE,BLACK,BLACK,
        BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,BLACK,
        ]
    
    #Pole pro jednodušší indexování ve while
    numbers = [ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    #Pre-selectnutý kolo
    selected = 4
    loop = True
    while loop:
        #Zobrazování vybraného čísla
        hat.set_pixels(numbers[selected])
        #Kontrola toho co uživatel zmáčknul
        for event in hat.stick.get_events():
            direction = event.direction
            action = event.action
            #if nahoru tak se přidá +1 k selected = index, tím pádem se zvětší selected číslo
            if direction == 'up' and action == 'pressed' and selected != 8:
                selected += 1
            #if dolu tak se přidá -1 k selected = index, tím pádem se zmenší selected číslo
            elif direction == 'down' and action == 'pressed' and selected != 0:
                selected -= 1
            #Pokud uživatel zmáčkně prostřední tlačítko tak se vypne výběr loop a přejde se do hry v main loopu
            elif direction == 'middle':
                loop = False
    #vrátí to počet vybraných "kol"
    return selected+1

#Metoda pro generaci prvotní mapy (ano šlo by použít fuknce "NewLine" ale takto to je přehlednější)
def GenerateMap():
    #Deklarace že tato promněnná je globální abych ji mohl upravovat uvnitř metody
    global PlayerBlock
    #Přidání místa do pole + předvygenerovýní první line
    for i in range(64):
        if i < 8:
            #První line
            array.append(random.choice(POINTS_ARRAY))
        else:
            #Tmavé (prázdné) políčka
            array.append(BLACK)
    #Výběr random "blocku" (barvy kterou uživatel má)
    array[PlayerPosition] = random.choice(PLAYER_POINTS_ARRAY)
    #Přidání hráče do pole 
    PlayerBlock = array[PlayerPosition]
    
#Metoda pro blikání všech led
def BlickScreen(color):
    #for pro 3
    for i in range(3):
        #Černá
        hat.clear(BLACK)
        #Čekání
        sleep(0.5)
        #Červená
        hat.clear(color)
        #Čekání
        sleep(0.5)
        
#Metoda pro chození hráče
def Movement():
    #Globalizace promněnné
    global PlayerPosition
    loop = True
    #Loop pro pohyb
    while loop:
        #Kontrola eventu
        for event in hat.stick.get_events():
            direction = event.direction
            action = event.action
            
            #If zmáčkné doprava => změna pozice hráče
            if direction == 'right' and action == 'pressed':
                if PlayerPosition != 63:
                    PlayerPosition += 1
                    array[PlayerPosition-1] = BLACK
                    array[PlayerPosition] = PlayerBlock
            if direction == 'left' and action == 'pressed':
                if PlayerPosition != 56:
                    PlayerPosition -= 1
                    array[PlayerPosition+1] = BLACK
                    array[PlayerPosition] = PlayerBlock
            if direction == 'middle' and action == 'pressed':
                loop = False
        #Zobrazení pole = zobrazení hrací plochy = zobrazení změn
        hat.set_pixels(array)

#Funkce pro "animaci" "výstřelu"
'''
    Tato funkce dělá animaci = posouvá jednu barvu pomalu dolů =>
    musíme jednu led rozsvítít, poté ji zasnou, rozsvítít pozici nad tím
    to je tady řešeno celkem chaoticky ale i s vyjímkou zasínání když tam je hráč
'''
def ShootProjectile():
    #uložení pozice hráče = pozice ze které poletí "střela"
    projectile = PlayerPosition
    #Animace loop
    while True:
        #Změna pozice projektilu o -8 = posunutí o jedno nahoru (protože pole je 8x8 = když zmenšíme o 8 tak se dostaneme o jedno "nahoru")
        projectile -= 8
        '''
        Jelikož na začátku odečítám "pozici" tak pokud to bude mimo "pole" ale i led tak se vykoná else =
        = OŠETŘENÍ CHYBY
        '''
        if projectile >= 0:
            #Vrácení pozice projectilu
            if array[projectile] != BLACK:
                return projectile+8
            #Pokud bude projectil pod hráčem tak se ta led za projectilem nezmění na černou = ošetření "bugu"
            if projectile + 8 != PlayerPosition:
                array[projectile + 8] = BLACK
            #Změnění barvu projektilu na barvu kterou má mít
            array[projectile] = PlayerBlock
            #Sleep pro "animaci"
            sleep(0.5)
        else:
            #Změnění finální barvy projectilu na finální pozici = ta pozice 
            array[projectile+8] = PlayerBlock
            #Vrácení pozice projectilu
            return projectile+8
        #Aktualizace led = aktualizace pozic
        hat.set_pixels(array)

'''
    Kontrola bodů v poli jestli mají zmizet nebo zůstat
    Je to vyřešeno tak že:
    
    První bod po dopadu se změní na žlutou barvu, poté se projíždí celé pole a pokud s narazí na pozici v poli s
    žlutou barvou tak se zkontroluje jestli... nad, pod, v levo a v pravo, nejsou barvy stejné jako je vystřelená
    barva projectilu, pokud ano tak se tato pozice také změní na žlutou a celé pole se odznova projede.
    
    Pokud už to nenarazí na žádné další podobné a vedle sebe "block"(pozice) tak loop skončí a všechny žluté pozice
    se změní na prázdno a SenseHat led se "aktualizuje" = dá se tam to nové upravené pole
'''
def PointsControl(projectile):
    #Globalizace
    global array
    #Vytvoření nového pole které je stejné jako to předchozí pro "Bezpečnější úpravu"
    new_array = array
    #Barva kam doletěl projectil tak se změní na žluto aby byl "startovní" bod
    new_array[projectile] = YELL
    
    #Počet pozic v poli (počet led (když se počítá od 0))
    i = 63
    while i >= 0:
        #Pokud najdeme žlutou
        if new_array[i] == YELL:
            #OŠETŘENÍ CHYBY (OUT OF ARRAY BOUNDS)
            #Pod
            if i + 8 <= 63:
                if new_array[i+8] == PlayerBlock:
                    new_array[i+8] = YELL
                    i = 63
            #OŠETŘENÍ CHYBY (OUT OF ARRAY BOUNDS)
            #Nad
            if i - 8 >= 0:
                if new_array[i-8] == PlayerBlock:
                    new_array[i-8] = YELL
                    i = 63
            #OŠETŘENÍ CHYBY (OUT OF ARRAY BOUNDS)
            #V pravo
            if i + 1 <= 63: 
                if new_array[i+1] == PlayerBlock:
                    new_array[i+1] = YELL
                    i = 63
            #OŠETŘENÍ CHYBY (OUT OF ARRAY BOUNDS)
            #V levo
            if i - 1 >= 0:
                if new_array[i-1] == PlayerBlock:
                    new_array[i-1] = YELL
                    i = 63
        i-= 1
        
    yellpocet = 0
    #Zjištění kolik je žlutých polí v poli (kolik polí musímě vymazat)
    #+ Smazání těch pozic = dát je na černou barvu
    for i in range(len(new_array)):
        if new_array[i] == YELL:
            yellpocet += 1
            new_array[i] = BLACK
    #Pokud je v poli jen jeden žlutý => ten projectil co doletěl, takže ho tam chceme nechat a nic nemazat
    #Zobrazení barvy projectilu (protože ho nahoře dáváme na BLACK jako všechny žluté v poli
    if yellpocet == 1:
        new_array[projectile] = PlayerBlock
        
    #Aktualizace SenseHat
    array = new_array
    
#Funkce pro přidání nového řádku + zjištění pokud uživatel neprohrál
def NewLine():
    #Globalizace
    global array
    #Nové pole
    new_array = []
    #Loop který nám vytvoří "pozice" v poli (abych to nemusel psát ručně)
    for i in range(len(array)):
        new_array.append(BLACK)
    #Naplnění nového pole za to co bylo ve starém a posunuté o jedno dolu
    #(až na poslední pozici, tam je hráč a je to nepotřebné)
    for i in range(len(array)-8):
        new_array[i+8] = array[i]
    #Kontrola posledního řádku (už posunuté) = pokud ten řádek není prázdný tak hráč prohrál  
    for i in range(len(array)-8,len(array)):
        if new_array[i] != BLACK:
            #Vyvolání metody pro blikání všech led podle určené barvy
            #GAME OVER
            BlickScreen(RED)
            return False
    #Naplnění vzniklého prázdného řádku za nové random barvy 
    for i in range(8):
        new_array[i] = random.choice(POINTS_ARRAY)
    
    #Globalizace
    global PlayerBlock
    #Výběr nového "blocku" (barvy) kterou uživatel bude mít a bude ji používat v dalším kole
    PlayerBlock = random.choice(PLAYER_POINTS_ARRAY)
    #Změna barvy hráče (aby se zobrazila v poli/na led)
    new_array[PlayerPosition] = PlayerBlock
    #Změna pole za toto nově vzniklé
    array = new_array
    #Zobrazení nové hrací plochy
    hat.set_pixels(array)
    return True

#SenseHat inicializace
hat = SenseHat()

#Deklarace barev
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (250,20,147)
YELL = (255,255,0)

#Deklarace pole pro lehčí výběr s RANDOM
POINTS_ARRAY = [RED,GREEN,BLUE]
PLAYER_POINTS_ARRAY = [RED,GREEN,BLUE]

#Pozice hráče
PlayerPosition = 59
#Jakou barvu má uživatel (kterou barvu střílí)
PlayerBlock = WHITE
#Pole ve kterém vše "upravuji" a pak ho zobrazuji na LED
array =[]

################################################

#Vyber kolik chce uživatel "kol"
wave = Zacatek()
#Vygenerování mapy
GenerateMap()
#Zobrazené mapy
hat.set_pixels(array)

#GAME LOOP
while True:
    #Pohyb hráče
    Movement()
    #Vystřelení projektilu a kontrola => mazání
    PointsControl(ShootProjectile())
    #Kontola pokud se bude poslední řada dotýkat hráče tak konec hry
    if NewLine() == False:
        break
    #Kontrola kolik zbývá kol => if == 0 výhra
    if wave == 0:
        #Metoda pro blikání všech LED
        BlickScreen(GREEN)
        break
    #Odečítání kola po dohrání kola
    wave -=1