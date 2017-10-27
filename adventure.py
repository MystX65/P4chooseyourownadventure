import turtle
import os

xd = turtle.Turtle()
pic = turtle.Turtle()

wn = turtle.Screen()

choose_click = False

#input functions

def startOver(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            main(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def epilogue(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            missionEpilogue(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def input1(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            jungle_bush(t)
            turtle.done()
        elif x == 2:
            swamp(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
    print(x)

def inputBush(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            stream(t)
            turtle.done()
        elif x == 2:
            stone_castle(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputSwamp(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            backToBoat(t)
            turtle.done()
        elif x == 2:
            keepGoing(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputStream(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            streamToBoat(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputCastle(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            takeAShot(t)
            turtle.done()
        elif x == 2:
            goToCastle(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputExploreRuins(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            goToRoom(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputGoToCastle(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            goToRoom(t)
            turtle.done()
        elif x == 2:
            exploreRuins(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputDavid(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            sacrificeDavid(t)
            turtle.done()
        elif x == 2:
            spareDavid(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputRun(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            goToCastle(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputBackToBoat(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            run(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def inputKeepGoing(t):
    x = 0
    while x != 1 or x != 2:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            defensivePos(t)
            turtle.done()
        else:
            write_screen("Please choose a valid number", t, "grey", (0, 500))
            t.color("white")
        print(x)

def write_screen(txt, t, c, (x, y)):
    t.goto(x,y)
    t.color(c)
    t.write(txt, move=False, align="center", font=("Arial", 20, "normal"))

#-------------------------------------------------------

def title(t):
    t.up()
    t.color("black")
    t.goto(0, 300)
    t.write("Operation Jungle Tiger: Choose your own adventure!", move=False, align="center", font=("Times New Roman", 30, "normal"))
    t.color("white")

def main(t):
    t.clear()
    t.goto(0,0)
    pic.clear()
    wn.addshape(os.path.expanduser("PTBoat.gif"))
    pic.shape(os.path.expanduser("PTBoat.gif"))

    pic.penup()
    pic.goto(0, 200)
    pic.stamp()
    t.speed(0)
    title(t)
    t.goto(0,-20)
    t.color("black")
    t.write("\nIn 1971, at the height of the Vietnam war, a team of Navy Seals have been assigned a special mission.\n"
            "A former US Navy Seal squad leader has gone rogue and fled into neighboring Cambodia.\n"
            "Intelligence believes he has obtained a cult following with as many as 200 followers.\n"
            "You, squad leader Jack Cornwall, along with your five"
            " other privates are embarking on a journey deep into Cambodia.\n"
            "An extra two men have been assigned to captain the patrol boat.\n", move=False, align="center", font=("Arial", 15, "normal"))
    t.goto(0, -350)
    t.write("Please choose 1 or 2. Press Enter to exit the game.", move=False, align="center", font=("Arial", 15, "normal"))
    firstDec(xd)
    t.color("white")
    input1(xd)

def firstDec(t):
    t.speed(0)
    write_screen("You have reached the end of the river, which way do you choose to go?", t, "black", (0, -100))
    t.color("white")
    write_screen("2) We shall head right, into the swamp.", t, "black", (275, -200))
    t.color("white")
    write_screen("1) We shall head left, towards the thick jungle bush.", t, "black", (-200, -200))
    t.color("white")

#event functions

def jungle_bush(t):
    t.clear()
    pic.clear()
    pic.goto(0, 250)
    wn.addshape(os.path.expanduser("junglebush.gif"))
    pic.shape(os.path.expanduser("junglebush.gif"))
    text = "\nYou have decided to head towards the dense jungle. " \
           "\nYou pull out your machete cut away at the thick bush." \
           "\nYou hear a noise. It is coming from all around you. " \
           "\nYou can see the anomaly of some sort of humanoid." \
           "\nDavid fires a shot at it and it takes off running. " \
           "\nYou realize that there is not only one." \
           "\nDavid insists on continuing, and after a 10 minute walk, you stumble upon a clearing. " \
           "\nIn front of you lies a majestic stone castle." \
           "\nWhich way do you go now?"
    write_screen(text, t, "black", (0, -200))
    q1 = "1) Follow the stream from the lagoon."
    q2 = "2) Head straight towards the massive stone castle."
    write_screen(q1, t, "black", (-200, -300))
    write_screen(q2, t, "black", (200, -300))
    t.color("white")
    inputBush(t)

def stream(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("stream.gif"))
    pic.shape(os.path.expanduser("stream.gif"))
    text = "\nYou instruct your men to follow the stream upwards away from the lagoon." \
           "\nSuddenly, you stop. You can hear howling coming from behind you." \
           "\nYou instruct your men to take the defensive position." \
           "\nYou look further up the stream. The creature is staring at you." \
           "\nYou take aim and fire at it. It runs away, but you begin to hear the howl of more than one."
    write_screen(text, t, "black", (0, -200))
    t.color("white")
    q1 = "1) We need to head back to the boat! Now!"
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    inputStream(t)

def streamToBoat(t):
    t.clear()
    pic.clear()
    text = "\nYou instruct your men to abandon the mission and escape." \
           "\nAs you run, you can see the boat nearing, but one of the creatures lashes out at you." \
           "\nIt gets David, but you can't look back. You tell the boat captain to get you out of there." \
           "\nYour mission has been failed at the cost of one man. THE END."
    write_screen(text, t, "black", (0, -200))
    q1 = "1) Start over."
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    startOver(t)


def stone_castle(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("stonecastle.gif"))
    pic.shape(os.path.expanduser("stonecastle.gif"))
    text = "\nAs you walk towards the castle, you see something alarming." \
           "\nIn the distance is a creature. You can only make out its head in the dense jungle." \
           "\nDavid wants to shoot at it, but Jeff insists we continue to the castle." \
           "\nDo you listen to David or Jeff?"
    write_screen(text, t, "black", (0, -200))
    q1 = "1) Alright David, take a shot at it."
    q2 = "2) We can't waste our time on that. We must get to that castle."
    write_screen(q1, t, "black", (-250, -300))
    write_screen(q2, t, "black", (200, -300))
    t.color("white")
    inputCastle(t)

def takeAShot(t):
    t.clear()
    pic.clear()
    text = "\nYou instruct your men to be ready." \
           "\nDavid shoots it. It goes down instantly." \
           "\nYou and your men cautiously move towards it." \
           "\nWhen you are about 10 yards away from the corpse, you get ambushed." \
           "\nThere is not only one of those. Shots go off." \
           "\n'GO GO GO, BACK TO THE BOAT!'"
    write_screen(text, t, "black", (0, -200))
    q1 = "1) RUN BOYS, RUN!"
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    inputStream(t)

def goToCastle(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("goToCastle.gif"))
    pic.shape(os.path.expanduser("goToCastle.gif"))
    text = "\nYou instruct your men to lower their weapons to head towards the castle." \
           "\nWhen you get to the castle, you can see one of those creatures waiting their for you." \
           "\nYou tell your men to stay back. You approach it cautiously. It points towards a room." \
           "\nDo you go into the room it's pointing at, or do you choose to explore the ruins?"
    write_screen(text, t, "black", (0, -200))
    q1 = "1) Go into the room."
    q2 = "2) Explore the ruins."
    write_screen(q1, t, "black", (-200, -300))
    write_screen(q2, t, "black", (200, -300))
    t.color("white")
    inputGoToCastle(t)

def exploreRuins(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("exploreRuins.gif"))
    pic.shape(os.path.expanduser("exploreRuins.gif"))
    text = "\nYou tell the team to search the ruins for anything." \
           "\nNothing comes up."
    q1 = "1) Go into the room."
    write_screen(text, t, "black", (0, -200))
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    inputExploreRuins(t)

def goToRoom(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("goToCastle.gif"))
    pic.shape(os.path.expanduser("goToCastle.gif"))
    text = "\nYou tell David to follow you and have the rest of the team wait outside." \
           "\nInside the room, you meet your target. Sir Billy Smith." \
           "\n'It seems as if you have found my secret hideout.' - Billy Smith" \
           "\n'Alright, fatso. It seems as if your days are numbered.' - You" \
           "\n'Before you kill me, I have some important news for you.' - Billy" \
           "\nHe gives you a piece of paper" \
           "\n'A map?' - You" \
           "\n'Yes, it includes all of the VietCong's networks and plans. This will win you the war.' - Billy" \
           "\n'But I would like some payment. I want that friend of yours. I want his head.' - Billy" \
           "\nDo you accept or reject the offer?"
    q1 = "1) Sorry David, this will save more lives than one person."
    q2 = "2) I'm sorry, but I'll kill you instead of my good friend."
    write_screen(text, t, "black", (0, -230))
    write_screen(q1, t, "black", (-230, -300))
    write_screen(q2, t, "black", (300, -300))
    t.color("white")
    inputDavid(t)

def sacrificeDavid(t):
    t.clear()
    pic.clear()
    text = "\n'Alright, have it your way.' - You" \
           "\n'WHAT! JACK YOU CAN'T DO THIS!' - David" \
           "\n'This will save more lives than just you. Sorry David.' - You" \
           "\nBilly grabs a hold of David as six of the creatures escort you outside." \
           "\nYou turn around one more time and see David with a grenade in his hand." \
           "\nDavid waves goodbye to you. He blows himself up along with Billy. The creatures run away in terror." \
           "\nYou collapse onto your knees as you exit." \
           "\n'What's wrong chief?' - Jeff" \
           "\n'David is dead. Our mission is a success at the cost of one casualty. Let's get going.' - You" \
           "\nAs you walk towards the boat, no one says a single word." \
           "\n'Ay! Where have yall been?' - Hank, the boat captain" \
           "\n'David is gone.' - You" \
           "\n'Oh... Sorry about that, Jack.' - Hank"
    q1 = "1) Let's head home."
    write_screen(text, t, "black", (0, -270))
    write_screen(q1, t, "black", (0, -350))
    t.color("white")
    epilogue(t)

def spareDavid(t):
    t.clear()
    pic.clear()
    text = "\n'Sorry Billy, you won't take David.' - You" \
           "\nYou unload a full magazine into him." \
           "\n'Alright, let's get out of here.' - You" \
           "\n'Um, Jack... Where did the door go?' - David" \
           "\nSuddenly, you get ambushed by the creatures." \
           "\nYou and David are killed." \
           "\nThe rest of the team get startled by a huge group of those creatures and flee to the boat." \
           "\nMISSION FAILED: TWO CASUALTIES, MISSING IN ACTION. DEATH OF BILLY UNCONFIRMED."
    q1 = "1) Start over."
    write_screen(text, t, "black", (0, -200))
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    startOver(t)

def missionEpilogue(t):
    t.clear()
    pic.clear()
    text = "\nYou report back to base camp with the rest of the team." \
           "\nYou have been promoted to a major, and the rest of the team has been promoted to squad leader." \
           "\nThe map has been received by high command. The VietCong was crushed in a matter of 5 years." \
           "\nIn 1976, the communists surrendered, and Vietnam had a quick recovery." \
           "\nThe country prospered and is now a major trading center of the world." \
           "\nHowever, four years after the mission, in 1975, Jack Cornwall was reported Killed In Action." \
           "\nJack did not get to see days without war. Every year, his old squad visits his grave." \
           "\nIn memory of his brave deeds."
    q1 = "1) Start over."
    write_screen(text, t, "black", (0, -200))
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    startOver(t)

#-------------------------------------------------------

def swamp(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("swamp.gif"))
    pic.shape(os.path.expanduser("swamp.gif"))
    text = "\nAs you make your way into the swampy marsh, a very thick fog rolls in." \
           "\nIt has a greenish tinge to it, and the smell of a rotting corpse." \
           "\nYou instruct your men to put on their gas masks. As you continue to head north, you can hear screeches." \
           "\nSuddenly, David is attacked by the howling creature." \
           "\nYou aim your M16 at it and shoot it. The bullet goes straight through its head." \
           "\nDavid exclaims in terror,'What in god's name is that!?'" \
           "\nThe corpse has the eyes of a human, the fangs of a cobra, and the body of a chimp." \
           "\nUpon closer examination, you conclude it is an undiscovered species." \
           "\nDo you let the corpse rot and continue on or do you take the corpse back to the boat?"
    write_screen(text, t, "black", (0, -200))
    q1 = "1) We shall take the corpse to the PT Boat."
    q2 = "2) There is no time for a delivery, we must proceed."
    write_screen(q1, t, "black", (-250, -300))
    write_screen(q2, t, "black", (250, -300))
    t.color("white")
    inputSwamp(t)

def backToBoat(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("creatureAppears.gif"))
    pic.shape(os.path.expanduser("creatureAppears.gif"))
    text = "\nYou instruct Jeff and Sam to handle the corpse while the rest of the team escorts them." \
           "\nAs you are making your way back to the PT Boat, more of the creatures appear behind you." \
           "\nTheir slow tread turns into a sprint. You begin to fire at them, but it does little." \
           "\nYou instruct your men to leave the corpse and get to the boat as fast as possible."
    write_screen(text, t, "black", (0, -200))
    q1 = "1) RUN BOYS! RUN!"
    write_screen(q1,t, "black", (0, -300))
    t.color("white")
    inputBackToBoat(t)

def run(t):
    t.clear()
    pic.clear()
    text = "\nYou manage to outrun the creatures, but you find yourself lost in the jungle." \
           "\nYou take a good look around and see a castle." \
           "\nYou spot the outline of the creature in the bush line." \
           "\n'Alright, let's get going.' - You"
    q1 = "\n1) Head to the castle."
    write_screen(text, t, "black", (0, -200))
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    inputRun(t)

def keepGoing(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("creatureAppears.gif"))
    pic.shape(os.path.expanduser("creatureAppear     Qs.gif"))
    text = "\nYou begin to hear more screeches. You proceed with caution." \
           "\nWhen you turn around, you see one appear out of the bush." \
           "It begins to walk towards you. Then, a whole line of them appear."
    dialogue = "\n'ALRIGHT, LET'S GET MOVING BEFORE THOSE THINGS GET US!'" \
               "\n                                     'DON'T LOOK BACK!'"
    write_screen(text, t, "black", (0, -200))
    t.goto(0, -300)
    t.write(dialogue, move=False, align="center", font=("Arial", 20, "normal"))
    t.color("white")
    q1 = "1) Set up a defensive position in the temple a few yards in front of you."
    write_screen(q1, t, "black", (0, -400))
    t.color("white")
    inputKeepGoing(t)

def defensivePos(t):
    t.clear()
    pic.clear()
    wn.addshape(os.path.expanduser("exploreRuins.gif"))
    pic.shape(os.path.expanduser("exploreRuins.gif"))
    text = "\nYou see a small temple ruin. You instruct your men to hold there." \
           "\nAs the monsters approach, you get your M3 Grease gun ready." \
           "\nYou begin firing, but in the chaos you don't realize a pack of those things behind you." \
           "\nYou and your entire squad are wiped out." \
           "\nMISSION FAILED: SIX CASUALTIES, ALL MISSING"
    q1 = "1) Start over."
    write_screen(text, t, "black", (0, -200))
    write_screen(q1, t, "black", (0, -300))
    t.color("white")
    startOver(t)

#-------------------------------------------------------

main(xd)

wn.exitonclick()