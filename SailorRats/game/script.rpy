# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(" Jeoseung Saja ")
define a = Character(" Amarok ")
define mc = Character ("  You  ")
define l = Character (" Lily ")
define m = Character (" Morrigan ")
define n = Character (None)
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

    scene black with fade
    pause 0.5
    show text "Home {p}September 19, 2026 {p}19:30" with dissolve
    pause 2.5
    hide text with dissolve

    scene black

    n "I shouldn't be scaredd."
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

    scene black with fade
    pause 0.5
    show text "Home {p}September 26, 2026 {p}18:00" with dissolve
    pause 2.5
    hide text with dissolve


    scene bednight

    n "I'm about to get into bed when my phone buzzes from my nightstand, the dating app's logo visible on the pop-up banner."
    n "I grab it to check the notification, realizing after that I may have moved a little {i}too{/i} quickly to check a dating app message sent at 3 o'clock in the morning."

    notif "You have a new message from [LIName]!"
    LoveInterest "I set my bag down for two seconds when I was leaving work and a trash panda stole my leftover mac (T.T)"

    mc "No, not the macaroni! But also it's 3am, are you super sad about the macaroni or just can't sleep?"

    LoveInterest "2 things can be true, I can be super sad about my macaroni while I'm also just leaving work lol"

    mc "At 3am!?!?"

    LoveInterest "Yeah, I work nights. It's kinda nice being up when everyone else is asleep... It makes work pretty easy but the trade off is that I spend all day sleeping and am basically nocturnal."

    mc "So what I'm hearing is our first date should be a romantic night out, so you can stay awake for it?"

    LoveInterest "I mean... i'm not upset at that idea ^_^"
    jump dateone_path


label dateone_path:

    scene black with fade
    pause 0.5
    show text "Blueberry Acres National Park {p}October 1, 2026 {p}21:00" with dissolve
    pause 2.5
    hide text with dissolve

    scene forest

    n "{nw=0.5}"

    n "Is meeting a stranger in a national park at night for a picnic the smartest idea I've ever had? Probably not."
    n "Even so, I'm excited to finally meet them."
    n "{cps=20}...{/cps}{w=1.5}Okay.... I'm about 90 percent sure that the butterflies in my stomach are excitement, and not anxiety over the prospect of possibly walking into my own murder."
    n "{cps=20}...{/cps}{w=1.5}... Make that 85 percent."
    n "I'm comforted by the fact that there are at least a handful of cars in the parking lot when I pull in. We won't be out here completely alone, which helps quiet down the catastrophizing part of my brain."
    n "I turn into the first parking spot I see and turn off the ignition."
    n "The person in the car next to me is still in their car, and it takes a second before [LIName] turns to face me too. They give a little wave, and I smile."

    show LI happy at character_cent 

    LoveInterest "Hey stranger."

    mc "Fancy meeting you here."

    n "They walk around the front of their car to meet me halfway."

    show LI neutral at character_cent

    LoveInterest "Okay, I know we talked about a picnic, but the radio was talking about a meteor shower that's supposed to be visible tonight."
    
    LoveInterest "And there's apparently a perfect place to see it that's like a 15 minute walk to the top of a hill nearby..."

    n "[LIName] pauses and looks at me like they're trying to gauge my reaction."

    mc "I sense a {i}'but'{/i} coming on..."

    pause 0.5

    show LI happy at character_cent

    n "[LIName] smiles, clapping their hands together in front of them."

    LoveInterest "There's also supposed to be this gorgeous lake nearby, but it's not as easy to see the sky."

    n "They turn their eyes towards my car, where a cooler bag filled with sandwiches and cut up fruit is sitting on the passenger's seat."
    
    n "Their smile fades a little bit, their eyes widening as if they're afraid I'll be offended."

    show LI scared at character_cent

    LoveInterest "But I know you specifically asked me out here for a picnic so I don't want to ruin any plans you had, so if you had a specific place in mind, I'm cool with anything."

    menu:
        mc "Honestly, they all sound amazing. What I really think I want to do is..."

        # "Have our picnic in the clearing.":
        #     jump wolf_path

        # "Watch the meteor shower.":
        #     jump vamp_path

        "See the lake, how romantic!":
            jump mer_path


