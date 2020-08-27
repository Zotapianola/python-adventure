from termcolor import colored
import random
import time
import sys

castle = """
                                                     o
                                                 _---|         _ _ _ _ _
                                              o   ---|     o   ]-I-I-I-[
                             _ _ _ _ _ _  _---|      | _---|    \ ` ' /
                             ]-I-I-I-I-[   ---|      |  ---|    |.   |
                              \ `   '_/       |     / \    |    | /^\|
                               [*]  __|       ^    / ^ \   ^    | |*||
                               |__   ,|      / \  /    `\ / \   | ===|
                            ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
                            I_I__I_I__I_I  (====(_________)___|_|____|____
                            \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
                             |[]      '|   | []  |`__  . [  \-\--|-|--/-/
                             |.   | |' |___|_____I___|___I___|---------|
                            / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
                           <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \
                           ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
                           ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [
                           <===>     ' ||||| |   |   | ||||.||  []   <===>
                            \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
                             |      . _||||| |   |   | ||||.|| |     | |
                          ../|' v . | .|||||/____|____\|||| /|. . | . ./
                           |//\............/...........\........../../\\\

"""


HIGH_HP = 100
LOW_HP = 50
# PLAYER_HP = 0

def start_game():
    print(castle)
    print(colored("Manuk dice: ", "magenta"))
    print(colored("Como te llamas?... Dime tu nombre... No recuerdo la ultima vez que alguien me vino a ver", "magenta"))
    player_name = input("Escribe tu nombre: ")
    print("Te has identificado como: ", player_name)
    print(colored("Manuk dice: ", "magenta"))
    print(colored("... \n... \n Hola %s... que raro tu nombre, se nota que no eres de aqui... " % (player_name), "magenta"))

def propose_game():
    print(colored("Manuk dice: ", "magenta"))
    print(colored("Te propongo una aventura... ", "magenta"))
    time.sleep(1)
    print(colored("Vamos a tirar un dado de 6 caras...", "magenta"))
    time.sleep(1)
    print(colored("Si el dado es mayor a 3... tu aventura parte con %s de vida" % str(HIGH_HP), "magenta"))
    time.sleep(1)
    print(colored("Si el dado es menor a 3... tu aventura parte con %s de vida" % str(LOW_HP), "magenta"))
    time.sleep(1)
    print(colored("Si el dado es 3... debes reintentar..." , "magenta"))
    time.sleep(2)
    print(colored("SUERTE... la vas a necesitar" , "magenta"))
    time.sleep(3)

def check_dice(dice):
    global PLAYER_HP
    while True:
        if dice < 3:
            print(colored("Dado menor a 3 :'(", "red", attrs=['bold']))
            PLAYER_HP = LOW_HP
            time.sleep(1)
            print(colored("Bien... pero pudo ser mejor... tu aventura ha partido con un HP de %s" % str(PLAYER_HP), "magenta", attrs=['bold']))
            return dice
        elif dice > 3:
            print(colored("Dado mayor a 3","green", attrs=['bold']))
            PLAYER_HP = HIGH_HP
            time.sleep(1)
            print(colored("Felicidades!!!",  "magenta", attrs=['bold']))
            time.sleep(1)
            print(colored("Sorprendente... tu aventura ha partido con un HP de %s :)" % str(PLAYER_HP), "magenta", attrs=['bold']))
            return dice
        else:
            print("Dado igual a 3, se lanza de nuevo")
            time.sleep(1)

            
def roll_dice():
    """ funcion para lanzar un dado, solo retorna valor si la cara es distinta a 3 """
    print(colored("Lanzando tu dado...", "green", attrs=['bold']))
    while True:
        dice = random.randint(1, 6)
        if dice != 3:
            return dice
        else:
            print(colored("Tu dado es 3, lancemos de nuevo", "green", attrs=['bold']))
            continue

