# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(" Jeoseung Saja ")

#Normy
image s neutral = "images/characters/saja/SajaNeut.png"
image s happy = "images/characters/saja/SajaHap.png"
image s angry = "images/characters/saja/SajaAngry.png"
image s sad = "images/characters/saja/SajaSad.png"
image s scared = "images/characters/saja/SajaScared.png"

#MermanStage1
define sm = Character(" Merm-Saja? ")

image sm neutral = "images/characters/saja/SajaMerNeut.png"
image sm happy = "images/characters/saja/SajaMerHap.png"
image sm angry = "images/characters/saja/SajaMerAngry.png"
image sm sad = "images/characters/saja/SajaMerSad.png"
image sm scared = "images/characters/saja/SajaMerScared.png"

#Vampire
define sv = Character(" Vamp-Saja? ")

image sv neutral = "images/characters/saja/SajaVampNeut.png"
image sv happy = "images/characters/saja/SajaVampHap.png"
image sv angry = "images/characters/saja/SajaVampAngry.png"
image sv sad = "images/characters/saja/SajaVampSad.png"
image sv scared = "images/characters/saja/SajaVampScared.png"

#MegaVamp
define smv = Character(" MegaVamp-Saja ")

image smv neutral = "images/characters/saja/SajaMegaVampNeut.png"
image smv happy = "images/characters/saja/SajaMegaVampHap.png"
image smv angry = "images/characters/saja/SajaMegaVampAngry.png"
image smv sad = "images/characters/saja/SajaMegaVampSad.png"
image smv scared = "images/characters/saja/SajaMegaVampScared.png"


define a = Character(" Amarok ")

#Man
image a neutral = "images/characters/amarok/Amarok_Neutral.png"
image a happy = "images/characters/amarok/Amarok_Happy.png"
image a angry = "images/characters/amarok/Amarok_Angry.png"
image a sad = "images/characters/amarok/Amarok_Sad.png"
image a scared = "images/characters/amarok/Amarok_Scared.png"

#Merperson
define am = Character(" Merm-Amarok? ")

image am neutral = "images/characters/amarok/Amarok_S1_Neutral.png"
image am happy = "images/characters/amarok/Amarok_S1_Happy.png"
image am angry = "images/characters/amarok/Amarok_S1_Angry.png"
image am sad = "images/characters/amarok/Amarok_S1_Sad.png"
image am scared = "images/characters/amarok/Amarok_S1_Scared.png"

#FullMer
define mer = Character(" Merperson ")

image mer = "images/characters/merman/Merman_Final.png"

#Vamp
define av = Character(" Vamp-Amarok? ")

image av neutral = "images/characters/amarok/Amarok_VampNeut.png"
image av happy = "images/characters/amarok/Amarok_VampHap.png"
image av angry = "images/characters/amarok/Amarok_VampAng.png"
image av sad = "images/characters/amarok/Amarok_VampSad.png"
image av scared = "images/characters/amarok/Amarok_VampScared.png"

#FullVamp
define amv = Character(" FullVamp-Amarok ")

image amv neutral = "images/characters/amarok/Amarok_SVampNeut.png"
image amv happy = "images/characters/amarok/Amarok_SVampHap.png"
image amv angry = "images/characters/amarok/Amarok_SVampAng.png"
image amv sad = "images/characters/amarok/Amarok_SVampSad.png"
image amv scared = "images/characters/amarok/Amarok_SVampScared.png"


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

    #Man
    show a neutral at character_cent
    a "Testing neutral."

    show a happy at character_right
    a "Testing happy."

    show a angry at character_left
    a "Testing angry."

    show a sad at character_cent
    a "Testing sad."

    show a scared at character_right
    a "Testing scared."

    hide a

    #Merperson
    show am neutral at character_left
    am "Testing neutral."

    show am happy at character_cent
    am "Testing happy."

    show am angry at character_right
    am "Testing angry."

    show am sad at character_left
    am "Testing sad."

    show am scared at character_cent
    am "Testing scared."

    hide am

    #FullMer
    show mer at character_right
    mer "Testing the final merperson form."

    hide mer

    #Vamp
    show av neutral at character_right
    av "Testing neutral."

    show av happy at character_left
    av "Testing happy."

    show av angry at character_cent
    av "Testing angry."

    show av sad at character_right
    av "Testing sad."

    show av scared at character_left
    av "Testing scared."

    hide av

    #FullVamp
    show amv neutral at character_cent
    amv "Testing neutral."

    show amv happy at character_left
    amv "Testing happy."

    show amv angry at character_right
    amv "Testing angry."

    show amv sad at character_cent
    amv "Testing sad."

    show amv scared at character_left
    amv "Testing scared."

    hide amv

    #Normy
    show s neutral at character_left
    s "Testing neutral."

    show s happy at character_right
    s "Testing happy."

    show s angry at character_cent
    s "Testing angry."

    show s sad at character_left
    s "Testing sad."

    show s scared at character_right
    s "Testing scared."

    hide s

    #MermanStage1
    show sm neutral at character_right
    sm "Testing neutral."

    show sm happy at character_cent
    sm "Testing happy."

    show sm angry at character_left
    sm "Testing angry."

    show sm sad at character_right
    sm "Testing sad."

    show sm scared at character_cent
    sm "Testing scared."

    hide sm

    #Vampire
    show sv neutral at character_cent
    sv "Testing neutral."

    show sv happy at character_right
    sv "Testing happy."

    show sv angry at character_left
    sv "Testing angry."

    show sv sad at character_cent
    sv "Testing sad."

    show sv scared at character_right
    sv "Testing scared."

    hide sv

    #MegaVamp
    show smv neutral at character_left
    smv "Testing neutral."

    show smv happy at character_cent
    smv "Testing happy."

    show smv angry at character_right
    smv "Testing angry."

    show smv sad at character_left
    smv "Testing sad."

    show smv scared at character_cent
    smv "Testing scared."

    hide smv

    return
