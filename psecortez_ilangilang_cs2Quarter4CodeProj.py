import pygame, time, math, sys, random
pygame.init()
Width = 15
Height = 15
FOV = 0
Resolution = 0
multiplayer = 0

TileSize = 64

Minigame_Number = 0
#pygame.mixer.init()
Num_ProjectedRays = 0
mapnum = 1
TurnSpeed = 1.4 * (math.pi/180)
TopSpeed = 4.75
MinSpeed = 0.1
Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))
wallcolor1 = 0.9
wallcolor2 = 0.1
game3finished = False
##URGENT##
#Before analyzing the code, please, please, please run it first to not spoil the story
##URGENT##
#if you don't got pygame yet, go to terminal and type 'pip install pygame'

########################################
#DISCLAIMER!!
#THE CHARACTERS AND LORE HERE ARE ALL A PART OF FICTION AND DO NOT ACTUALLY REFLECT MY REAL LIFE
#THIS IS PURELY FICTIONAL, I AM NOT DEPRESSED OR ANYTHING. I LOVE MY LIFE :))
#######################################


########################################
##DESIGN AND MENU##
########################################
def display_headers():
    for i in range(0, 60):
        print() 
    print("Your Name") 
    print("----------------------------------") 
    print("Prinx Savier E. Cortez") 
    print("b2030psecortez@pshs.edu.ph")
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

    print()
    print()

def Menu():
    pygame.display.iconify()
    print()
    global Width, Height,FOV, Resolution, Num_ProjectedRays, multiplayer
    Width = 31
    Height = 31
    FOV = 0
    Resolution = 0
    multiplayer = 0
    while Width == 31:
        Width = input("'How wide would my memory replay need to be to remember his name..?' (Screen Width [10-30]): ")
        if not Width.isdigit() or not(10<=int(Width)<=30):
            print("Do you not want me to remember...")
            print()
            Width = 31
    print()
    while Height == 31:
        Height = input("'How tall would my memory replay need to be to remember his name..?' (Screen Height [10-15]: ")
        if not Height.isdigit() or not(10<=int(Height)<=15):
            print("Do you not want me to remember...")
            print()
            Height = 31
    print()
    while FOV == 0:
        FOV = input("'How narrow was my vision when I still had him...'(FOV, [60-180], smaller is narrower view): ")
        if not FOV.isdigit() or not(60<=int(FOV)<=180):
            print("Did I really taking him for granted..")
            print()
            FOV = 0
    print()
    while Resolution == 0:
        Resolution =  input("'How vivid does my memory need to be to remember your name...'(Resolution, [1-5]. Smaller is more defined): ")
        if not Resolution.isdigit() or not(1<=int(Resolution)<=5):
            print("Did I forget to take my meds again...why is everything so blocky?")
            print()
            Resolution = 0
    print()
    while multiplayer == 0:
        multiplayer = input("Does...does my memory involve..'him'? (number people playing [1-2]. 2 Players required for Narrative Story (Don't worry, you can play Multiplayer with only yourself but it's gonna take longer, trust)): ")
        if not multiplayer.isdigit() or not(1<=int(multiplayer)<=2):
            print("My mind can't handle that much...")
            print()
            multiplayer = 0
    Width = int(Width)
    Height = int(Height)
    FOV = int(FOV)
    Resolution = int(Resolution)

    if multiplayer == '2':
        multiplayer = True
    else:
        multiplayer = False
    basics = '[SYSTEM]: To move around, press WASD/Arrow Key. If playing on multiplayer, player "Stella" is on the left, and player "cloverforever0905" on the right'
    for i in basics:
        print(i, end='', flush=True)
        time.sleep(0.04)
    Num_ProjectedRays = FOV//Resolution
    if Num_ProjectedRays == 0:
        Num_ProjectedRays = 1

def MultiplayerMenu():
    print()
    
    seperator = '---------------------'
    for i in seperator:
        print(i, end='', flush=True)
        time.sleep(0.1)
    print()
    print()
    today = '[SYSTEM]: What are we doing today?'
    for i in today:
        print(i, end='', flush=True)
        time.sleep(0.1)
    print()
    gameslist = ["[1] 'Young Stella: 'I challenge you to Montgeometry Racers!!'", "[2] 'Young ████: 'let's play Blind and Seek'", "[3] Open Google Chrome", "[4] Shut Down Lenovo ThinkPad X100e"]
    error = ["Geometry_Dash.exe", "File not found.", "Check the file name and try again"]
    gamefiles = [MRH,BS]

    for i in gameslist:
        print(i)
    global Minigame_Number
    Minigame_Number = 0
    print()
    if int(Minigame_Number)==10:
        MS.GameStart()

    while not(1<=int(Minigame_Number)<=4 or int(Minigame_Number) == 10):
        Minigame_Number = input("what..what memory should I try to remember? [1-4]: ")
        if not Minigame_Number.isdigit() or not(1<=int(Minigame_Number)<=4):
            for i in error:
                print(i)
            Minigame_Number = 0
            print()
            continue
        if int(Minigame_Number) == 10:
            break
        elif int(Minigame_Number) == 3:
            dialogue1_5()
            MultiplayerMenu()
        elif int(Minigame_Number) == 4:
            break
        else:
            gamefiles[int(Minigame_Number) - 1].GameStart()

    
