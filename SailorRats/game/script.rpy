# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(" Jeoseung Saja ")
define a = Character(" Amarok ")
define mc = Character ("  You  ")
define l = Character (" Lily ")
define m = Character (" Morrigan ")
define n = Character (None, what_italic=True)
define notif = Character (" Notifications ",what_color="#FFA500" )

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

    n "I shouldn't have been surprised."
    n "I'd meant to message back sooner, but work was busy and life happened..."
    n "... Now it's been over a week since I responded to my last message on the dating app I'd joined, and my inbox is full of half finished conversations with empty profiles from people who've unmatched me."
    n "I know it's my own fault, but the disappointment still stings. {p}But I suppose I'm here now. Might as well give this another shot."

    n "{cps=20}... {p}... {/cps}"
    n "{cps=20}... {p}... {/cps}"

    n "Before long I'm completely zoned out, swiping left without even really looking at the people on my phone."
    n "I let my head fall backwards and sigh, only a little too dramatically."
    
    mc "Just watch, somewhere in those rejected profiles was the love of my life."
    
    n "I'm about to just throw in the towel completely when my phone buzzes, and a small notification banner rolls down from the top of the screen."
    notif "Your {i}Daily Showcase{/i} Is Ready! View Your Top 4 Most Compatible Right Now!"

    mc "{w=1.5}I mean.... it can't hurt, right?"
    
    n "I tap the notification, and am instantly shown four people all smiling at me from the screen."

    call screen chooseAmarok


    return

label startDate1:
    show LI happy at character_cent
    notif "It's a match!"

    n "There's a moment of panic that happens with every new match."
    n "My stomach drops, and I feel a sudden overwhelming urge to chuck my phone across the room."
    n "I stare at [LIName]'s profile picture."
    
    mc "Okay, how am I going to win them over?"

    menu: 

        "Hey.":
            jump generic_path

        "If I could rearrange my keyboard, I'd put u and i .... oh wait.":
            jump cheesy_path

        "Hey! What three items would someone need to have to successfully cast a summoning spell for you?":
            jump question_path

label generic_path:
    LoveInterest "Hey. How's it going?"

label cheesy_path:
    LoveInterest "Are they already together? I didn't even notice, I was too busy getting lost in your eyes."

label question_path:
    LoveInterest "Ooh, that's a good one. I'm gonna say a flat white, a good book, and a cozy spot in front of a fire."
    return
