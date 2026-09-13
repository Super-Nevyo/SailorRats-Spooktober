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
image sm neutral = "images/characters/saja/SajaMerNeut.png"
image sm happy = "images/characters/saja/SajaMerHap.png"
image sm angry = "images/characters/saja/SajaMerAngry.png"
image sm sad = "images/characters/saja/SajaMerSad.png"
image sm scared = "images/characters/saja/SajaMerScared.png"

#Vampire
image sv neutral = "images/characters/saja/SajaVampNeut.png"
image sv happy = "images/characters/saja/SajaVampHap.png"
image sv angry = "images/characters/saja/SajaVampAngry.png"
image sv sad = "images/characters/saja/SajaVampSad.png"
image sv scared = "images/characters/saja/SajaVampScared.png"

#MegaVamp
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

    show a neutral at character_cent
    a "Testing neutral expression on this one - I guess i shoud try and test all of them?"

    show a happy at character_left
    a "Testing that this in fact places the character to the left"

    show a angry at character_left
    a "Imma so angy uwu >:c"

    show a sad at character_right
    a "Dont cry uwu :c"

    show a scared at character_cent
    a "A?AAAAAAAHHssssggGGGGHHH!!"


    hide a

    show am neutral at character_cent
    am "Testing neutral expression on this one - I guess i shoud try and test all of them?"

    show am happy at character_left
    am "Testing that this in fact places the character to the left"

    show am angry at character_left
    am "Imma so angy uwu >:c"

    show am sad at character_right
    am "Dont cry uwu :c"

    show am scared at character_cent
    am "A?AAAAAAAHHssssggGGGGHHH!!"


    hide am

    show mer at character_cent
    mer "A?AAAAAAAHHssssggGGGGHHH!!"

    hide mer

    show s neutral at character_cent
    a "Testing neutral expression on this one - I guess i shoud try and test all of them?"

    show s happy at character_left
    a "Testing that this in fact places the character to the left"

    show s angry at character_left
    a "Imma so angy uwu >:c"

    show s sad at character_right
    a "Dont cry uwu :c"

    show s scared at character_cent
    a "A?AAAAAAAHHssssggGGGGHHH!!"


    hide s

    show sm neutral at character_cent
    am "Testing neutral expression on this one - I guess i shoud try and test all of them?"

    show sm happy at character_left
    am "Testing that this in fact places the character to the left"

    show sm angry at character_left
    am "Imma so angy uwu >:c"

    show sm sad at character_right
    am "Dont cry uwu :c"

    show sm scared at character_cent
    am "A?AAAAAAAHHssssggGGGGHHH!!"

    hide sm

    show sv neutral at character_cent
    am "Testing neutral expression on this one - I guess i shoud try and test all of them?"

    show sv happy at character_left
    am "Testing that this in fact places the character to the left"

    show sv angry at character_left
    am "Imma so angy uwu >:c"

    show sv sad at character_right
    am "Dont cry uwu :c"

    show sv scared at character_cent
    am "A?AAAAAAAHHssssggGGGGHHH!!"


    hide sv

    show smv neutral at character_cent
    am "Testing neutral expression on this one - I guess i shoud try and test all of them?"

    show smv happy at character_left
    am "Testing that this in fact places the character to the left"

    show smv angry at character_left
    am "Imma so angy uwu >:c"

    show smv sad at character_right
    am "Dont cry uwu :c"

    show smv scared at character_cent
    am "A?AAAAAAAHHssssggGGGGHHH!!"

    # This ends the game.

    return
