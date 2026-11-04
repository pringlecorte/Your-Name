## THIS IS STILL A WORK IN PROGRESS. WORKING CODE IS MY OTHER ONE BUT ITS MORE UNOPTIMZED (well duh, obv it is)
import pygame, time, math, sys, random
pygame.init()


WIDTH = 31
HEIGHT = 31
FOV = RES = MULTIPLAYER = MINIGAME_NUMBER = PROJECTED_RAYS = 0

TILE_SIZE = 64
MAP_NUM = 1


FINISHED = False

## DESIGN AND MENU!!!
def typewrite(text, timing_per_letter, padding):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(timing_per_letter)
    print(""*padding)

def typewrite_list(list, timing_per_letter, timing_per_text, padding):
    for text in list:
        for letter in text:
            print(letter, end='', flush=True)
            time.sleep(timing_per_letter)
        time.sleep(timing_per_text)
        print()
    print(""*padding)

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
    typewrite_list(everydialogue, 0.1, 0.08, 2)


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
    typewrite(basics, 0.04, 2)

    PROJECTED_RAYS = FOV//RES
    if PROJECTED_RAYS == 0:
        PROJECTED_RAYS = 1

def Multiplayer_Menu(MINIGAME_NUMBER):
    print()
    
    seperator = '---------------------'
    typewrite(seperator, 0.1, 2)

    today = '[SYSTEM]: What are we doing today?'
    
    typewrite(today, 0.1, 2)
    
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

        elif REPLAY.upper() == 'Y':
            givingup = 'Stella: I am not giving up!!'
            typewrite(givingup, 0.04, 2)


    return REPLAY

        


## GAMESSSS
key = pygame.key.get_pressed()

class MONTGEOMETRY_RACERS:
    def __init__(self, map_num, name):
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
        title = "Memory II: I'm With You Till the End of the Line"
        typewrite(title, 0.09, 2)
        
        rules = "[SYSTEM]: Race to get the shorter time!! It's that simple, really. [Open the game window]"
        typewrite(rules, 0.09, 2)
        
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

        if self.DIALOUGE == 1:
            for i in random.choice(MGR_dialogues_Stella):
                print(i, end = '', flush= True)

            for i in random.choice(MGR_dialogues_1234):
                print(i, end='', flush=True)


class BLIND_SEEK:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

        self.L_PRESS = 0
        self.HIDER = False
    

class BLIND_SEEK_CALC:
    def __init__(self, player_1, player_2):
        self.STELLA = player_1
        self.CLOVER = player_2

        self.START = 0
        self.END = 0
        self.COUNT = 0
        self.GAME_STATE = False
        self.KEY_STATE = False
        self.DISTANCE = 0

    def GameStart(self):
        print()
        
        title = "Memory III: Dancing In The Dark"
        typewrite(title, 0.09, 2)
        

        rules = "[SYSTEM]:The hider will be given 1 min(s) to hide somewhere in the map and the seeker will be given 2 min(s) to find the seeker. The seeker must find the other guy. Since you are 'blind' and none of you can see the other, press the 'L' key to know how far you are to the other player. Once 1 min(s) is up, the hider isn't allowed to move. Oh and also, you can't press the 'L' key more than eight (8) times [Open the game window]"
        typewrite(rules, 0.05, 2)

        Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))
        time.sleep(1)
    
    def coin_flip(self):
        COIN = random.randint(0,1)

        if COIN == 1:
            system = ["[SYSTEM]: sT311a38 is the hider!", "cloverforever0905 is the seeker!"]
            typewrite(system, 0.04, 2)
            
            self.STELLA.HIDER = True
    
            print("[SYSTEM]: Hider, start hiding!! (Open game window)")
            self.START = pygame.time.get_ticks()
    
            return

        system = ["[SYSTEM]: cloverforever0905 is the hider!", "sT311a38 is the seeker!"]
        typewrite(system, 0.04, 2)

        self.CLOVER.HIDER = True

        print("[SYSTEM]: Hider, start hiding!! (Open game window)")
        self.START = pygame.time.get_ticks()

        return
    
    
    def REFEREE(self, name, x, y):
        self.TIMER = pygame.time.get_ticks()
        self.END = (self.TIMER - self.START)/1000 ## gets seconds
        
        if self.END > 10:
            if not self.GAME_STATE:
                print("[SYSTSEM]: Seeker...start finding!!")   
                self.GAME_STATE = True
            
            if abs(self.STELLA.x - self.CLOVER.x) < 50:
                if abs(self.STELLA.y - self.CLOVER.y) < 50:
                    self.DISTANCE = math.dist((self.STELLA.x, self.STELLA.y), (self.CLOVER.x, self.CLOVER.y))/32

                    if self.DISTANCE < 4:
                        if self.STELLA.HIDER:
                            return ## message goes here
                        
                        else:
                            return ## message goes here also
            
            if key[pygame.K_l]:
                if self.STELLA.L_PRESS < 8:
                    if not self.KEY_STATE:
                        self.DISTANCE = math.dist((self.STELLA.x, self.STELLA.y), (self.CLOVER.x, self.CLOVER.y))/32
                        print(f"[SYSTEM]: Hider is {self.DISTANCE}m away")
                        
                        self.KEY_STATE = True
                        self.STELLA.L_PRESS += 1

                else:
                    self.KEY_STATE = False
            else:
                print("[SYSTEM]: You used up all your presses!!")


            if self.END > 120:
                if self.STELLA.HIDER:
                    return ## MESSAGE GOES HERE I FORGOT HAHA
            
                else:
                    return ## SAME GOES HERE

