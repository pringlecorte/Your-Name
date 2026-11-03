import pygame, time, math, sys, random
pygame.init()


WIDTH = 31
HEIGHT = 31
FOV = RES = MULTIPLAYER = MINIGAME_NUMBER = PROJECTED_RAYS = 0

TILE_SIZE = 64
MAP_NUM = 1


FINISHED = False

## DESIGN AND MENU!!!

def display_headers():
    print(''*60) 
    print("Your Name") 
    print("----------------------------------") 
    print()
    print("Project Your Name")
    print()

def PsuedoGameLoading():
    print()
    word = "Stella: wait! I recall another memory..."
    load = "............"
    everydialogue = [word, load]
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        print()
        time.sleep(0.08)

    print(""*2)

def Menu(WIDTH, HEIGHT, FOV, RES, PROJECTED_RAYS, MULTIPLAYER):
    pygame.display.iconify()
    print()
    WIDTH = HEIGHT = 0
    while WIDTH == 0:
        WIDTH = input("'How wide would my memory replay need to be to remember his name..?' (Screen WIDTH [10-30]): ")
        if not WIDTH.isdigit() or not(10<=int(WIDTH)<=30):
            print("Do you not want me to remember...")
            print()
            WIDTH = 0
    print()
    while HEIGHT == 0:
        HEIGHT = input("'How tall would my memory replay need to be to remember his name..?' (Screen HEIGHT [10-15]: ")
        if not HEIGHT.isdigit() or not(10<=int(HEIGHT)<=15):
            print("Do you not want me to remember...")
            print()
            HEIGHT = 0
    print()
    while FOV == 0:
        FOV = input("'How narrow was my vision when I still had him...'(FOV, [60-180], smaller is narrower view): ")
        if not FOV.isdigit() or not(60<=int(FOV)<=180):
            print("Did I really taking him for granted..")
            print()
            FOV = 0
    FOV = int(FOV)
    print()
    while RES == 0:
        RES =  input("'How vivid does my memory need to be to remember your name...'(RES, [1-5]. Smaller is more defined): ")
        if not RES.isdigit() or not(1<=int(RES)<=5):
            print("Did I forget to take my meds again...why is everything so blocky?")
            print()
            RES = 0
        
    RES = int(RES)
    print()
    while MULTIPLAYER == 0:
        MULTIPLAYER = input("Does...does my memory involve..'him'? (number people playing [1-2]. 2 Players required for Narrative Story (Don't worry, you can play Multiplayer with only yourself but it's gonna take longer, trust)): ")
        if not MULTIPLAYER.isdigit() or not(1<=int(MULTIPLAYER)<=2):
            print("My mind can't handle that much...")
            print()
            MULTIPLAYER = 0

    if MULTIPLAYER == '2':
        MULTIPLAYER = True
    else:
        MULTIPLAYER = False

    basics = '[SYSTEM]: To move around, press WASD/Arrow Key. If playing on MULTIPLAYER, player "Stella" is on the left, and player "cloverforever0905" on the right'
    for i in basics:
        print(i, end='', flush=True)
        time.sleep(0.04)

    PROJECTED_RAYS = FOV//RES
    if PROJECTED_RAYS == 0:
        PROJECTED_RAYS = 1

def Multiplayer_Menu(MINIGAME_NUMBER):
    print()
    
    seperator = '---------------------'
    for i in seperator:
        print(i, end='', flush=True)
        time.sleep(0.1)

    print(""*2)

    today = '[SYSTEM]: What are we doing today?'
    
    for i in today:
        print(i, end='', flush=True)
        time.sleep(0.1)
    print()
    
    GAME_LIST = ["[1] 'Young Stella: 'I challenge you to Montgeometry Racers!!'", "[2] 'Young ████: 'let's play Blind and Seek'", "[3] Open Google Chrome", "[4] Shut Down Lenovo ThinkPad X100e"]
    ERROR_MESSAGE = ["Geometry_Dash.exe", "File not found.", "Check the file name and try again"]
    GAME_FILES = [MRH,BS]

    for i in GAME_LIST:
        print(i)

    
    MINIGAME_NUMBER = 0
    print()

    if int(MINIGAME_NUMBER)==10:
        MS.GAME_START()
        return

    while MINIGAME_NUMBER == 0:
        Minigame_Num = input("what..what memory should I try to remember? [1-4]: ")
        
        if not MINIGAME_NUMBER.isdigit() or not(1<=int(MINIGAME_NUMBER)<=4):
            for i in error:
                print(i)
            MINIGAME_NUMBER = 0
            print()

        elif int(MINIGAME_NUMBER) == 3:
            dialogue1_5()
            Multiplayer_Menu()

        elif int(MINIGAME_NUMBER) == 4:
            break
        else:
            GAME_FILES[int(MINIGAME_NUMBER) - 1].GAME_START()

#Menu(WIDTH, HEIGHT, FOV, RES, PROJECTED_RAYS, MULTIPLAYER)
print(WIDTH, HEIGHT, FOV, RES, PROJECTED_RAYS, MULTIPLAYER)
success = pygame.display.iconify()
print(success)  # Will print False if your Linux environment blocked it

def choiceToPlay():
    REPLAY = 'F'

    while REPLAY == 'F':
        REPLAY = input("Stella: Should I try to recall once more? [Y/N]: ")

        if REPLAY.upper() != 'Y' or REPLAY.upper() != 'N':
            print("Stella: ...please...")
            print()

        elif REPLAY() == 'Y':
            givingup = 'Stella: I am not giving up!!'
            for i in givingup:
                print(i, end='', flush=True)
                time.sleep(0.1)
            print()
            print()

    return REPLAY

class MONTGEOMETRY_RACERS:
    def __init__(self, map_num, name):
        self.MAP_NUM = map_num

        self.START = 0
        self.TIMER = 0
        self.TOTAL_TIME = 0
        self.STATE = "NOT YET STARTED"
        self.DIALOUGE = random.randint(0, 20)
        self.START_LINE_THRESH = [[150, 275], 
                                [260, 286]] 
        self.NAME = name
    def GAME_START(self):
        print()
        
        for i in title:
            print(i, end='', flush=True)
            time.sleep(0.09)
        print()
        
        rules = "[SYSTEM]: Race to get the shorter time!! It's that simple, really. [Open the game window]"
        for i in rules:
            print(i, end='', flush=True)
            time.sleep(0.09)
        print()
        
        Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))

    def REFEREE(self, name, x, y):
        if abs(x - self.START_LINE_THRESH[0][0]) > 50:
            return 

        if self.START_LINE_THRESH[0][0] <= x <= self.START_LINE_THRESH[1][0]:
            if self.START_LINE_THRESH[0][1] <= y <= self.START_LINE_THRESH[1][1]:
                
                if self.STATE == "NOT YET STARTED":
                    print()
                    print(f"Timer STARTED ({self.NAME}) 0:00:00")
                    self.START = pygame.time.get_ticks()
                    self.STATE = "RACING"
                
                if self.STATE == "RACING":
                    print()
                    print(f"Timer Ended. {self.NAME}'s Results: {self.TOTAL_TIME//60000}:{self.TOTAL_TIME - self.TOTAL_TIME//1000}:{self.TOTAL_TIME%1000}")
                    self.STATE = "FINISHED"

        if self.STATE == "RACING":
            self.TIMER = pygame.time.get_ticks()
            self.TOTAL_TIME = self.TIMER - self.START
        
        elif self.STATE == "FINISHED":
            return self.TOTAL_TIME




