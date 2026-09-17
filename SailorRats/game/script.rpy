# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(" Jeoseung Saja ")
define a = Character(" Amarok ")
define mc = Character ("  You  ")

default LIName = "character"
default LIStage = "normal"

define LoveInterest = Character("null")

image LI neutral = "images/characters/[LIName]/[LIStage]/neutral.png"
image LI happy = "images/characters/[LIName]/[LIStage]/happy.png"
image LI angry = "images/characters/[LIName]/[LIStage]/angry.png"
image LI sad = "images/characters/[LIName]/[LIStage]/sad.png"
image LI scared = "images/characters/[LIName]/[LIStage]/scared.png"


# The game starts here.

transform character_cent:
    zoom 0.5
    xalign 0.5
    yalign 1.0

transform character_left:
    zoom 0.5
    xalign 0.0
    yalign 1.0

transform character_right:
    zoom 0.5
    xalign 1.0
    yalign 1.0

label start:

    scene black
    call screen chooseAmarok

    return

label startDate1:
    show LI happy at character_cent
    LoveInterest "I am a person"

    LoveInterest "Where do you want to go on a date?"

    menu:
        "Go on a night hike":
            pass

        "A night hike? Why that?":
            pass

        "Okay let's go!":
            pass

   
    mc "I dont know what to say omg aahahhahs"

    return