class MOUNTAIN_SCENE:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.DISTANCE = 0
        self.GAME_STATE = 0
        self.KEY_STATE = False
        self.L_PRESS = False
        self.THRESHOLD_X = 1330
        self.THRESHOLD_Y = 200
        self.GAME_FINISHED = False
        

    def GAME_START(self):
        title = "Memory IV: Kimi No Wa Na..."
        typewrite(title, 0.05, 2)

        if not self.GAME_STATE:
            print("[Stella's Consiousness]: Keep moving forward until you see our mountain hideout!! Press L to see how far you are from there!! (Open game window)")   
            self.GAME_STATE = True
        
    def REFEREE(self, x, y, GAME_3):
        if self.THRESHOLD <= x:
            self.GAME_FINISHED = True
            GAME_3 = True
        
        if key[pygame.k_l]:
            self.DISTANCE = math.dist((x, y), (self.THRESHOLD_X, self.THRESHOLD_Y))
            if not self.KEY_STATE:
                print(f"[Stella's memory]: Our hideout is ", {self.distance}, "m away!!")
                self.KEY_STATE = True
            
            else:
                self.KEY_STATE = False
            

#######################
##dialogueS##
#######################

list_of_thoughts = [
    "the familiarity of this place...",
    "this scene...I remember it a long time ago",
    "this place...is this the place we used to love..?",
    "is this the place that I've been dreaming off...",
    "this feeling...so...familiar",
    "where am I...",
    "why did that happen...",
    "you feel so near...yet so far....",
    "did his name start with an M or a W...or a P...",
    "holding onto memories...feels tiring...but I must..",
    "HEY!! Oh...I'm sorry...I thought you were someone else....",
]            
MGR_dialogues_Stella = ["Youre such a slow poke!!", "Hurry up man!", "Get a better car bro"]
MGR_dialogues_1234 = ["Watch me driftttt", "360 no scope?! oh nevermind.", "You know, I may not be good FOR NOW, but at least I have a LIFE, you TRYHARD"]

