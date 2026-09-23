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

    n "I shouldn't be surprised."
    n "I'd meant to message back sooner, but work has been busy and life happened..."
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
            n "Sending the first message is the hardest part, so I keep it simple. A little basic, sure, and yet, somehow, still effective."
            jump generic_path

# COMMENTED OUT UNTIL DIALOGUE FINISHED FOR THESE PATHS =)
        # "If I could rearrange my keyboard, I'd put u and i .... oh wait.":
        #     jump cheesy_path

        # "Hey! What three items would someone need to have to successfully cast a summoning spell for you?":
        #     jump question_path

label generic_path:
    mc "Hey."

    LoveInterest "Hey, how's it going?"

    mc "Not too shabby, you?"

    LoveInterest "It's going okay. I picked up a coworkers shift so I'm working a double tonight which sucks tho"

    mc "Damn, that sucks. More money though at least?"

    LoveInterest "Thankfully. The only thing getting me thru is thinking of how I might be able to treat myself to a brand name mac and cheese box next week."

    mc "Mmmmm .... delicious brand name cardboard pasta."

    LoveInterest "See, you get it! i only have the best after a hard days work XD"
    jump genericsecondchat_path

# COMMENTED OUT UNTIL DIALOGUE FINISHED FOR THESE ROUTES! =)
# label cheesy_path:
#     notif "{cps=30} ... {i}[LIName] is typing{/i} ... {/cps}"
#     LoveInterest "Are they already together? I didn't even notice, I was too busy getting lost in your eyes ;)"

#     jump secondchat_path

# label question_path:
#     notif "{cps=30} ... {i}[LIName] is typing{/i} ... {/cps}"
#     LoveInterest "Ooh, that's a good one :D I'm gonna say a flat white, a good book, and a cozy spot in front of a fire."
#     jump secondchat_path
    
label genericsecondchat_path:
    n "I'm about to get into bed when my phone buzzes from my nightstand, the dating app's logo visible on the pop-up banner."
    n "I grab it to check the notification, realizing after that I may have moved a little {i}too{/i} quickly to check a dating app message sent at 3 o'clock in the morning."

    notif "You have a new message from [LIName]!"
    LoveInterest "I set my bag down for two seconds when I was leaving work and a trash panda stole my leftover mac (T.T)"

    mc "No, not the macaroni! But also it's 3am, are you super sad about the macaroni or just can't sleep?"

    LoveInterest "2 things can be true, I can be super sad about my macaroni while I'm also just leaving work lol"

    mc "At 3am!?!?"

    LoveInterest "Yeah, I do security overnight for a bougie hotel downtown. I mostly just sit and watch movies, occasionally check some cameras. Usually pretty easy but the trade off is that I spend all day sleeping and am basically nocturnal"

    mc "So what I'm hearing is our first date should be a romantic night out, so you can stay awake for it?"

    LoveInterest "I mean... i'm not upset at that idea ^_^"
    jump dateone_path


label dateone_path:
    n "Is meeting a stranger in a national park at night for a picnic the smartest idea I've ever had? Probably not."
    n "Even so, I'm excited to finally meet them."
    n "{cps=20}...{/cps}{w=1.5}Okay.... I'm about 90 percent sure that the butterflies in my stomach are excitement, and not anxiety over the prospect of possibly walking into my own murder."
    n "{cps=20}...{/cps}{w=1.5}Okay... 85 percent."
    n "I'm comforted by the fact that there are at least a handful of cars in the parking lot when I pull in. We won't be out here completely alone, which helps quiet down the true crime-addict part of my brain."
    n "I turn into the first parking spot I see and turn off the ignition."
    n "The person in the car next to me is still in their car too, and it takes a second before [LIName] turns to face me too. They give a little wave, and I smile."

    LoveInterest "Hey stranger."

    mc "Fancy meeting you here."

    n "They walk around the front of their car to meet me halfway."

    LoveInterest "Okay, I know we talked about a picnic, but the radio was talking about a meteor shower that's supposed to be visible tonight, and there's apparently a perfect place to see it that's like a 15 minute walk to the top of a hill nearby..."

    n "[LIName] pauses and looks at me like they're trying to guage my reaction."

    mc "I sense a 'but' coming on..."

    n "[LIName] smiles, clapping their hands together in front of them."

    LoveInterest "But also there's supposed to be this gorgeous lake nearby but it's not as easy to see the sky."

    n "They turn their eyes towards my car, where a cooler bag filled with sandwiches and cut up fruit is sitting on the passenger's seat. Their smile fades a little bit, their eyes widening as if they're afraid I'll be offended."

    LoveInterest "But I know you specifically asked me out here for a picnic so I don't want to ruin any plans you had, so if you had a specific place in mind, I'm cool with anything."

    menu:
        "Stargazing does sound fun...":
            jump vamp_path

        "I kinda had my heart set on the forest. I've heard it's magical in there.":
            jump wolf_path

        "I said our first date should be a romantic night out, right? What's more romantic than a lake under the stars?":
            jump mer_path

    label vamp_path

    label wolf_path

    label mer_path

    return