def choiceToPlay():
    global Minigame_Number, i_still_wanna_play
    i_still_wanna_play = 'f'
    while i_still_wanna_play.upper() != 'Y' and i_still_wanna_play.upper() !='N':
        pygame.display.iconify()
        print()
        i_still_wanna_play = input("Stella: Should I try to recall once more? [Y/N]: ")

        if i_still_wanna_play.upper() == 'Y':
            givingup = 'Stella: I am not giving up!!'
            for i in givingup:
                print(i, end='', flush=True)
                time.sleep(0.1)
            print()
            print()
            global MultiplayerMenuInitializitationCounter, SinglePlayerInitializationCounter, dialogue1counter, player, player2, RayCasterFunc, RayCasterFunc2, MRH, BS,MS, map,Width, Height, TileSize, Resolution, multiplayer, Minigame_Number, Num_ProjectedRays, mapnum, TurnSpeed, TopSpeed, MinSpeed, wallcolor1 , wallcolor2
            player = Player()
            player2 = Player2()
            RayCasterFunc = Raycaster()
            RayCasterFunc2 = Raycaster2()
            MRH = MontgeometryRacers()
            BS = BlindSeek()
            MS = MountainScene()
            map = Map()
            Width = 30
            Height = 16
            TileSize = 64
            Resolution = 0
            multiplayer = 0
            Minigame_Number = 0
            #pygame.mixer.init()
            Num_ProjectedRays = 0
            mapnum = 1
            TurnSpeed = 1.5 * (math.pi/180)
            TopSpeed = 4.75
            MinSpeed = 0.1
            Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))
            wallcolor1 = 0.9
            wallcolor2 = 0.1
            SinglePlayerInitializationCounter = 0
            MultiplayerMenuInitializitationCounter = 0
            dialogue1counter = 0
            break
        elif i_still_wanna_play.upper() == 'N':
            Exit1()
            break
        else:
            wrong = "Stella: Huh? ", i_still_wanna_play, "? Free cheeseburgers? Wrong thought..."
            for i in wrong:
                print(i, end='', flush=True)
                time.sleep(0.1)
            continue
        