def realization():
    alarm = "It's just another manic Mondayyyy, wish it were Sunda-"
    realization = "Stella slams her alarm shut and sits up with her messy hair and yawns. It's always been this way since he left"
    dialogue = "*Stella: *rubbing her eyes* there goes the 3649th dream trying to...*crosses out her calendar"
    action = "Stella lays back in her bed and opens her phone to do her daily message. The 3649th message that hasn't been read."
    message = "'Hi...  how have you been?'"
    message1 = "'Sent'"
    dialogue1 = "Stella puts down her phone for the 3649th time,"
   
    action1 = "As Stella gets up from her bed to get ready for her first class, she trips and falls onto the floor face first"
    dialogue2 = "Stella: tsk, I forgot to take my meds"
    action2 = "Stella slowly picks herself off her dorm’s cold, hard floors, and quietly shuffles into the bathroom to splash herself with some cold water"
    dialogue3 = "Stella: *opens the closet then just stops and wonders for a while* why did I open this closet again?"
    action3 = "Stella: *As her eyes meet the meds she needs to take everyday to aid her in her dementia, she suddenly remembers and closes the closet* oh yeah"
    action4 = "Stella: *reopens the closet and takes her meds before closing it again*"
    action5 = "Stella plumps herself on her bed again for one more time to cuddle with her stuff toys, deeply inhaling and exhaling, trying to recall the stuff that has happened this week"
    list1 = "They learnt about spark plugs, advanced circuitry, MB102 boards…"
    list2 = "While she has been trying to remember his name"
    dialogue4 = "Stella: *sits back up and sighs* Another day to try..."
    action6 = "Stella: *opens her old Lenovo Thinkpad* ...and another day with this old laptop"
    action7 = "Stella closes her tired eyes and goes back to trying for the 3649th time"
    everydialogue = [alarm, realization, dialogue, action, message, message1, dialogue1, action1, dialogue2, action2, dialogue3, action3, action4, action5, list1, list2, dialogue4, action6, action7]
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.08)
        if i == action3:
            time.sleep(1)
        print()

def dialogue1():
    dialogue0 = '"the youthful sapling doesnt always mean a beautiful oak"'

    dialogue1 = "'Umm..hi there...our teacher told me we're going to be groupmates for a project. What's your namee?'"
    dialogue2 = "'Haii..I am Stellaria Hebeto but you can just call me Stella...my parents gave me a really stupid name i know, i know..'"
    dialogue3 = "'erm...I don't think it's stupid..I think its beautiful!! I'm ████'"
    dialogue4 = "'what happened...'"
    dialogue5 = "'what was his name again...'"


    everydialogue = [dialogue0, dialogue1, dialogue2, dialogue3, dialogue4, dialogue5]
    print()
    print("pringl.corte Production Presents...")
    time.sleep(3)
    print("A game called...")
    time.sleep(3)
    print()
    print("'Your Name'")
    time.sleep(2)
    print("Memory I: 'Kimi No Wa Na?'")
    time.sleep(2)
    for i in everydialogue:
        typewrite(i, 0.1, 2)
        if i == dialogue3:
            time.sleep(2.5)
            print()
        time.sleep(0.5)
        
        print()
        print() 

def dialogue1_5():
    dialogue1 = "As young Stella navigates to the Chrome Window, she notices ████ trying to hold in a laugh"
    dialogue2 = "'Young Stella: What? Why are you laughing'"
    dialogue3 = "'[Chrome]: Now Loading: https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1&pp=ygUVbmV2ZXIgZ29ubmEgZ2l2ZSB1IHVwoAcB0gcJCdQKAYcqIYzv'"
    dialogue4 = "'Young Stella: hey...wait a minute...whats this?'"
    dialogue5 = "'[Chrome]: Never gonna give you up,'"
    dialogue6 = "'[Chrome]: Never gonna let you down'"
    dialogue7 = "'Young Stella: BRUH'"
    everydialogue = [dialogue1, dialogue2, dialogue3, dialogue4, dialogue5, dialogue6, dialogue7]
    for i in everydialogue:
        for y in i:
            if i == dialogue3:
                typewrite(i, 0.06, 1)
                continue

            if i == (dialogue5 or dialogue6):
                typewrite(i, 0.06, 1)
                continue

            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.5)
        if i == dialogue3:
            time.sleep(2.5)
            print()
        print()
        print()
    


