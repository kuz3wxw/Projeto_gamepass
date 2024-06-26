
def planos_jogos():

    b = print("""Bem-vindo ao catalogo de jogos!\n Agora vamos escolher o plano ideal para você!

        Esses são os planos disponiveis:

        Bronze
Assassin's Creed Rogue Remastered
Bee Simulator
Ben 10: Power Trip
Celeste
Just Cause 4
Killing Floor 2
NBA 2K24 Kobe Bryant Edition for PS4™
SAMURAI WARRIORS 5
Teardown
UNCHARTED 4: A Thief’s End
Valiant Hearts: The Great War™

        R$ 50,00""")
    
    p = print(""" 

        Prata

A Hat in Time
Bee Simulator
Ben 10: Power Trip
Cat Quest II
Celeste
Chess Ultra
Dark Rose Valkyrie
DAVE THE DIVER
Eagle Flight
Earth Defense Force 4.1: The Shadow of New Despair
D BROTHERS
Fade to Silence
FAR CRY 3: BLOOD DRAGON CLASSIC EDITION
Get Even
Ghost of Tsushima DIRECTOR’S CUT (PlayStation Plus)
Hardspace: Shipbreaker
Harvest Moon: Mad Dash
Immortals Fenyx Rising™ PS4 & PS5
Journey To The Savage Planet: Employee Of The Month
JUMANJI: The Video Game
Kena: Bridge of Spirits PS4 & PS5
Killing Floor 2
Lawn Mowing Simulator: Landmark Edition
NBA 2K24 Kobe Bryant Edition for PS4™
Observer: System Redux
Paradise Killer
PAW Patrol Mighty Pups Save Adventure Bay
Rabbids® Invasion
Sackboy: A Big Adventure PS4 & PS5
Salt and Sacrifice
Tails Noir
Tales of Arise PS4 & PS5
UNCHARTED: The Lost Legacy
Undertale

        R$ 80,00""")
            

    o = print("""  

        Ouro

Observer: System Redux
Paradise Killer
PAW Patrol Mighty Pups Save Adventure Bay
Rabbids® Invasion
Sackboy: A Big Adventure PS4 & PS5
Salt and Sacrifice
Tails Noir
Tales of Arise PS4 & PS5
UNCHARTED: The Lost Legacy
Undertale
A Hat in Time
Bee Simulator
Ben 10: Power Trip
Cat Quest II
Celeste
Chess Ultra
Dark Rose Valkyrie
DAVE THE DIVER
Eagle Flight
Earth Defense Force 4.1: The Shadow of New Despair
Observer: System Redux
ODDBALLERS
Oddworld: New 'n' Tasty
Oddworld: Soulstorm Enhanced Edition
Odin Sphere Leifthrasir
The Elder Scrolls V: Skyrim Special Edition - PS5 & PS4
The Evil Within
The Evil Within 2
The Fisherman - Fishing Planet
The Forgotten City
The Gardens Between
The Last Guardian
TRON RUN/r
Tropico 5
Two Point Hospital: JUMBO Edition
Two Point Hospital™


        R$ 150,00""")
    
    print('Digite o nome do plano desejado!')
    bronze = input('Bronze')
    prata = input('Prata')
    ouro = input('Ouro')

    if b =='Bronze':
        print('Voce escolheu o plano Bronze')
    elif p =='Prata':
        print('Voce escolheu o plano Prata')
    elif o == 'Ouro':
        print('Voce escolheu o plano Ouro')
    else:
        print('plano inexistente ')