# label wolf_path:

#     jump hospital_path

# label vamp_path:

#  jump hospital_path

label mer_path:
    n "[LIName] pulls up the exact directions to the lake on their phone, and we fall into step beside each other as we walk. The lights from the parking lot are drifting farther behind us, allowing the few stars we {i}can{/i} see from beneath the canopy of leaves to shine even brighter."

    LoveInterest  "We might be able to still see the meteor shower after all."
    
    n "I gesture to the cooler bag on my shoulder."

    mc "And we still get our picnic, too."

    n "[LIName] smiles, and releases a dry huff of amusement."

    show LI happy at character_cent 

    LoveInterest "We get to have our picnic and eat it too."

    n "They're looking at me expectantly, so I smile and nod."

    show LI scared at character_cent

    n "[LIName] looks at the ground suddenly."

    LoveInterest "Like cake? You can have your cake and eat it - actually, ignore that."

    n "This time, my laugh is genuine."

    mc "No, it's cute! It just took me a minute."

    show LI neutral at character_cent

    n "They smile, their eyes finding mine when their head turns back towards me just the slightest bit."

    show LI happy at character_cent

    n "When they see my smile, their face turns back fully towards me, flashing me a big, mischevious grin."

    LoveInterest "Okay thank God, I was worried I'd already blown my cover as an incredibly cool, interesting individual."

    n "I shrug my shoulders."

    mc "If we're being honest, cool was up for debate anyway."

    show LI neutral at character_cent

    mc "But interesting? We're walking to a lake in the forest at night for a picnic. I think you're good on {i}interesting{/i}"

    show LI happy at character_cent

    LoveInterest "Interesting, or anxiety inducing?"

    mc "I mean, two things can be true at the same time. Like how if I end up a cautionary tale on some True Crime podcast somewhere, my story will be both interesting and axiety inducing."

    show LI scared at character_cent with hpunch

    n "My foot catches on a tree root on the path, and I stumble sideways, grabbing onto [LIName]'s arm for stability."

    n "Their other arm grabs onto me too, holding me up before I completely hit the ground."

    n "[LIName] helps me right myself and I can feel my cheeks heating up, but I try to play it cool."

    show LI happy at character_cent

    mc "Like I said, interesting {i}and{/i} anxiety inducing."

    pause 0.5

    hide LI

    scene lake

    n "It's quiet by the lake."

    n "No one else is around, and [LIName] places the blanket I brought on the grassy bank next to the lake's shore."

    show LI happy at character_cent

    LoveInterest "Okay so maybe the stars aren't exactly clear here, but still..."

    n "They're right; we have a pretty limited view of the sky, but it's not entirely obscured."
    n "Off in the distance I can hear the sounds of some sort of critter shuffling around in the brush, and there is the distinct smell of campfire in the air."
    n "But other than that, there aren't any other signs of people. Just me and [LIName] and the soft waves of the lake."
    n "I sit down next to [LIName] on the blanket, lean back on one hand with the other draped dramatically over my forehead and sigh."

    mc "However will we survive."

    show LI neutral at character_cent

    n "[LIName] closes their eyes and shakes their head."
    n "They take a deep, exaggerated breath in and hold it for a moment, before placing one hand on my shoulder."

    show LI sad at character_cent

    LoveInterest "It is a tragedy that has befallen us on this night, but we are strong. We shall prevail."

    n "Neither of us can hold our feigned sadness for very long, and we both crack up laughing."

    show LI happy at character_cent

    LoveInterest "But seriously, this is nice. I'm really glad we -"

    show LI scared at character_cent

    n "[LIName] stares at their own hand still holding onto my shoulder."
    n "For the smallest of seconds, their grip tightens before releasing completely, and they pull their hand back."

    show LI neutral at character_cent

    LoveInterest "I um... {w=2}I was just gonna say that I'm uh -"
    LoveInterest "{w=2} I'm really glad you agreed to meet up. I know this isn't exactly a conventional first date."

    mc "It's not, but I'm sure there have been weirder. Besides, technically it was my idea."

    show LI happy at character_cent
    LoveInterest "Okay true."
    
    n "[LIName] stares out at the water as I start rummaging through the picnic basket, setting plastic containers onto the blanket."

    show LI scared at character_cent
    LoveInterest "Wait, before we eat, can I make a suggestion that could potentially backfire horrifically on me?"

    show LI neutral at character_cent

    mc "Is this the part where you show me you've brought ropes and duct tape just in case the night goes well, and definitely not for anything sinister?"

    show LI happy at character_cent
    LoveInterest "First of all, those don't come out until {i}the end{/i} of the date, when I have a better idea of if they're needed for fun or to make sure my dirty secrets never get out."

    n "[LIName] winks at me, then stands up and offers me their hand."

    LoveInterest "Secondly, I was going to throw out the idea of .... should we say {i}taking advantage{/i} of being alone here?"

    show LI scared at character_cent

    LoveInterest "Wait, that sounded super sexual too."

    LoveInterest "Swimming. I meant swimming. We could go swimming. Not skinny dipping or anything."
    LoveInterest "And only if you want to. I mean, it sounds weird now that I've already said it and I feel kind of like an idiot or-"

    n "[LIName]'s eyes look frantic, like they're half expecting me to run away in horror at the verbal vomit and lack of a brain-to-mouth filter."
    n "I laugh, from both the adorable breakdown happening in front of me on on top of the wash of relief that I didn't make a complete fool of myself first."

    show LI neutral at character_cent
    n "I push myself to my feet, and grab their hand before they can twist their fingers apart from anxiety."    

    mc "What happened to waiting to see how the night goes before making any decisions? Don't say no for me, you never know."

    show LI scared at character_cent

    n "I lead them closer to the rocky shore, before slipping off my shoes and dropping my jacket on top."
    n "I'm standing in front of [LIName] in my underwear before they take the hint and start following my lead." 

    show LI happy at character_cent

    LoveInterest "We're actually doing this."

    n "I nod as they repeat the phrase to themselves quietly while they strip."

    mc "Okay {i}this{/i} was your idea, you can't be {i}that{/i} scaredd that I said yes, right?"

    show LI scared at character_cent

    LoveInterest "I'm gonna be honest, it was one of those moments where the bravery kicked in before the logical part of my brain could rethink it. I'm almost more scared I said it in the first place."

    show LI happy at character_cent

    LoveInterest "But I have always wanted to do this."

    n "I book it towards the water."

    mc "Then let's go!"

    hide LI

    n "It's freezing cold, so I plunge myself up to my shoulders the moment the water is deep enough."
    n "I can hear [LIName] splashing in close behind me, and they dive in fully to acclimate."

    show LI scared at character_cent
    LoveInterest "Oh my god it's so cold!"

    n "They swing their hair to get it out of their own eyes, sending the water droplets fling directly into mine."

    show LI happy at character_cent
    LoveInterest "Oops. Sorry!"

    mc "Yep, I'm sure you are."

    hide LI

    n "I splash water back at them, but they dodge it by diving past me, heading deeper into the lake."
    n "They surface a few feet behind me and splash me the moment I turn towards them."

    show LI happy at character_cent

    LoveInterest "You've gotta be faster than that. I won bronze in my seventh grade swimming championship."

    mc "Ooh, bronze. Not gold?"

    show LI sad at character_cent

    LoveInterest "No, but it was a super close race."

    n "I raise an eyebrow."

    show LI neutral at character_cent

    LoveInterest "Besides, the two people who beat me were brothers, and I'm pretty sure they were half fish anyway. No 12 year olds should be able to swim as fast as they did."

    mc "The only exception of course would have been you if you'd won instead?"

    show LI happy at character_cent

    LoveInterest "Exactly. You get it!"

    n "I tread my way towards [LIName], but they paddle backwards out of my reach."

    LoveInterest "See, great swimmer. I was made to be in the -"

    show LI scared at character_cent

    LoveInterest "Shit, something bit me!"

    n "I stop moving towards them instinctively."
    n "[LIName] reaches under the water and screams."

    LoveInterest "I think it's a leech!"

    mc "Don't rip it-"

    n "I can't speak fast enough and [LIName] pulls, hard."
    n "Their hand shoots out of the water, but the only evidence of the creature left is watery blood and slightly grey slime coating their palm."
    n "Tiny bits of what look like the same slime float to the surface of the water."
    n "My stomach turns at the sight."

    mc "Oh god, you popped it."

    n "[LIName] gags."

    LoveInterest "It still feels like it's biting me, we need to get out of here."

    hide LI

    n "There's no need for further argument. We both race back towards the shore."
    n "The moment [LIName] gets to their feet and their thigh is above the water, I can see the wound trickling thin rivulets of blood down their leg, swirling itself around globs of sticky leech goo still stuck to their skin around the bite mark."

    n "It's my turn to gag, and I'm suddenly very thankful we decided to go into the water {i}before{/i} we ate anything."
    
    n "[LIName] steps fully onto the rocky beach and holds their leg out to examine it."
    n "The sounds that are coming out of them as they poke and prod at the skin around the bite sounds halfway between a dry heave and a cat in heat."
    n "I run to the pile of my clothes and grab my shirt."

    show LI scared at character_cent
    
    mc "Stop touching it. Hold this on it to help stop the bleeding."

    n "[LIName] takes the shirt and holds it over their thigh, pressing it into the skin."
    n "I lead them back to the blanket, helping them cross the small bank between it and the beach. As they go to sit, I run back and grab our clothes, frantically checking my own skin for any unwelcome blood bags of my own."
    n "Thankfully I seem to be clear."

    n "When I drop our belongings next to [LIName], they've peeled back the shirt just a little bit to examine the wound more closely."
    
    show LI sad at character_cent

    n "If nothing else, they've stopped yowling."

    LoveInterest "This is so gross."

    n "I kneel next to them, leaning over slightly to make sure they also have no other extra new friends."

    mc "It is, but at least it's gone."

    show LI neutral at character_cent

    n "I take the shirt from them and bat their hands out of the way."

    mc "Let me see, I'm pretty sure you're not supposed to just rip them off like that."

    show LI sad at character_cent

    LoveInterest "Technically I exploded it off of me."

    mc "I'm fairly certain that's not better."

    hide LI

    n "I move the shirt out of my way and take a better look at the damage."
    n "There's a small but noticable chunk of skin missing from [LIName]'s thigh, and the skin around it looks jagged, almost as if it had been ripped open."
    n "Which, to be fair, I suppose it was."
    n "It also looks like it's not planning on clotting any time soon, and I have to keep dabbing around it with the shirt to be able to actually look at it."

    show LI scared at character_cent

    LoveInterest "What's my prognosis, doc? Please tell me it didn't like, leave a piece of it's head in my leg or something."

    n "I don't know much about leeches, but I'm pretty sure that's a thing tics can do, so it wouldn't surprise me."
    n "Especially with such an.... {w=2}unexpected ending to it's meal."
    n "I'm definitely not going to say that bit out loud though."

    mc "I think we need to get you checked out. At least so they can get it cleaned up, maybe see if it needs a stitch or something. It's not exactly a clean cut."

    show LI sad at character_cent

    n "I gesture for them to take my shirt and keep pressure on it."
    n "[LIName]'s hand closes over mine for a second, and I look up at them."
    n "They're just staring at my hand under theirs, and my bloody tee underneath them both."

    LoveInterest "This was not the way this night was supposed to end."

    n "I reach over and grab their clothes, handing them their own shirt."
    n "Realizing mine is otherwise occupied, I pull on my jacket and zip it up."

    mc "Maybe we just stick to the rope and duct tape next time."
        # jump hospital_path

#label hospital_path:



return
