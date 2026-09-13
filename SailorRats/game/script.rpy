# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character(" KoreanGuy Name Here ")

define a = Character(" Amarok ")
image a neutral = "images/characters/amarok/Amarok_Neutral.png"
image a happy = "images/characters/amarok/Amarok_Happy.png"
image a angry = "images/characters/amarok/Amarok_Angry.png"
image a sad = "images/characters/amarok/Amarok_Sad.png"
image a scared = "images/characters/amarok/Amarok_Scared.png"

define am = Character(" Merm-Amarok? ")
image am neutral = "images/characters/amarok/Amarok_S1_Neutral.png"
image am happy = "images/characters/amarok/Amarok_S1_Happy.png"
image am angry = "images/characters/amarok/Amarok_S1_Angry.png"
image am sad = "images/characters/amarok/Amarok_S1_Sad.png"
image am scared = "images/characters/amarok/Amarok_S1_Scared.png"

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

    # This ends the game.

    return