def dialogue2_(): 
    #winner is mark (racing)
    print()
    dialogue1 = "'Young ████:Hahahahaha I beat you again!! I beat you again *starts dancing'"
    dialogue2 = "'Young Stella: SHUSH. I only LET you win for that round!!! I'm gonna beat you the next round..!!'"
    dialogue3 = "'Young ████:Sureeeee buddy, that's what they ALL say. Nobody can beat the greatest gamer with their trusty gamer name: cloverforever0905'"
    dialogue4 = "'Young Stella: bro. thats a STUPID name. NOBODY names their character cloverforever0905. No wonder she rejected you bro'"
    dialogue5 = "[PRINX THE DEV]: Okay bro, I USE THAT USERNAME, I DON'T SEE ANYTHING WRONG"
    everydialogue = [dialogue1, dialogue2, dialogue3, dialogue4, dialogue5]
    typewrite_list(everydialogue, 0.1, 0.4, 2)
    dialogue3_1()

def dialogue2_5():
    #winner is stella  
    print()
    dialogue1 = "'Young Stella: Hahaha I told you I would beat you!! I wasn't even TRYING bro'"
    dialogue2 = "'Young ████: BULLY. I WAS NEW TO THE GAME. I WAS STILL LEARNING. I WAS---'"
    dialogue3 = "'Young Stella: Yap yap yappity yap, stop making excuses and go back to playing SNAKE'"
    dialogue4 = "'Young ████:*whimpers* lets just play another round...'"
    everydialogue = [dialogue1, dialogue2, dialogue3, dialogue4]
    typewrite_list(everydialogue, 0.1, 0.4, 2)
    dialogue3_1()

def dialogue3_1():
    print()
    seperator = "---------------------------"
    scene = "'Dear I fear, were facing a problem, you love me no longe-'"
    action = "Stella's eyes shoot open upon hearing her phone's ringtone ring ring"
    dialogue1 = "Stella: *snorts* this better be a good call"
    action1 = "Stella's Phone: 'Unsaved Contact is calling'"
    action2 = "Beep"
    dialogue2 = "Stella: Hello? Who's this?"
    dialogue3 = "Stella's Mom: Hi dear, it's me, your mother"
    dialogue4= "Stella: *thinks for a while* 'Mom'? Oh right. Hi mom, why'd you call."
    dialogue5 = "Stella's Mom: I wanted to know if you drank your meds honey…"
    dialogue6 = "Stella: Meds? Oh those, yeah I did. What else do you want from me?."
    dialogue7 = "Stella's Mom: Are you still thinking about that boy from your childhood?"
    dialogue8 = "Stella: *her eyes narrowing* no I'm not"
    dialogue9 = "Stella's Mom: Good. Because that boy…only made your life wor-"
    dialogue10 = "Beep. Call Ended"

    everydialogue = [seperator, '',scene, action, dialogue1, action1, action2, dialogue2, dialogue3, dialogue4, dialogue5, dialogue6, dialogue7, dialogue8, dialogue9, dialogue10, seperator]
    typewrite_list(everydialogue, 0.1, 0.3, 2)
    
def dialogue4():
    #STELLA WON
    dialogue1 = "Young Stella: BRO YOU DIDN'T EVEN TRY"
    dialogue2 = "Young ████: OH COME ON, WE BOTH KNOW YOUR GOOD AT FINDING AND HIDING. AFTER ALL, YOU GOTTA KEEP FINDING FOR YOUR NINTENDO 3DS AFTER YOUR MOM KEEPS TAKING IT AWAY CUZ YOU HAVE A SHORT ATTENTION SPAN EVERYTIME YOU PLAY IT"
    dialogue3 = "Young Stella: *puts her hand on her chest* Me??? Short attention span?? NO I DONT HAVE A SHORT ATTENTION SPA...woah lookie over there, a cool car!! wooooooo..."
    action1 = "Young Stella: *looks back at ████*"
    dialogue4 = "Young Stella: I dont have a short attention span and I'm just good at finding things, got it?? Hmph!"
    dialogue5 = "Young ████: *faces the player* (jokingly) THIS is what I gotta deal with everyday"
    everydialogue = [dialogue1, dialogue2, dialogue3, action1, dialogue4, dialogue5]
    typewrite_list(everydialogue, 0.1, 0.4, 2)
    dialogue5_1()
    
