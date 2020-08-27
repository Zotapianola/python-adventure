from termcolor import colored
import random
import time
import sys

HIGH_HP = 100
LOW_HP = 50
PLAYER_HP = 0

def start_game():
    print(colored("Como te llamas?... Dime tu nombre... No recuerdo la ultima vez que alguien me vino a ver", "magenta"))
    # player_name = input("Escribe tu nombre: ")
    player_name = "CAMBIAR"
    print("Te has identificado como: ", player_name)
    print(colored("... \n... \n Hola %s... que raro tu nombre, se nota que no eres de aqui... " % (player_name), "magenta"))

def propose_game():
    print(colored("Te propongo una aventura... ", "magenta"))
    # time.sleep(1)
    print(colored("Vamos a tirar un dado de 6 caras...", "magenta"))
    # time.sleep(1)
    print(colored("Si el dado es mayor a 3... tu aventura parte con %s de vida" % str(HIGH_HP), "magenta"))
    # time.sleep(1)
    print(colored("Si el dado es menor a 3... tu aventura parte con %s de vida" % str(LOW_HP), "magenta"))
    # time.sleep(1)
    print(colored("Si el dado es 3... debes reintentar..." , "magenta"))
    print(colored("SUERTE... la vas a necesitar" , "magenta"))
    

def check_dice(dice):
    while True:
        if dice < 3:
            print(colored("Dado menor a 3 :'(", "red"))
            PLAYER_HP = LOW_HP
            print(colored("Bien... pero pudo ser mejor... tu aventura ha partido con un HP de %s" % (PLAYER_HP), "magenta", attrs=['bold']))
            return dice
        elif dice > 3:
            print(colored("Dado mayor a 3","green"))
            PLAYER_HP = HIGH_HP
            print(colored("Felicidades, tu aventura ha partido con un HP de %s :)" % (PLAYER_HP), "magenta", attrs=['bold']))
            return dice
        else:
            print("Dado igual a 3, se lanza de nuevo")
            
def roll_dice():
    """ funcion para lanzar un dado, solo retorna valor si la cara es distinta a 3 """
    print(colored("Lanzando tu dado...", "green"))
    while True:
        dice = random.randint(1, 6)
        if dice != 3:
            return dice
        else:
            print(colored("Tu dado es 3, lancemos de nuevo", "green"))
            continue

def first_challenge():
    """ primer desafio del juego """
    print("bien... me decias que tu sabiduria era muy valorada en tu pueblo, veamos si tomas buenas decisiones.")
    print("estas en un calabozo y hay 2 puertas... en la puerta 1 hay una bestia mortifera")
    print("en la puerta 2 está la salida")
    print("vamos a lanzar un dado...si tu dado es par, acertarás a la salida...")
    print("de lo contrario debes enfrentar a la bestia mortal...")
    global gonna_roll
    player_action = ask_dice()
    gonna_roll = player_action
    dice_result = ""
    while gonna_roll:
        if player_action == True:
            dice = roll_dice()
            dice_number = is_even(dice)
            if is_even == True:
                print("Bien,... has elegido la salida...")
                gonna_roll = False
                dice_result = "exit"
                return dice_result
            else:
                print("Deberás enfrentar a la bestia...")
                gonna_roll = False
                dice_result = "beast"
                return dice_result

def roll_damage_dice():
    """ es el dado por el que se multiplica el dano de tu espada """
    # """ funcion para lanzar un dado, solo retorna valor si la cara es distinta a 3 """
    print(colored("Lanzando tu dado para calcular tu daño...", "green"))
    dice = random.randint(1, 6)
    print("Tu dano es de %s" % str(dice*20))
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
    # if PLAYER_HP > 0:
    player_alive = True
    
    # if BEAST_HP > 0:
    beast_alive = True

    player_turn = True

    while player_turn:
        player_damage_dice = roll_damage_dice()
        if player_damage_dice < BEAST_HP:
            print("A la bestia le queda %s de vida de un total de 60" % str(BEAST_HP-player_damage_dice))
            # pla
        else:
            print("has asesinado a la bestia")
            sys.exit()
        
        if BEAST_HP > 0:
            print("ahora hace dano la bestia...")
            # player_turn = False
    
    # while player_turn == False:
    #     print("la bestia es mala...")
    #     player_turn = True
    #     continue
    





start_game()
propose_game()
dice = roll_dice()
check_dice(dice)

# primer desafío
first_challenge_result = first_challenge()
# validacion de resultado de primer desafio
if first_challenge_result == "beast":
    print("necesitaras suerte porque de esta bestia necesita 2 golpes para morir...")
    print("tienes una espada que hara 10 de daño multiplicada por un dado de 6 caras")
    print("la bestia al atacar tambien tiene un dado")
else: 
    print("felicidades, tienes la salida...")
    sys.exit()

# vamos a la pelea con la bestia
beast_fight()