############################################
##Minigame_NumberS##
############################################
class MontgeometryRacers():
    global mapnum
    mapnum = 1

    def __init__(self):
        self.starttime, self.starttime2 = 0, 0
        self.timer, self.timer2 = 0, 0
        self.timeelapses, self.timeelapses2 = 0, 0      
        self.gamestate, self.gamestate2 = 'Not Yet Started', 'Not Yet Started'  
        self.winner = 'e'
        self.dialogue_chance = random.randint(0,20)

    def GameStart(self):
        print()
        PsuedoGameLoading()
        print()
        title = "Memory II: I'm With You Till the End of the Line"
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

    def Referee(self, name, coordxplayer, coordyplayer):
        startlineymin = 275
        startlineymax = 285
        startlinexmin = 150
        startlinexmax = 260
        winner = 0
            
        if (startlineymin <= coordyplayer <= startlineymax) and (startlinexmin <= coordxplayer <= startlinexmax):
            
            if self.gamestate == "Not Yet Started" :
                if name == 'sT311a38':
                    print()
                    print("Timer started (", name,") 0 : 00 : 00")
                    self.starttime = pygame.time.get_ticks()
                    self.gamestate = "Racing"

            if self.gamestate2 == 'Not Yet Started':
                if name == 'cloverforever0905':
                    print()
                    print("Timer started (", name,") 0 : 00 : 00")
                    self.starttime2 = pygame.time.get_ticks()
                    self.gamestate2 = "Racing"
                
            if self.gamestate == 'Racing':
                if name == 'sT311a38':
                    if self.timeelapses//1000 > 5:
                        print()
                        print("Timer ended. ", name, "'s Results: ",str(self.timeelapses//60000),":", str((self.timeelapses - 60000*(self.timeelapses//60000))//1000),":",str(self.timeelapses%1000))
                        self.gamestate = "Finished"
           
            if self.gamestate2 == 'Racing':
                if name == 'cloverforever0905':
                    if self.timeelapses2//1000 > 5:
                        print()
                        print("Timer ended. ", name, "'s Results: ",str(self.timeelapses2//60000),":", str((self.timeelapses2 - 60000*(self.timeelapses2//60000))//1000),":",str(self.timeelapses2%1000))
                        self.gamestate2 = "Finished"
        
        if self.gamestate == "Racing":
            if name == 'sT311a38':
                self.timer = pygame.time.get_ticks()
                self.timeelapses = abs(self.starttime - self.timer)
        if self.gamestate2 == 'Racing':
            if name =='cloverforever0905':
                self.timer2 = pygame.time.get_ticks()
                self.timeelapses2 = abs(self.starttime2 - self.timer2)

        if self.gamestate == 'Finished':
            winner = 3 
        
        if self.gamestate == 'Finished' and self.gamestate2 == 'Finished':
            if self.timeelapses > self.timeelapses2:
                winner = 0
            elif self.timeelapses < self.timeelapses2:
                winner = 1
            else:
                winner = 2
            pygame.display.iconify()
            return winner
        
        if self.dialogue_chance == 1:
            for i in random.choice(MGR_dialogues_Stella):
                print(i, end = '', flush= True)
            for i in random.choice(MGR_dialogues_1234):
                print(i, end='', flush=True)
        
MRH = MontgeometryRacers()

class BlindSeek():
    def __init__(self):
        self.player1x, self.player1y = 0, 0
        self.player2x, self.player2y = 0, 0
        self.distance = 0
        self.timer = 0
        self.gamestate = False
        self.keystate = False
        self.lkeypress = 0

    def GameStart(self):
        print()
        PsuedoGameLoading()
        print()
        title = "Memory III: Dancing In The Dark"
        for i in title:
            print(i, end='', flush=True)
            time.sleep(0.09)
        print()
        rules = "[SYSTEM]:The hider will be given 1 min(s) to hide somewhere in the map and the seeker will be given 2 min(s) to find the seeker. The seeker must find the other guy. Since you are 'blind' and none of you can see the other, press the 'L' key to know how far you are to the other player. Once 1 min(s) is up, the hider isn't allowed to move. Oh and also, you can't press the 'L' key more than eight (8) times [Open the game window]"
        for i in rules:
            print(i, end = '', flush = True)
            time.sleep(0.05)
        print()
        Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))
        time.sleep(1)

    def Rules(self):
        global coin_flip
        coin_flip = random.randint(0,1)
        
        if coin_flip == 1:
            system = ["[SYSTEM]: sT311a38 is the hider!", "cloverforever0905 is the seeker!"]
            for i in system:
                print(i)
        else:
            system = ["[SYSTEM]: cloverforever0905 is the hider!", "sT311a38 is the seeker!"]
            for i in system:
                print(i, flush = True)
                time.sleep(0.5)
        print("[SYSTEM]: Hider, start hiding!! (Open game window)")
        self.starttimer = pygame.time.get_ticks()

    def Referee(self,name, coordx, coordy):
        key = pygame.key.get_pressed()
        if name == 'sT311a38':
            self.player1x = coordx
            self.player1y = coordy
        if name == 'cloverforever0905':
            self.player2x = coordx
            self.player2y = coordy
        self.endtimer = pygame.time.get_ticks()
        global stellawon

        if self.timer >= 1200:
            if self.gamestate == False:
                print()
                print("[SYSTSEM]: Seeker...start finding!!")   
                self.gamestate = True
            self.distance = math.sqrt((self.player2x - self.player1x)**2 + (self.player2y - self.player1y)**2)/32

            if abs(self.endtimer - self.starttimer)//60000 <= 2:
                if int(self.distance) < 4:
                    pygame.display.iconify()
                    if coin_flip == 1:
                        #clover is seeker
                        stellawon = '0'
                        return stellawon
                    else:
                        #stella is seeker
                        stellawon = '1'
                        return stellawon
                if self.lkeypress <= 8:
                    if key[pygame.K_l]:
                        if not self.keystate:
                            print("[SYSTEM]: Hider is ", str(int(self.distance)), "m away")
                            self.keystate = True
                            self.lkeypress += 1
                    else:
                        self.keystate = False
                else:
                    print("[SYSTEM]: You used up all your presses!!")
                self.distance = math.sqrt((self.player2x - self.player1x)**2 + (self.player2y - self.player1y)**2)/64
                    
                self.endtimer = pygame.time.get_ticks() 
        if self.timer >= 4800:
            if coin_flip == 1:
                stellawon = '1'
                return stellawon
            else:
                stellawon = '0'
                return stellawon

        self.timer += 1
                
BS = BlindSeek()

class MountainScene():
    global Minigame_Number
    def __init__(self):
        self.player1x, self.player1y = 0, 0
        self.player2x, self.player2y = 0, 0
        self.distance = 0
        self.gamestate = False
        self.keystate = False
        self.lkeypress = 0
        self.minxtresh = 1330
        self.gamefinished = False

    def GameStart(self):
        print()
        PsuedoGameLoading()
        print()
        title = "Memory IV: Kimi No Wa Na."
        for i in title:
            print(i, end='', flush=True)
            time.sleep(0.09)
        print()
        if self.gamestate == False:
            print("[Stella's Consiousness]: Keep moving forward until you see our mountain hideout!! Press L to see how far you are from there!! (Open game window)")   
            self.gamestate = True
        Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))

    def Referee(self,name, coordx, coordy):
        key = pygame.key.get_pressed()
        if name == 'sT311a38':
            self.player1x = coordx
            self.player1y = coordy
        if name == 'cloverforever0905':
            self.player2x = coordx
            self.player2y = coordy
        self.endtimer = pygame.time.get_ticks()

        

        self.distance = math.sqrt((self.player2x - self.player1x)**2 + (self.player2y - self.player1y)**2)/64

        if self.minxtresh <= self.player1x:
            pygame.display.iconify()
            self.gamefinished = True
            global game3finished
            game3finished = True
            
        if key[pygame.K_l]:
            if not self.keystate:
                print("[Stella's memory]: Our hideout is ", str(int(self.distance)), "m away!!")
                self.keystate = True
            else:
                self.keystate = False
        
        self.distance = math.sqrt((self.player2x - self.player1x)**2 + (self.player2y - self.player1y)**2)/64
        return self.gamefinished