def dialogue4_5():
    #████ WON
    dialogue1 = "Young ████: HAHA SKILL ISSUE, I TOLD YOU I WAS A PRO"
    dialogue2 = "Young Stella: BEGINNER'S LUCK. I LET YOU WIN OR ELSE YOU WOULD'VE STOPPED PLAYING WITH ME YOU CRYBABY"
    dialogue3 = "Young ████: I'M NOT A CRYBABY CUH. IM NOT--wait...you just want me to play with you don't you?"
    dialogue4 = "Young Stella: No?? NO. I CAN PLAY BY MYSELF"
    action1 = "Young ████:*smirks* oh COME ON admit it, without me your life would be full of wins. I'M TEACHING YOU THE LESSON OF LOSS."
    dialogue5 = "Young ████: I'm like *thinks for a while* MASTER SHIFU"
    dialogue6 = "Young Stella: More like Master Shi-POO"
    everydialogue = [dialogue1, dialogue2, dialogue3, dialogue4, action1, dialogue5, dialogue6]
    
    typewrite_list(everydialogue, 0.1, 0.4, 2)
    dialogue5_1()

def dialogue5_1():
    print()
    seperator = "---------------------------"
    dialogue1 = "The more Stella remembers her old memories, the more it hurts her heart, seeing how much she changed ever since he left"
    dialogue2 = "'why..why did you have to teach me the hard way...'"
    dialogue3 = "'please....just let me remember..'"
    dialogue4 = "'was i too much for you...'"
    dialogue5 = "'or was i too little?'"
    everydialogue = [seperator, '', dialogue1, dialogue2, dialogue3, dialogue4, dialogue5, seperator]
    
    typewrite_list(everydialogue, 0.06, 0.1, 2)

