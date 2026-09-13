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

    # This ends the game.

    return