MS = MountainScene()                    

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
    dialogue0 = '"What used to be the joy could lead to the devastation of one."'

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
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
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
                print(y, end='', flush=True)
                time.sleep(0.05)
                continue
            if i == (dialogue5 or dialogue6):
                print(y, end='', flush=True)
                time.sleep(0.08)
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
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.5)
        print()
    print()
    dialogue3_1()
def dialogue2_5():
    #winner is stella  
    print()
    dialogue1 = "'Young Stella: Hahaha I told you I would beat you!! I wasn't even TRYING bro'"
    dialogue2 = "'Young ████: BULLY. I WAS NEW TO THE GAME. I WAS STILL LEARNING. I WAS---'"
    dialogue3 = "'Young Stella: Yap yap yappity yap, stop making excuses and go back to playing SNAKE'"
    dialogue4 = "'Young ████:*whimpers* lets just play another round...'"
    everydialogue = [dialogue1, dialogue2, dialogue3, dialogue4]
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.5)
        print()
    print()
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
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.3)
        print()
    print()
    
def dialogue4():
    #STELLA WON
    dialogue1 = "Young Stella: BRO YOU DIDN'T EVEN TRY"
    dialogue2 = "Young ████: OH COME ON, WE BOTH KNOW YOUR GOOD AT FINDING AND HIDING. AFTER ALL, YOU GOTTA KEEP FINDING FOR YOUR NINTENDO 3DS AFTER YOUR MOM KEEPS TAKING IT AWAY CUZ YOU HAVE A SHORT ATTENTION SPAN EVERYTIME YOU PLAY IT"
    dialogue3 = "Young Stella: *puts her hand on her chest* Me??? Short attention span?? NO I DONT HAVE A SHORT ATTENTION SPA...woah lookie over there, a cool car!! wooooooo..."
    action1 = "Young Stella: *looks back at ████*"
    dialogue4 = "Young Stella: I dont have a short attention span and I'm just good at finding things, got it?? Hmph!"
    dialogue5 = "Young ████: *faces the player* (jokingly) THIS is what I gotta deal with everyday"
    everydialogue = [dialogue1, dialogue2, dialogue3, action1, dialogue4, dialogue5]
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.4)
        print()
    print()
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
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.4)
        print()
    print()
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
    for i in everydialogue:
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.1)
        time.sleep(0.6)
        print()
    print()

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
                    print(y, end='', flush=True)
                    time.sleep(0.09)
                if i == dialogue18:
                    print()
                print()    

            dialogueEndCredits()

            everydialogue = [end, name]
            print()
            print()
            for i in everydialogue:
                for y in i:
                    print(y, end ='', flush=True)
                    if i == name:
                        time.sleep(0.5)
                    else:
                        time.sleep(0.09) 
                print()
                print()
                #pygame.mixer.music.fadeout(3)
                sys.exit()      
        else:
            everydialogue = [dialogue1, dialogue2, dialogue3, sequence, dialogue4, sequence, alarm, dialogue6, action1, action2, action3, action4, action5, time1, dialogue5, action6, action7, action8, action9, action10, action11, action12, time2, action14, action15, action16, action17, action18, action19, action20, dialogue16, response1, dialogue17, action21, memory1, action22, dialogue18, memory2, dialogue19, memory3, memory4, memory5, memory6, memory7, action23, dialogue20, action24, time3, action25, action26]
            for i in everydialogue:
                for y in i:
                    print(y, end='', flush=True)
                    time.sleep(0.09)
                print()
                time.sleep(0.1)
            print()
        
            print()
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
    for i in everydialogue:
        #if i == credits1:
            #pygame.mixer.music.fadeout(3)
            #pygame.mixer.music.load("Fukashigi No Carte.mp3")
            #pygame.mixer.music.play()
        for y in i:
            print(y, end='', flush=True)
            time.sleep(0.09)
        print()
        time.sleep(0.2)
    print()
    return

 ###################
 ##OBJECTS/CLASSES##
 ###################   
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
    def __init__(self):
        self.x = 208
        self.y = 288
        self.MovementSpeed = 0
        self.ActualSpeed = 0
        self.PlayerFacingDirection = 90 * (math.pi / 180)
        self.PlayerTurnSpeed = TurnSpeed
        self.LeftRightBool= 0
        self.map = map
        self.PlayerSideLength = 5
        #gamefunctions
        self.MRH = MRH
        self.BS = BS
        self.MountainScene = MS
        #calculates next position
        self.next_x = 0
        self.next_y = 0 
        #sets up spawnpoint
        self.game1setup = 0
        self.game2setup = 0
        self.game3setup = 0
        #to run rules only once
        self.dice_rolled = 0
        #to check games played so far
        self.gameadder = 0
        self.gameadder2 = 0
        self.GamesPlayed = []
        #validate for final exit
        global game3finished
        game3finished = False

    def PlayerController(self):
        global Minigame_Number, mapnum, wallcolor1, TopSpeed
        self.LeftRightBool= 0
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.LeftRightBool= -1
            if key[pygame.K_s] and key[pygame.K_a]:
                self.PlayerFacingDirection -= 0.009
          
        if key[pygame.K_d]:
            self.LeftRightBool= 1
            if key[pygame.K_s] and key[pygame.K_d]:
                self.PlayerFacingDirection += 0.009
                
        if key[pygame.K_s]:
    
            if self.MovementSpeed <= TopSpeed:             
                self.MovementSpeed += 0.04
        else:
           
            if self.MovementSpeed > 0:                
                self.MovementSpeed -= 0.04

        if key[pygame.K_w]:
           
            if self.MovementSpeed >= -TopSpeed:                
                self.MovementSpeed -= 0.04
        else:
        
            if self.MovementSpeed < 0:
                self.MovementSpeed += 0.005
            
        if abs(self.MovementSpeed) <= MinSpeed and not(key[pygame.K_s] or key[pygame.K_w]):
                self.MovementSpeed = 0
        
        self.ActualSpeed = self.MovementSpeed

        self.next_x = self.x + self.ActualSpeed*math.cos(self.PlayerFacingDirection)
        self.next_y = self.y + self.ActualSpeed*math.sin(self.PlayerFacingDirection)

        if not(self.map.wall_at(self.next_x, self.next_y) or self.map.wall_at(self.next_x + self.PlayerSideLength, self.next_y) or self.map.wall_at(self.next_x, self.next_y + self.PlayerSideLength) or self.map.wall_at(self.next_x + self.PlayerSideLength, self.next_y + self.PlayerSideLength)):
            self.x = self.next_x
            self.y = self.next_y
        else:
            self.MovementSpeed *= -0.5

        self.PlayerFacingDirection += self.PlayerTurnSpeed * self.LeftRightBool
        
        self.ActualSpeed = self.MovementSpeed
        self.x +=  self.ActualSpeed * math.cos(self.PlayerFacingDirection)
        self.y += self.ActualSpeed * math.sin(self.PlayerFacingDirection)

        
        if multiplayer == True:
            if int(Minigame_Number) == 1:
                #self.MRH.Referee('sT311a38', int(self.x), int(self.y))
                if self.game1setup == 0:
                    self.x = 208
                    self.y = 288
                    self.PlayerFacingDirection = 90 * (math.pi / 180)
                    self.ActualSpeed = 0
                    self.game1setup = 1
                result = self.MRH.Referee('sT311a38', int(self.x), int(self.y))
            
                if result == 0:
                    print()
                    print("[SYSTEM]: Congratulations to cloverforever0905!! You are the victor!")
                    Minigame_Number = 0
                    time.sleep(1)
                    if self.gameadder == 0:
                        self.GamesPlayed.append('1')
                        self.gameadder += 1
                    dialogue2_()
                    MultiplayerMenu()
                    return
                        
                elif result == 1:
                    print()
                    print("[SYSTEM]: Congratulations to sT311a38!! Keep shining!!")
                    Minigame_Number = 0
                    time.sleep(1)
                    if self.gameadder == 0:
                        self.GamesPlayed.append('1')
                        self.gameadder += 1
                    dialogue2_5()
                    MultiplayerMenu()
                    return
                        
                elif result == 2:
                    print()
                    print("[SYSTEM]: Draw?! Wow how is that even possible...")
                    Minigame_Number = 0
                    if self.gameadder == 0:
                        self.GamesPlayed.append('1')
                        self.gameadder += 1
                    return
    
            elif int(Minigame_Number) == 2:
                if self.game2setup == 0:
                    self.x = 208
                    self.y = 288
                    self.PlayerFacingDirection = 90 * (math.pi / 180)
                    self.game2setup = 1
                    self.ActualSpeed = 0
                mapnum = 2 
                stellawon = self.BS.Referee('sT311a38', int(self.x + self.PlayerSideLength//2), int(self.y + self.PlayerSideLength//2))
                    
                if self.dice_rolled == 0:
                    self.BS.Rules()
                    self.dice_rolled += 1
                    
                if stellawon == '1':
                    print("[SYSTEM]: Congrats to sT311a38!! Are you a star or what??")
                    Minigame_Number = 0
                    time.sleep(0.5)
                    if self.gameadder2 == 0:
                        self.GamesPlayed.append('2')
                        self.gameadder2 += 1
                    dialogue4()
                    MultiplayerMenu()
                    
                elif stellawon == '0':
                    print("[SYSTEM]: Congrats to cloverforever0905. Zayum you da goat bro")
                    Minigame_Number = 0
                    time.sleep(0.5)
                    if self.gameadder2 == 0:
                        self.GamesPlayed.append('2')
                        self.gameadder2 += 1
                    dialogue4_5()
                    MultiplayerMenu()
                    

            elif int(Minigame_Number) == 10:
                TopSpeed = 1
                checker = self.MountainScene.Referee('sT311a38', int(self.x + self.PlayerSideLength//2), int(self.y + self.PlayerSideLength))
                wallcolor1 = 0.9
                mapnum = 3
                if self.game3setup == 0:
                    self.ActualSpeed = 0
                    self.x = 208
                    self.y = 320
                    self.game3setup = 1
                    self.PlayerFacingDirection = 180*math.pi/180
                    self.MountainScene.GameStart()
                    
                if checker == True:
                    dialogue1 = "As Stella bursts through the crisp snow of the old mountain, a familiar feeling sweeps through her"
                    dialogue2 = "It's here..."
                    Exit1() 
                    everydialogue = [dialogue1, dialogue2]
                    for i in everydialogue:
                        for y in i:
                            print(y, end='', flush=True)
                            time.sleep(0.08)
                        print()
                    self.game3finished = True
                    checker = False
               
                      

    
player = Player()        


class Raycaster():
    def __init__(self):
        self.proxy = player
        self.map = map
    def RayRenderer(self):
        self.finaldotx = self.proxy.x + self.proxy.PlayerSideLength//2
        self.finaldoty = self.proxy.y + self.proxy.PlayerSideLength//2
        self.AngleDiffBetweenRays = -FOV//2
        self.PositionRay = 5
        self.Num_ProjectedRays = Num_ProjectedRays

        if multiplayer == True:
            self.AngleDiffBetweenRays = -FOV//4
            self.PositionRay = 10
            self.Num_ProjectedRays = Num_ProjectedRays//2
            
        self.vertical = 1
        self.baseline = self.proxy.PlayerFacingDirection - 90*math.pi/180
        
        #for each ray (FOV/RES)
        for i in range(self.Num_ProjectedRays):
            self.color = 1
            self.linedotx = self.proxy.x + self.proxy.PlayerSideLength//2 
            self.linedoty = self.proxy.y + self.proxy.PlayerSideLength//2
            self.finaldotx = self.proxy.x + self.proxy.PlayerSideLength//2
            self.finaldoty = self.proxy.y + self.proxy.PlayerSideLength//2
            
            self.midpoint = Height*TileSize/2

            #are we there yet? - finaldotx and finaldoty
            while self.map.wall_at(self.finaldotx, self.finaldoty) == False:
                self.finaldotx -= math.cos(self.proxy.PlayerFacingDirection + (math.pi/180)*int(self.AngleDiffBetweenRays))
                self.finaldoty -= math.sin(self.proxy.PlayerFacingDirection + (math.pi/180)*int(self.AngleDiffBetweenRays))
            self.vertical1 = math.sqrt(((self.finaldotx - self.linedotx)**2) + ((self.finaldoty - self.linedoty)**2))
            self.vertical = 1/(math.cos(self.AngleDiffBetweenRays * math.pi/180)*self.vertical1 + 0.0001)
        
            #calculates color
            self.color *= 15000/(math.sqrt(((self.finaldotx - self.linedotx)**2) + ((self.finaldoty - self.linedoty)**2))+0.001)
            if self.color > 255:
                self.color = 255
            if self.color < 0:
                self.color = 0
            self.randomcolor = random.uniform(0.1, 0.4)
            if int(Minigame_Number) == 10:
                self.randomcolor = wallcolor1
            pygame.draw.line(Screen, (int(wallcolor1*self.color), int(self.randomcolor*self.color), int(wallcolor1*self.color)), (self.PositionRay, self.midpoint + self.vertical*8000), (self.PositionRay, self.midpoint - self.vertical*8000), ((Width*TileSize)//Num_ProjectedRays + 2))
            
            self.PositionRay += Width*TileSize/Num_ProjectedRays
            self.AngleDiffBetweenRays += Resolution
          
        
RayCasterFunc = Raycaster()

#player 2
class Player2:
    def __init__(self):
        self.x = 208
        self.y = 288
        self.MovementSpeed = 0
        self.ActualSpeed = 0
        self.PlayerFacingDirection = 90 * (math.pi / 180)
        self.PlayerTurnSpeed = TurnSpeed
        self.LeftRightBool= 0
        self.map = map
        self.PlayerSideLength = 5
        #gamefunctions
        self.MRH = MRH
        self.BS = BS
        self.MountainScene = MS
        #calculates next position
        self.next_x = 0
        self.next_y = 0 
        #sets up spawnpoint
        self.game1setup = 0
        self.game2setup = 0

    def PlayerController2(self):
        self.LeftRightBool= 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.LeftRightBool= -1
            if key[pygame.K_DOWN] and key[pygame.K_LEFT]:
                self.PlayerFacingDirection -= 0.009
          
        if key[pygame.K_RIGHT]:
            self.LeftRightBool= 1
            if key[pygame.K_DOWN] and key[pygame.K_RIGHT]:
                self.PlayerFacingDirection += 0.009
                
        if key[pygame.K_DOWN]:
    
            if self.MovementSpeed <= TopSpeed:             
                self.MovementSpeed += 0.04
        else:
           
            if self.MovementSpeed > 0:                
                self.MovementSpeed -= 0.04

        if key[pygame.K_UP]:
           
            if self.MovementSpeed >= -TopSpeed:                
                self.MovementSpeed -= 0.04
        else:
        
            if self.MovementSpeed < 0:
                self.MovementSpeed += 0.005
            
        if abs(self.MovementSpeed) <= MinSpeed and not(key[pygame.K_DOWN] or key[pygame.K_UP]):
                self.MovementSpeed = 0
        
        self.ActualSpeed = self.MovementSpeed

        self.next_x = self.x + self.ActualSpeed*math.cos(self.PlayerFacingDirection)
        self.next_y = self.y + self.ActualSpeed*math.sin(self.PlayerFacingDirection)

        if not(self.map.wall_at(self.next_x, self.next_y) or self.map.wall_at(self.next_x + self.PlayerSideLength, self.next_y) or self.map.wall_at(self.next_x, self.next_y + self.PlayerSideLength) or self.map.wall_at(self.next_x + self.PlayerSideLength, self.next_y + self.PlayerSideLength)):
            self.x = self.next_x
            self.y = self.next_y
        else:
            self.MovementSpeed *= -0.5

        self.PlayerFacingDirection += self.PlayerTurnSpeed * self.LeftRightBool
        
        self.ActualSpeed = self.MovementSpeed
        self.x +=  self.ActualSpeed * math.cos(self.PlayerFacingDirection)
        self.y += self.ActualSpeed * math.sin(self.PlayerFacingDirection)


        global mapnum
        if multiplayer == True:
            if int(Minigame_Number) == 1:
                if self.game1setup == 0:
                    self.x = 208
                    self.y = 288
                    self.PlayerFacingDirection = 90 * (math.pi / 180)
                    self.ActualSpeed = 0
                    self.game1setup = 1
                mapnum = 1
                self.MRH.Referee('cloverforever0905', int(self.x), int(self.y))
            elif int(Minigame_Number) == 2:
                if self.game2setup == 0:
                    self.x = 208
                    self.y = 288
                    self.PlayerFacingDirection = 90 * (math.pi / 180)
                    self.ActualSpeed = 0
                    self.game2setup = 1
                mapnum = 2  
                self.BS.Referee('cloverforever0905', int(self.x + self.PlayerSideLength//2), int(self.y + self.PlayerSideLength//2))
            elif int(Minigame_Number) == 10:
                global wallcolor2
                self.x = 1323
                self.y = 320
                wallcolor2 = 0.5
                self.PlayerFacingDirection = 0
                self.MountainScene.Referee('cloverforever0905', int(self.x + self.PlayerSideLength//2), int(self.y + self.PlayerSideLength//2))
        

player2 = Player2()        

class Raycaster2():
    def __init__(self):
        self.proxy = player2
        self.map = map
    def RayRenderer(self):
        self.finaldotx = self.proxy.x + self.proxy.PlayerSideLength//2
        self.finaldoty = self.proxy.y + self.proxy.PlayerSideLength//2

        self.AngleDiffBetweenRays = -FOV//4
        self.PositionRay = Width*TileSize/2 + 10

        self.vertical = 1
        self.baseline = self.proxy.PlayerFacingDirection - 90*math.pi/180

        #for each ray (FOV/RES)
        for i in range(Num_ProjectedRays//2):
            self.color = 1
            self.linedotx = self.proxy.x + self.proxy.PlayerSideLength//2 
            self.linedoty = self.proxy.y + self.proxy.PlayerSideLength//2
            self.finaldotx = self.proxy.x + self.proxy.PlayerSideLength//2
            self.finaldoty = self.proxy.y + self.proxy.PlayerSideLength//2
            
            self.midpoint = Height*TileSize/2

            #are we there yet? - finaldotx and finaldoty
            while self.map.wall_at(self.finaldotx, self.finaldoty) == False:
                self.finaldotx -= math.cos(self.proxy.PlayerFacingDirection + (math.pi/180)*int(self.AngleDiffBetweenRays))
                self.finaldoty -= math.sin(self.proxy.PlayerFacingDirection + (math.pi/180)*int(self.AngleDiffBetweenRays)) 
            self.vertical1 = math.sqrt(((self.finaldotx - self.linedotx)**2) + ((self.finaldoty - self.linedoty)**2))
            self.vertical = 1/(math.cos(self.AngleDiffBetweenRays * math.pi/180)*self.vertical1 + 0.0001)
        
            #calculates color
            self.color *= 10000/(math.sqrt(((self.finaldotx - self.linedotx)**2) + ((self.finaldoty - self.linedoty)**2))+0.001)
            if self.color > 255:
                self.color = 255
            if self.color < 0:
                self.color = 0
            self.randomcolor = random.uniform(0.7, 0.9)
            if int(Minigame_Number) == 10:
                self.randomcolor = wallcolor2
            pygame.draw.line(Screen, (int(wallcolor2*self.color), int(self.randomcolor*self.color), int(wallcolor2*2*self.color)), (self.PositionRay, self.midpoint + self.vertical*8000), (self.PositionRay, self.midpoint - self.vertical*8000), ((Width*TileSize)//Num_ProjectedRays) + 2)
        
            self.PositionRay += Width*TileSize/Num_ProjectedRays
            self.AngleDiffBetweenRays += Resolution
          
       
RayCasterFunc2 = Raycaster2()

def Exit1():
    global Minigame_Number, state
    state = 0

    #if both games have been played
    if '1' in player.GamesPlayed and '2' in player.GamesPlayed:
        Minigame_Number = 10
        dialogueFinal()


    else:
        worry = "Stella: I-I don't think I'm ready to recall the memories yet...maybe another time..."
        action = "Stella turns off the dusty old machine, and it powers off with a sigh"
        print("Shutting Down...")
        everydialogue = [worry, action]
        for i in everydialogue:
            for y in i:
                print(y, end='', flush=True)
                time.sleep(0.1)
            print()

        sys.exit()
        
RefreshRate = pygame.time.Clock()
i_still_wanna_play = 'Y'
dialogue1counter = 0
MultiplayerMenuInitializitationCounter = 0
pygame.mixer.music.load("21 大貫妙子 - YAMAZAKURA.flac")
GameState = True
GlobalTimersecs = 0
SinglePlayerInitializationCounter = 0
################################
##MAIN LOOP##
################################
while True:
    pygame.init()
    while i_still_wanna_play.upper() == 'Y' :
        Menu()
        #pygame.mixer.music.play()
        Screen = pygame.display.set_mode((Width*TileSize, Height*TileSize))
        print()
        GameState = True

        #checks if game loop is running
        while GameState:
            key = pygame.key.get_pressed()
            RefreshRate.tick(20)


            Screen.fill((20,1,20))
            pygame.draw.rect(Screen, (50, 57, 22), (0, Height*TileSize/2, Width*TileSize, Height*TileSize/2))

            if int(Minigame_Number) == 10:
                    pygame.draw.rect(Screen, (150, 150, 150), (0, Height*TileSize/2, Width*TileSize, Height*TileSize/2))

            if multiplayer == False:
                if SinglePlayerInitializationCounter == 0:
                    MRH.GameStart()
                    SinglePlayerInitializationCounter = 1

                MRH.Referee("sT311a38", player.x, player.y)
            
            player.PlayerController()
            RayCasterFunc.RayRenderer()

            if multiplayer == True:
                if dialogue1counter == 0:
                    pygame.display.iconify()
                    dialogue1()
                    dialogue1counter += 1

                if MultiplayerMenuInitializitationCounter == 0:
                    print()
                    realization()
                    MultiplayerMenu()
                    MultiplayerMenuInitializitationCounter += 1

                player2.PlayerController2()
                RayCasterFunc2.RayRenderer()
                pygame.draw.line(Screen, (255, 255, 255), (Width*TileSize/2, 0), (Width*TileSize/2, Height*TileSize), 10)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameState = False
                    print()
                    print("Stella: Dang it...I forgot once again")
                    print()
                    Minigame_Number = 0
                    if multiplayer == True:
                        MultiplayerMenu()
                    else:
                        break
            
            pygame.display.update()

            #
            if GlobalTimersecs % 1000 == 0:
                print()
                print(random.choice(list_of_thoughts))
           
            GlobalTimersecs += int(1)

            if int(Minigame_Number) == 4:
                break
        break

    choiceToPlay()


    print()    