def dialogueFinal():
        dialogue1 = "The world around Stella begins to blur as liquid begins forming in her eyes."
        dialogue2 = "Stella: why...please...just let me recall it..why can't I recall it.."
        dialogue3 = "Stella buries her face in her hands, trying hard not to cry, giving in to the warm embrace of her bed."
        sequence = "............"
        dialogue4 = "Next day..."
        alarm = "'The world you know, always running to and fro, a frightful place to beeee~'."
        dialogue6 = "As Stella's alarm goes off, she doesn't turn it off"
        action1 = "She doesn't sit up with her frizzled hair and yawn"
        action2 = "She doesn't mark her calendar"
        action3 = "She just lies on her bed, staring blankly at the rotating ceiling fan"
        action4 = "........."
        action5 = "As Stella wakes up from her second sleep, Stella checks the time"
        time1 = "3:08 PM"
        dialogue5 = "Stella: *in a shaky voice* great..I skipped my whole class.."
        action6 = "Stella looks at her phone, wondering if she should really do it once more"
        action7 = "If it even still has meaning"
        action8 = "She grabs her phone and opens her messages app to do her daily routing"
        action9 = "Only this time, she doesn't"
        action10 = "This time, she just stares blankly at the flickering screen of her Samsung."
        action11 = "..........."
        action12 = "As Stella wakes up for the third time, she feels her stomach growling from the absence of food for the whole day..'whole day??' wonders Stella"
        time2 = "2:34 AM"
        action14 = "Stella: better get some food outside…"
        action15 = "As Stella slowly makes her way to her cabinet, she trips and falls onto the cold hard floor."
        action16 = "Stella: tsk. I forgot to take my...meds?"
        action17 = "Stella stand back up and changes to her outside clothes."
        action18 = "...Outside..."
        action19 = "As Stella was walking towards the closest McDonald's she stared hard at the mountain overlooking her city"
        action20 = "As if Stella had some sort of connection with it, but just couldn't seem to grasp it."
        dialogue16 = "Stella: A Quarter Pounder and a Coke Float...and a Quarter Pounder please."
        response1 = "Cashier: So 2 Quarter Pounders and a Coke Float?"
        dialogue17 = "Stella: What no, I only said one Quarter Pounder"
        action21 = "As Stella settles onto an isolated table, she continues studying the mountain as if its calling her"     
        memory1 = "'Stella!! Hurry up you slow poke it's not that cold up here!!'"
        action22 = "Stella turns back but sees no one talking to her"
        dialogue18 = "Stella: Huh?"
        memory2 = "'When we get to the top, let's cover the whole thing with snow angels!!'"
        dialogue19 = "Stella: ?! Am I remembering something..."
        memory3 = "'Take that! *throws a snowball."
        memory4 = "'Hey! What could you possibly be writing while we're on a mountain??'"
        memory5 = "'No peeking!! It's for the future you.'"
        memory6 = "'*lunges* just let me read it!! I'm future meeee'"
        memory7 ="'OUCHHH' 'MOMMY' 'LET GOOO' 'STOPPP' 'STELLAAAA LET ME GOOO.'"
        action23 = "Stella looks at the mountain."
        dialogue20 = "Stella: The note..the note that he wrote..."
        action24 = "Stella rises to her feet and without finishing her food, she's off to the call of the night'"
        time3 = "3:01 AM"
        action25 = "Stella runs on the edge of the mountain, the cool breeze flowing against her distraught face"
        action26 = "Despite running with only energy from the single bitewa that the Quarter Pounder gave her, it's as if, something is helping her through the mountain."
        dialogue21 = "Stella: What are you trying to tell me…"

        dialogue50 = "Stella: It's...here!!! The letter he wrote to me!! All those years ago...I thought it would be useless..."
        dialogue51 = "Stella breaks down in tears, not in anger anymore but finally from...joy.."
        dialogue52 = "as she begins reading the letter under the twilight sparkles of the night."
        letter = f"""
        ------------------------
        May 9, 2013
        To Stella,

        Love
        is a thing so true
        Love
        is how I feel for you.

        How do I admire you, let me count the ways,
        Each bird that chirps, each the sun’s rays,
        I like you not only for your beauty,
        But because you are a symphony.
        A symphony composed of everything dear,
        The beauty, the smarts, the wits I fear.

        My admiration for you is as bright as the stars,
        My guiding light during my wars. 


        Love,
        Is not a thing, an object out of the blue
        But love,
        Is how I’ve felt for you

        ...P.S, you forgot to greet me happy birthday
        """

        end = "After all these years, after all these time, Stella has finally found her peace. 3650 days after he left and Stella finally found peace."
        name = "Stella: from...Prinx Cortez..."
        if game3finished:
            everydialogue = [dialogue50, dialogue51, dialogue52, letter]
            
            for i in everydialogue:
                if i == letter:
                    for line in i.split('\n'):
                        for y in line:
                            print(y, end='', flush=True)
                            time.sleep(0.1)
                        print()
                    continue

                for y in i:                #
                    typewrite(y, 0.05, 2)

                if i == dialogue18:
                    print()
                print()    

            dialogueEndCredits()

            everydialogue = [end, name]
            typewrite_list(everydialogue, 0.08, 0.1, 2)
            sys.exit()

        else:
            everydialogue = [dialogue1, dialogue2, dialogue3, sequence, dialogue4, sequence, alarm, dialogue6, action1, action2, action3, action4, action5, time1, dialogue5, action6, action7, action8, action9, action10, action11, action12, time2, action14, action15, action16, action17, action18, action19, action20, dialogue16, response1, dialogue17, action21, memory1, action22, dialogue18, memory2, dialogue19, memory3, memory4, memory5, memory6, memory7, action23, dialogue20, action24, time3, action25, action26]
            typewrite_list(everydialogue, 0.08, 0.1, 2)