def first_challenge():
    """ primer desafio del juego """
    print(colored("Manuk dice: ", "magenta"))
    time.sleep(1)
    print(colored("Estas en un calabozo y hay 2 puertas... en la puerta 1 hay una bestia mortifera", "magenta"))
    time.sleep(1)
    print(colored("Bien... me decias que tu sabiduria era muy valorada en tu pueblo, veamos si tomas buenas decisiones.", "magenta"))
    time.sleep(4)
    print(colored("En la puerta 2 está la salida", "magenta"))
    time.sleep(1)
    print(colored("Vamos a lanzar un dado...si tu dado es par, acertarás a la salida...", "magenta"))
    time.sleep(1)
    print(colored("De lo contrario debes enfrentar a la bestia mortal...", "magenta"))
    global gonna_roll
    player_action = ask_dice()
    gonna_roll = player_action
    dice_result = ""
    while gonna_roll:
        if player_action == True:
            dice = roll_dice()
            dice_number = is_even(dice)
            if is_even == True:
                print(colored("Manuk dice: ", "magenta"))
                print(colored("Bien,... has elegido la salida...", "magenta"))
                gonna_roll = False
                dice_result = "exit"
                return dice_result
            else:
                
                print(colored("Manuk dice: ", "magenta"))
                time.sleep(1)
                print(colored("Oh no... ", "magenta"))
                time.sleep(1)
                print(colored("Me temo que deberás... enfrentar a la...", "magenta"))
                time.sleep(1)
                print(colored("BESTIA...", 'red'))
                time.sleep(1)
                gonna_roll = False
                dice_result = "beast"
                return dice_result

def roll_damage_dice(character):
    """ es el dado por el que se multiplica el dano de tu espada """
    # """ funcion para lanzar un dado, solo retorna valor si la cara es distinta a 3 """
    if character == "player":
        print(colored("Lanzando tu dado para calcular tu daño...", "green"))
        dice = random.randint(1, 6)
        print("Tu dano es de %s" % str(dice*10))
        return dice*10
    else:
        print(colored("Lanzando dado para calcular daño de la bestia...", "red"))
        dice = random.randint(1, 6)
        print("La bestia tiene un dano de %s" % str(dice*10))
        return dice*10

def ask_dice():
    """ pregunta a player si quiere tirar dado """
    while True:
        res = input("Deseas lanzar tu dado? [yes / no]: ")
        if res == "yes":
            return True
        elif res == "no":
            print("Debes lanzar! Prueba tu suerte...")
        else:
            print("Responde YES o NO... no seas cobarde...")    
    
def is_even(dice_number):
    """ valida si el dado es even (par) u odd (impar) 
    las funciones que retornan boolean se nombran 
    como pregunta """
    if dice_number % 2 == 0:
        print("Tu dado es par")
        return True # retorna verdadero porque es par
    else:
        print("Tu dado es impar")
        return False # retorna falso porque es impar

def beast_fight():
    global player_alive
    global beast_alive
    
    BEAST_HP = 60
    player_alive = True
    
    beast_alive = True
    player_turn = True

    # while player_turn:
    while True:
        player_damage_dice = roll_damage_dice("player")
        # print("TU HP ES DE %s" % str(PLAYER_HP))
        if player_damage_dice < BEAST_HP:
            print("A la bestia le queda %s de vida de un total de 60" % str(BEAST_HP-player_damage_dice))
            
        else:
            print("Has asesinado a la bestia")
            beast_alive = False
            return 1
            # sys.exit()
        
        if BEAST_HP > 0:
            print(colored("Ahora hace dano la bestia...", "red"))
        
        beast_damage_dice = roll_damage_dice("beast")

        if beast_damage_dice < PLAYER_HP:
            print("A ti te queda %s de vida de un total de %s" % ((str(PLAYER_HP-beast_damage_dice), str(PLAYER_HP))))
            
        else:
            print("Te ha asesinado la bestia")
            player_alive = False
            return 0
            # sys.exit()
    
  
start_game()
propose_game()
dice = roll_dice()
check_dice(dice)

# primer desafío
first_challenge_result = first_challenge()
# validacion de resultado de primer desafio
if first_challenge_result == "beast":    
    print(colored("Manuk dice: ", "magenta"))
    print(colored("Necesitaras suerte porque de esta bestia es muy dura...", "magenta"))
    time.sleep(1)
    print(colored("tienes una espada que hara 10 de daño multiplicada por un dado de 6 caras", "magenta"))
    time.sleep(1)
    print(colored("La bestia al atacar tambien tiene un dado", "magenta"))
else:
    print(colored("Felicidades, tienes la salida...", "green"))
    sys.exit()

# vamos a la pelea con la bestia
result = beast_fight()
if result == 0:
    print(colored("Manuk dice: ", "magenta"))
    print(colored("Se nota que aun te falta entrenar... vuelve cuando mejores...", "magenta"))
else:
    print(colored("Manuk dice: ", "magenta"))
    print(colored("Me has sorprendido... pero no te confies... habrá desafios...", "magenta"))
    