def dialogueEndCredits():
    keepgoing = '0'
    while keepgoing == '0':
        keepgoing = input("Skip End Credits? [Y/N]: ")
        if keepgoing.upper() == 'Y':
            return
        elif keepgoing.upper() == 'N':
            break
        else:
            print("Stella: Make up your mind!!")
            keepgoing = '0'

    credits1 = "Stella: Pringle.Corte Productions..."
    credits2 = "Stella: Based on the movie we used to watch 'Your Name'"
    credits3 = "Stella: Thank you to Pythonista for helping Prinx to render my memories"
    credits4 = "Stella: ....."
    credits5 = "Stella: I am Stellaria Hebeto..."
    credits6 = "Stella: And t-thank you to the players f-for helping me remember my memories..."
    song = "Songs Used:"
    song1 = "Yamazakura by Taeko Onuku [from the anime 'Words Bubble Up Like Soda Pop']"
    song2 = "Fukashigi No Carte by Various Artists; Piano Cover by Mahiw - Anime on Piano [from the anime 'Rascal Does Not Dream']"
    credits7 = "-----------------------------------------------------------------------"
    

    credits8 = "Stella: Hmm? You're still here?...oh whell, I guess..who? oh right Prinx. Prinx will take over now"
    credits9 = "[PRINX THE DEV]: Yoo wsg goise I'm here now and here's some facts n' easter eggs I bet yall didn't see"
    credits10 = "[PRINX THE DEV]: Originally, there was gonna be 4 games, the fourth game being able to stroll around as if to reminisce of the old times. However, due to code complexity and young me being to hesitant to code it in, I just didn't put it in"
    credits11 = "Stella: Man, you lazy"
    credits12 = "[PRINX THE DEV]: IS 1200+ LINES OF CODE NOT ENOUGH??? REMEMBER, I HAD TO LEARN ABOUT RAYCASTING AND TRIGONOMETRY, COPY A TUTORIAL AND CODE IT INTO A NEW FILE, THEN MADE A NEW NEW FILE TO CODE MY VERY OWN CODE"
    credits13 = "[PRINX THE DEV]: Second fact--The very concept of basing this code from 'Your Name' stemmed from the inability to see each other in multiplayer while I was testing the code"
    credits14 = "[PRINX THE DEV]: This genuinely reminded me of how Mitsuha and Taki couldn't see each other in the movie"
    credits15 = "[PRINX THE DEV]: Speaking of 'Your Name', the whole lore actually lies close with the central lore of the movie: finding your soulmate despite the struggles"
    credits16 = "[PRINX THE DEV]: The name 'Stellaria Hebeto' is actually derived from Latin..."
    credits17 = "Stella: What??"
    credits18 = "[PRINX THE DEV]: It means 'Dimming Star'.."
    credits19 = "Stella: oh..."

    everydialogue = [credits7, credits1, credits2, credits3, credits4, credits5, credits6, song, song1, song2, credits8, credits9, credits10,credits11,credits12,credits13,credits14,credits15,credits16,credits17,credits18,credits19, credits7]
    typewrite_list(everydialogue, 0.09, 0.2, 2)
    return

class Map:
    def __init__(self):
        self.map1 = [
            [1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
            [1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 2, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 2, 0, 0, 2, 2, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [2, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 1],
            [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 2, 2, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1],
            [1, 2, 2, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.map2 = [
            [1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 2, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [2, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 2, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.map3 = [
            [1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 2, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 2, 2, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 2, 0, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],    
        ]
        self.TileSize = Width//3 + 1
        self.maps = {
            1:self.map1,
            2:self.map2,
            3:self.map3
        }
        global mapnum
    def wall_at(self,x,y):
        return self.maps[mapnum][int(y//TileSize)][int(x//TileSize)] != 0 

map = Map()

class Player:
    def __init__(self, x, y, max_speed, length):
        self.x = x
        self.y = y

        self.next_x = x
        self.next_y = y

        self.TOP_SPEED = max_speed
        self.MOVEMENT_SPEED = 0

        self.PLAYER_DIRECTION = 90*(math.pi/180)
        self.PLAYER_TURN_SPEED = 1.5 * (math.pi/180)

        self.PLAYER_LENGTH = length

        self.LEFT_RIGHT = 0 # -1 is left, 0 is none, 1 is right

        self.map = map

    def PLAYER_CONTROLS(self):
        self.LEFT_RIGHT = 0

        if key[pygame.K_a]:
            self.LEFT_RIGHT = -1

            if key[pygame.K_s] and key[pygame.K_a]:
                self.PLAYER_DIRECTION -= 0.009
        

        if key[pygame.K_d]:
            self.LEFT_RIGHT = -1

            if key[pygame.K_s] and key[pygame.K_d]:
                self.PLAYER_DIRECTION += 0.009

        if key[pygame.K_s]:
            if self.MOVEMENT_SPEED <= self.TOP_SPEED:             
                self.MOVEMENT_SPEED += 0.04
        else:
            if self.MOVEMENT_SPEED > 0:                
                self.MOVEMENT_SPEED -= 0.04

        if key[pygame.K_w]:
            if self.MOVEMENT_SPEED >= -self.TOP_SPEED:                
                self.MOVEMENT_SPEED -= 0.04
        else:
            if self.MOVEMENT_SPEED < 0:
                self.MOVEMENT_SPEED += 0.005
        
        self.next_x = self.x + self.MOVEMENT_SPEED*math.cos(self.PLAYER_DIRECTION)
        self.next_y = self.y + self.MOVEMENT_SPEED*math.sin(self.PLAYER_DIRECTION)
        
        if not(self.map.wall_at(self.next_x, self.next_y) or self.map.wall_at(self.next_x + self.PLAYER_LENGTH, self.next_y) or self.map.wall_at(self.next_x, self.next_y + self.PLAYER_LENGTH) or self.map.wall_at(self.next_x + self.PLAYER_LENGTH, self.next_y + self.PLAYER_LENGTH)):
            self.x = self.next_x
            self.y = self.next_y
        else:
            self.MovementSpeed *= -0.5

        self.PLAYER_DIRECTION += self.PLAYER_TURN_SPEED * self.LEFT_RIGHT

        self.x, self.y = self.next_x, self.next_y


class Raycaster():
    def __init__(self, color, player_id, starting_ray_pos):
        self.proxy = player_id
        self.map = map
        self.WALL_COLOR = color

        self.ANGLE = -FOV//2 
        self.RAY_POSITION = starting_ray_pos
        self.RAY_COUNT = PROJECTED_RAYS
        self.MIDPOINT = HEIGHT*TILESIZE/2
    def RayRenderer(self, x, y, color, starting_ray_pos):
        
        self.CENTER_X = self.FINAL_X = self.proxy.x + self.proxy.PLAYER_LENGTH
        self.CENTER_Y = self.FINAL_Y = self.proxy.y + self.proxy.PLAYER_LENGTH

        if MULTIPLAYER:
            self.ANGLE = -FOV//4
            self.RAY_POSITION = starting_ray_pos
            self.RAY_COUNT = PROJECTED_RAYS//2
        

        for ray in range(self.RAY_COUNT):
            self.FINAL_X = self.proxy.x + self.proxy.PLAYER_LENGTH
            self.FINAL_Y = self.proxy.y + self.proxy.PLAYER_LENGTH

            while not self.map.wall_at(self.FINAL_X, self.FINAL_Y):
                self.FINAL_X -= math.cos(self.proxy.PLAYER_DIRECTION + (math.pi/180)*int(self.ANGLE))
                self.FINAL_Y -= math.sin(self.proxy.PLAYER_DIRECTION + (math.pi/180)*int(self.ANGLE))
            self.DISTANCE = math.dist((self.FINAL_X, self.FINAL_Y), (self.CENTER_X, self.CENTER_Y))
            self.NORMALIZED_DISTANCE = 1/(math.cos(self.ANGLE * math.pi/180)*self.DISTANCE + 0.00001)

            self.COLOR *= 15000/(self.DISTANCE + 0.001)
            self.COLOR = max(0, self.COLOR)
            self.COLOR = min(self.COLOR, 255)

            self.RANDOM_PALETTE = random.uniform(0.1, 0.4)

            if int(MINIGAME_NUMBER) == 10:
                self.RANDOM_PALETTE = color
            
            pygame.draw.line(Screen, (int(color*self.COLOR), int(self.RANDOM_PALETTE*self.COLOR), int(color*self.COLOR)), (self.RAY_POSITION, self.MIDPOINT + self.DISTANCE*8000), (self.RAY_POSITION, self.MIDPOINT - self.DISTANCE*8000), ((WIDTH*TILE_SIZE)//PROJECTED_RAYS + 2))

## TO ADD:
## GAME MANAGER (instead of making player 1 do all the heavy lifting)
## main game loop
##figer out how did i work with the minigame number
## good night

## planning on using 
## angle = math.atan2(dx/dy)
## distance = (y1 - y2)/math.sin(angle)
## imma weigh the benefits first
