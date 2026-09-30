# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(" Saja ")
define a = Character(" Amarok ")
define mc = Character (" You ")
define l = Character (" Lily ")
define m = Character (" Morrigan ")
define n = Character (None)
define notif = Character (" Notification ", what_size=55, what_color="#FFA500")
define p = Character ("Father Camden")

default LIName = "Character"
default LIFolder = "character"
default LIStage = "normal"
default route = "none"
default mcturned = False
default talkpathopen = True

define li = Character("[LIName]")

image LI neutral = "images/characters/[LIFolder]/[LIStage]/neutral.png"
image LI happy = "images/characters/[LIFolder]/[LIStage]/happy.png"
image LI angry = "images/characters/[LIFolder]/[LIStage]/angry.png"
image LI sad = "images/characters/[LIFolder]/[LIStage]/sad.png"
image LI scared = "images/characters/[LIFolder]/[LIStage]/scared.png"
image LI blush = "images/characters/[LIFolder]/[LIStage]/blush.png"

image priest neutral = "images/characters/priest/neutral.png"
image priest angry = "images/characters/priest/angry.png"
image priest furious = "images/characters/priest/very-angry.png"


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

transform background_fill:
    size (config.screen_width, config.screen_height)
    fit "cover"
    xalign 0.5
    yalign 0.5

label start:

    play music haunted_bg fadein 2.0
    scene frame with fade
    pause 0.5 
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}October 22, 2026{/size}\n{size=32}18:30{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene bednight at background_fill with dissolve


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
    play sound sfx_notification
    
    notif "Your {i}Daily Showcase{/i} Is Ready! View Your Top 4 Most Compatible Right Now!"

    mc "{w=1.5}I mean.... it can't hurt, right?"
    
    n "I tap the notification, and am instantly shown four people all smiling at me from the screen."

    call screen chooseAmarok


    return

label startDate1:

    
    show LI happy at character_cent
    play sound sfx_match
    notif "It's a match!"

    n "There's a moment of panic that happens with every new match."
    n "My stomach drops, and I feel a sudden overwhelming urge to chuck my phone across the room."
    n "I stare at [LIName]'s profile picture."
    
    mc "Okay, how am I going to win them over?"

    menu: 

        "Heeey!":
            n "Sending the first message is the hardest part, so I keep it simple. A little basic, sure, and yet, somehow, still effective."
            jump generic_path


        "Do you actually play all those games or just collect them?":
            jump gamer_path

        "SUPER important question, before anything: If you were a dragon, what would you hoard?":
            jump dragon_path


label generic_path:

    window hide
    scene expression ("images/phone/texts/%s.png" % LIFolder)
    
    $ Msgs = [ ["", "Hey"],
    ["Hey, how's it going?",""],
    ["","Not too shabby, you?"],
    ["It's going okay.",""],
    ["I picked up a coworkers shift",""],
    ["so I'm working a double tonight which sucks tho",""],
    ["","Damn, that sucks. More money though at least"],
    ["Thankfully!",""],
    ["The only thing getting me thru is thinking",""],
    ["of how I might be able to treat myself to a brand name mac and cheese box next week",""],
    ["","Mmmmm .... delicious brand name cardboard pasta"],
    ["See, you get it! i only have the best after a hard days work XD",""]
    
    ]
    $ counter = -1
    $ end = len(Msgs) -4
    $ jumpto = "genericsecondchat_path"

    jump textConversation

    

label gamer_path:

    window hide
    scene expression ("images/phone/texts/%s.png" % LIFolder)

    $ Msgs = [["","So... are you ACTUALLY gonna play those games or is it just to have them? xd"],
    ["wow, attacking me already TwT",""],
    ["please tell me your library is worse",""],
    ["","I mean... everyone has a bunch of games in their library,"],
    ["","but..."]

    ]

    $ counter = -1
    $ end = len(Msgs) -4
    $jumpto = "gamer_choice"

    jump textConversation


label gamer_choice:

    window auto

    menu:
        "Of course I play everything I get!":
            li "haha at least one of us has their life together xd."

        "We are not discussing my library!! xdd":
            li "THAT bad huh? haha xd"
    
    window hide

    $ Msgs = [["Anyway, what are you up to today?",""],
    ["","Not much, I'm trying to pick something to play!! I'm between Silksong and Blue Prince... \n I think its gonna be Blue Prince"],
    ["oh nice! that's an awesome game",""],
    ["Should I leave you to it? :D",""],
    ["","What? Of course not! It's a puzzle game haha you gotta help me!"],
    ["maybe we could play it together sometime! I dont want to distract you now haha",""],
    ["","But... you are a good distraction uwu"],
    ["haha you are cute uwu \n we should definitely do that! \n What else do you do for fun? ",""]
    ]

    $ counter = -1
    $ end = len(Msgs) -4
    $jumpto = "gamer_hobbies"

    jump textConversation
    

label gamer_hobbies:

    window auto

    menu:
        "Play ALL the games!":
            mc "I mean... games mostly, but I sometimes like to go out on walks and see what's around."
            li "haha I guess we can enable each other's purchases haha"
            li "I usually work nights but on my days off I like going for a night walk! (big time sleeping all day lol)"

        "I love horror movies!":
            mc "omg I love movies! Mostly spooky but I can never pick one lol"
            mc "but I like spooky stuff"
            li "horror movies are awesome! I need snacks tho or its not really complete"
            li "I work nights but on my days off i go for night walks! is that spooky enough? haha"

        "I'm more outdoorsy!":
            mc "I love hiking and sightseeing too! This is why I dont have time for games TwT"
            li "oh that's fun!! i work nights but on my days off I go for night walks! the night sky is really beautiful by the mountains"

    window hide

    $ Msgs = [ ["","oh yeah? that sounds like fun actually!"],
    ["","I think we will get along pretty well haha"],
    ["yeah i think so too...",""],
    ["we should hangout some time soon!! uwu",""],
    ["","I would really like that uwu - okay! I gotta go now, I've got work in the morning, but chat later?"],
    ["Absolutely! Night!",""]

    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "gamersecondchat_path"

    jump textConversation

#####

label dragon_path:

    window hide
    scene expression ("images/phone/texts/%s.png" % LIFolder)

    $ Msgs = [["","Your answer could maybe save the world"],
    ["wow, no hello?",""],
    ["no how's it going? xd",""],
    ["Straight right to assesing my dragonsona??? who hurt you...",""],
    ["","Hahaha, this is CRUCIAL information!! :3"],
    ["Okay, okay give me a second...",""],
    ["Oof! maybe dice! an insane amount of dice",""],
    ["Shiny ones, weird liquid filled ones, there's even ones that have candy inside!",""],
    ["What about you? What would you hoard?",""]
    ]

    $ counter = -1
    $ end = len(Msgs) -4
    $jumpto = "dragon_choice"

    jump textConversation


label dragon_choice:

    window auto

    menu:
        "GAMES AND GAME STUFF! Like the master sword or a minecraft lamp...":
            mc "And of course, all the games that come with loving things like that lmao"
            mc "I want my whole apartment full of game vibes <3"
            li "Oh damn, that actually sounds amazing! I'd love to have the new OoT collector's edition T.T"

        "Tiny thingys I find emotionally significant for no reason at all :3":
            mc "I really love collecting things like records, comics, statues... sometimes shoes xd"
            li "Aww that is actually adorable :3"
            li "Kinda like a crow-dragon haha xd"
        
        "What else!? Gold of course!":
            mc "Why complicate perfection? Dragons already like it for a reason xd"
            mc "Think about my investments and shared portfolio!! haha"
            li "I suppose with the way things are, having a safe investment is the best way to dragon XD"
    
    window hide

    $ Msgs = [["Okay but if we're talking dragons now I have to ask...",""],
    ["Do you play DnD?",""],
    ["","A little, but I prefer other kinds of TTRPGs!"],
    ["","I think Vampire The Mascarade is really cool!"],
    ["","But character creation is my nemesis, lmao xd I take forever..."],
    ["REAL!! Who would have thought that would be the final boss haha",""],
    ["this is also why I can't play Baldur's Gate!!",""],
    ["I go and create a new character, take forever doing that and then",""],
    ["play the game for like an hour before creating another xD",""],
    ["","Hahaha oh if only we didn't have free will xDD"],
    ["What about you? Do you actually play after making the character?",""]

    ]

    $ counter = -1
    $ end = len(Msgs) -4
    $jumpto = "dragon_char"

    jump textConversation
    

label dragon_char:

    window auto

    menu:
        "I don't ever play the games, I just create characters!":
            mc "Sims, BG3, Monster Hunter... I live in the character creator mode haha"
            li "ikr!!?? Cyberpunk too has a very cool one!!"
            li "sad they decided to make it ONLY a FPS hahah"

        "I like having different stories and just a few characters":
            mc "I like to see the different parts of what the game can be..."
            mc "but I do spend more time in the game but with different characters"
            li "That's fair! Baldur's Gate is huge so I totally get it"

        "I can just do one character and play the game forever":
            mc "And I guess once I have over 400 hrs I don't wanna create a new one haha"
            li "yeah no that's totally fair xd"

    window hide

    $ Msgs = [
    
    ["so what are you actually playing right now?",""],
    ["","I'm trying to choose what to start next... a puzzle game maybe?"],
    ["oooohhh... do you like chill puzzles? Or like wrecking brain puzzles? xd",""],
    ["","Mmmm... I'm gonna say the second!"],
    ["","But I'm insanely bad at them, ngl xd I need so much help and hints haha"],
    ["Nothing like a game insulting you for hours to feel alive haha",""],
    ["Puzzles are generally better with someone else anyway!",""],
    ["","So are you saying you are gonna help me? owo"],
    ["Totally! Maybe we can play together sometime c:",""],
    ["I have to get ready for work now tho... talk later?",""],
    ["","Absolutely! Good luck at work :3"]

    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "gamersecondchat_path"

    jump textConversation


########
    
label genericsecondchat_path:

    window auto

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}October 26, 2026{/size}\n{size=32}03:00{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve


    scene bednight at background_fill with dissolve

    n "I'm about to get into bed when my phone buzzes from my nightstand, the dating app's logo visible on the pop-up banner."
    
    play sound sfx_phone_vibrate

    n "I grab it to check the notification, realizing after that I may have moved a little {i}too{/i} quickly to check a dating app message sent at 3 o'clock in the morning."

    notif "You have a new message from [LIName]!"

    window hide
    scene expression ("images/phone/texts/%s.png" % LIFolder)

    $ Msgs = [
    ["I set my bag down for two seconds when I was leaving work and a trash panda stole my leftover mac (T.T)",""],
    ["","No, not the macaroni! But also it's 3am, are you super sad about the macaroni or just can't sleep?"],
    ["2 things can be true, I can be super sad about my macaroni while I'm also just leaving work lol",""],
    ["","At 3am!?!?"],
    ["Yeah, I work nights. It's kinda nice being up when everyone else is asleep...",""],
    ["It makes work pretty smooth, for sure",""],
    ["but the trade off is that I spend all day sleeping and am basically nocturnal xd",""],
    ["","So what I'm hearing is our first date should be a romantic night out, so you can stay awake for it?"],
    ["That would actually be awesome if that's cool with you ^_^",""],
    ["","Of course! That would be super fun!"]
    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "dateone_path"

    jump textConversation


label gamersecondchat_path:

    window auto

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}October 26, 2026{/size}\n{size=32}03:00{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve


    scene bednight at background_fill with dissolve

    n "I'm about to get into bed when my phone buzzes from my nightstand, the dating app's logo visible on the pop-up banner."

    play sound sfx_phone_vibrate

    n "I grab it to check the notification, realizing after that I may have moved a little {i}too{/i} quickly to check a dating app message sent at 3 o'clock in the morning."

    notif "You have a new message from [LIName]!"

    window hide

    scene expression ("images/phone/texts/%s.png" % LIFolder)

    $ Msgs = [
    ["hey hey heeeeyyyy! (:",""],
    ["how are you? Did you ended up playing?",""],
    ["","Of course I did! And then I got stuck..."],
    ["","This puzzle was taking me forever and then I blinked and it was 2am, like.....???"],
    ["oh no :c well, we should probably play it together soon!",""],
    ["actually, I'm off on the 31st owo",""],
    ["Should we plan something?",""],
    ["","You have Halloween off?!? Heck yeah!"],
    ["","It would probably be super spooky outside..."],
    ["","Would you be up for a night-halloweeny-hike? :D"],
    ["oh that's right, it actually is Halloween, isn't it? I take it you like it? Do you dress up?",""],
    ["That is an awesome idea, actually.",""],
    ["Do you like halloween that much? haha",""]
    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "gamer_second_halloween_choice"

    jump textConversation
    


label gamer_second_halloween_choice:

    window auto

    menu:
        "Are you kidding me? I love it! I'm always dressing up and planning next year's costume!":
            li "oh that's awesome! I love it too, i usually go to parties or music festivals :D"
        "I think I like it enough, but I prefer summer stuff more tbh!":
            li "haha its been a while since i've done things in the summer. imo winter is the best - unpopular opinion I know"
        "Meh, I guess it's okay, some people do go crazy about it tho":
            li "I know haha, but i'm a big believer in letting people like what they like idk Halloween can be fun!"

    window hide
    
    $ Msgs = [
    ["but back to our super spooky nighttime walk plans!",""],
    ["There's some nice spots around the area, but we can choose where to go when we get there?",""],
    ["and maybe snacks? It's a good idea now but it'll be even better with snacks. Maybe some popcorn!!",""],
    ["","YAASS snacks make everything better!!"],
    ["","I can bring something else too, make it a picnic!"]
    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "gamer_second_snacks_choice"

    jump textConversation

    

label gamer_second_snacks_choice:

    window auto

    menu:
        "Maybe some hot chocolate?":
            li "uh yeah, that'd be awesome!"
        "Something sweet? How do we feel about cookies?":
            li "!!!!"
            li "Cookies would go soooooo hard!!"
        "Or maybe you're just satisfied with being in my company? uwu":
            li "hahah yes, yes absolutely, oh queen of England XD"
            mc "hey now hahahaha =P"
    
    window hide

    $ Msgs = [
    ["amazing, I'm loving this plan already. can't wait to meet you",""],
    ["","Me neither, I'm excited!"],
    ["","Don't forget to bring a jacket too, it's cold out there!"],
    ["awww look at you taking care of me already <3",""],
    ["","heyyy!! :< "],
    ["","I can't have my date going hypothermic on me ... on a walk.... at night..."],
    ["","that's suspicious AF"],
    ["hahah fair",""],
    ["now go, I've distracted you from your game long enough. Go forth and get those achievements, soldier!",""]
    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "dateone_path"

    jump textConversation


label dateone_path:

    window auto

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Blueberry Acres National Park{/size}\n\n{size=40}October 31, 2026{/size}\n{size=32}21:00{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene forest at background_fill with dissolve
    play music music_first_date fadeout 1.5 fadein 2.0

    n "{nw=0.5}"

    n "Is meeting a stranger in a national park at night for a picnic the smartest idea I've ever had? Probably not."
    n "Even so, I'm excited to finally meet them."
    n "{cps=20}...{/cps}{w=1.5}Okay.... I'm about 90 percent sure that the butterflies in my stomach are excitement, and not anxiety over the prospect of possibly walking into my own murder."
    n "{cps=20}...{/cps}{w=1.5}... Make that 85 percent."
    n "I'm comforted by the fact that there are at least a handful of cars in the parking lot when I pull in. We won't be out here completely alone, which helps quiet down the catastrophizing part of my brain."
    n "I turn into the first parking spot I see and turn off the ignition."
    n "The person in the car next to me is still in their car, and it takes a second before [LIName] turns to face me too. They give a little wave, and I smile."

    show LI happy at character_cent 

    li "Hey stranger."

    mc "Fancy meeting you here."

    n "They walk around the front of their car to meet me halfway."

    show LI neutral at character_cent

    li "Okay, I know we talked about a picnic, but the radio was talking about a meteor shower that's supposed to be visible tonight."
    
    li "And there's apparently a perfect place to see it that's like a 15 minute walk to the top of a hill nearby..."

    n "[LIName] pauses and looks at me like they're trying to gauge my reaction."

    mc "I sense a {i}'but'{/i} coming on..."

    pause 0.5

    show LI happy at character_cent

    n "[LIName] smiles, clapping their hands together in front of them."

    li "There's also supposed to be this gorgeous lake nearby, but it's not as easy to see the sky."

    n "They turn their eyes towards my car, where a cooler bag filled with sandwiches and cut up fruit is sitting on the passenger's seat."
    
    n "Their smile fades a little bit, their eyes widening as if they're afraid I'll be offended."

    show LI scared at character_cent

    li "But I know you brought a bit of a picnic so I don't want to ruin any plans you had, so if you had a specific place in mind, I'm cool with anything."

    menu:
        mc "Honestly, they all sound amazing. What I really think I want to do is..."

        "Have our picnic in the clearing.":
            $ route = "wolf"
            jump wolf_path

        "Watch the meteor shower.":
            $ route = "vamp"
            jump vamp_path

        "See the lake, how romantic!":
            $ route = "mer"
            jump mer_path


label wolf_path:
    show LI happy at character_cent
    li "Honestly, real. And besides it's probably for the best anyway; a nice walk is good, but I don't want to get all sweaty from a long hike."

    mc "Me neither. And I also may have gone a bit overboard wtih the snacks... this thing is heavy!"

    n "As I lift the cooler up to gesture towards it, I stumble slightly on a rock in the path."

    play sound sfx_fall
    
    show LI scared at character_cent with hpunch

    n "[LIName]'s hand shoots out, catching my arm before I can fall."

    li "Careful!"

    mc "I can't believe I did that."

    n "[LIName]'s hand doesn't leave my arm. Instead it slides down to my hand, their fingers intertwining with mine. I stare at our joined hands for a second while I try to mentally push down the heat taking over my cheeks."

    show LI blush at character_cent

    li "Here, just in case."

    n "My brain is practically screaming at me to both acknowledge the situation and ignore it in what is mostly just a running chorus of {i}don't make it weird, don't make it weird, don't make it weird{/i}"

    mc "I'm going to make this weird."

    show LI scared at character_cent

    mc "OH MY GOD WAIT NO. THAT'S NOT WHAT I MEANT!"

    show LI blush at character_cent

    n "I cannot believe I just said that."

    li "I'm sorry, that was weird of me to just do without asking."

    n "They try to let go of my hand, but I hold on instead."

    mc "No, not at all! What I meant was that it's probably for the best that you do hold my hand. After all, I have the snacks, so if I go down, so do they."

    show LI happy at character_cent

    n "[LIName] laughs, their fingers closing around mine again."

    li "Very fair. This is in both of our best interest. For the snacks, of course."
    
    mc "Absolutely, for the snacks."

    hide LI

    n "We walk a bit more in silence."
    n "Our hands have started swinging between us, and every so often [LIName] looks down at them and smiles to themself."
    n "It's kind of adorable."
    n "The trees around us form a canopy overhead, but every once in a while I can see bits and pieces of the sky."
    n "As I watch, a particularly large bird soars overhead."

    mc "Man, being a bird would be so cool."

    show LI neutral at character_cent

    n "[LIName] looks up too."

    li "It really would be. The freedom to go anywhere? Yes, please."

    mc "Right? You could just take off and go anywhere you wanted to whenever you wanted to... I wish"

    show LI happy at character_cent

    li "So I'm guessing that your answer to 'What superpower would you have' is flight?"

    mc "Nah, there's so many cool ones to choose. If it had to be travel related, I'd rather just teleport to be honest."
    mc "But if my only option was flight? I'd specifically want to be a bird."

    show LI neutral at character_cent
    li "Why a bird?"

    mc "Because then you can poop on people."

    show LI happy at character_cent
    li "..."
    li "Real."

    mc "What about you, though?"

    show LI neutral at character_cent
    li "What about me?"

    mc "Your superpower."

    show LI blush at character_cent

    li "Mine would definitely be flight. As a human, though."

    mc "I shall poop on the other lame humans in your honour, then."

    show LI happy at character_cent
    li "I appreciate it."

    show LI neutral at character_cent
    li "But really though... being a pilot has always been the dream. I was even going to try to take lessons and learn, but they're so expensive and the timing was never right and.... I don't know, life just always seemed to get in the way."

    mc "I know what you mean. The way we live our lives these days... it makes it hard to do anything but grind to survive sometimes."
    mc "But you've still got time! We're young! A ton of super successful people don't find their success until they're older. We've got literal decades left to figure it out."

    show LI blush at character_cent

    li "True. I don't know, I think my inner child is still holding out hope for that dream."

    mc "And what about outer adult you?"

    show LI happy at character_cent

    li "They are too."

    mc "Well, then it's settled. I'm officially on Team [LIName] becomes a pilot. Even if you get there one baby step at a time, it's still a step!"

    show LI blush at character_cent

    li "True."

    show LI neutral at character_cent
    
    li "I guess I never thought of it like that. I've always been a more 'final big picture' type of person, I get lost in the details, especially when there's a lot of them."

    show LI happy at character_cent

    li "But I guess the only way to make the number of steps get smaller is to start taking them."

    n "I use our still-joined hands to pull their shoulder towards mine and bump them."

    mc "And I will gladly remind you of that any time you need me to."

    n "We come to a slightly overgrown part of the path, and [LIName] pushes the branches out of the way, revealing the clearing."

    window hide
    scene clearing at background_fill with dissolve
    pause 0.7
    window auto

    n "It's gorgeous, and completely private. I can hear people laughing way off in the distance, and a dog howls in response somewhere else equally far away."
    n "But aside from a few small critters moving around in the underbrush, it seems like we are completely alone."
    n "[LIName] sets down the blanket they brought, and I start unpacking containers of cookies, cut up fruits and veggies, a container of popcorn, some chocolates... "
    n "[LIName]'s face lights up."

    show LI happy at character_cent

    li "Hey, you brought it!"

    mc "I said I would, didn't I?"

    n "But looking at the spread I've set out, it seems I may have forgotten a few things."

    show LI neutral at character_cent

    mc "Okay, so I'm realizing now that in my excitement, I may have forgotten real food."

    li "That's okay. It's not a traditional picnic..."

    show LI happy at character_cent

    li "It's a snack-a-thon!"

    show LI blush at character_cent

    li "And honestly, that's even better in my opinion." 

    n "We sit down opposite one another and start digging in to our unconventional feast."
    n "My cooler bag didn't seem to get the memo that it was supposed to actually cool things, so unfortunately the chocolate I packed has melted a little bit."

    show LI neutral at character_cent
    
    li "Pfft, it just wanted to be chocolate dip for the fruit. It knew it had a higher purpose."

    n "[LIName] drags a bit of cantelope through the chocolate puddle before taking a bite."

    show LI happy at character_cent

    li "See? Perfection."

    n "Unfortunately, [LIName] was so caught up in their snack that they didn't notice the now chocolate sauce missing half of their mouth, instead smearing onto their lip and chin."

    mc "You've got a bit of -"
    n "I gesture to my own mouth."
    
    show LI neutral at character_cent
    
    li "Here?"

    n "They swipe a finger at their bottom lip and stare at their finger."

    show LI scared at character_cent

    li "Oh my god, that's so embarrasing."

    show LI blush at character_cent

    mc "It's fine, really! But there's definitely more."

    show LI happy at character_cent

    n "The look they give me is downright mischevious."

    li "I mean, if you're so bothered by it, you could come help me clean it up?"

    n "[LIName] leans forward and stares at me."
    n "I'm pretty sure my brain has forgotten how to move."

    mc "I mean, it {i}would{/i} be an absolute shame to waste it..."

    n "I move slowly towards them..."
    
    stop music fadeout 0.5
    play sound sfx_eerie

    n "but something crashes through the trees beside us, and I instinctively pull backwards as it lunges towards us."

    show LI scared at character_cent
    li "What the -"
    mc "Look out!"

    n "The small dog stops at the edge of our blanket, wide eyes staring directly at the food in between us."

    show LI happy at character_cent

    li "Awww, it's just a puppy!"
    li "You hungry little guy?"

    n "[LIName] picks up a carrot from the veggies and holds it out to the dog."
    n "I laugh, my heartbeat still racing in my chest, when I notice that the hand [LIName] is holding out just so happens to be the same one covered in chocolate."

    mc "Wait!"

    show LI scared at character_cent
    n "[LIName] pauses, lifting the food just out of the dog's reach."
    n "The dog growls, but doesn't move. It just keeps it's eyes locked on the carrot."
    
    play sound sfx_dog_growl

    li "What's wrong?"

    mc "Your hand is covered in chocolate. We don't want him to get sick!"

    show LI happy at character_cent

    n "[LIName] looks at their hand and smiles."

    li "You're so right. Hang on, little guy, we'll get you somethi-"

    show LI scared at character_cent with hpunch

    li "OWWW!!"

    n "As [LIName] pulls the carrot away to grab something else with their other hand, the dog pounces onto them, teeth closing around the carrot.... and their hand."
    
    play sound sfx_dog_bark

    n "I lean forward, but the dog is already bounding into the treeline before I even get a chance to pull it off of [LIName]."

    mc "Are you okay?"

    show LI angry at character_cent

    li "Fuck, that hurt!"
    
    n "[LIName] turns towards the trees where the dog disappeared."
    li "You little jerk, I was going to get you something that {i}wouldn't{/i} make you sick, not taking it away completely!"

    n "I look at their hand in their lap. Blood is collecting in their palm and mixing with the melted chocolate and probably a not-so-healthy dose of dog saliva."
    n "I dig into the cooler and grab a handful of napkins. I pull their hand closer and press a napkin on each side to get the initial bleeding out of the way so I can take a better look."

    show LI sad at character_cent
    n "I pull the napkins away and check the bite - it's small but fairly deep, and it looks like one of them pulled away before the dog's teeth were out of the wound, so it's torn a little bit to one side."

    show LI neutral at character_cent

    li "Damn, he got me good."
    
    show LI scared at character_cent

    li "Wait, did he have a collar? Was that a wild dog? Can chocolate in a dog bite cause an infection?"
    li "Am I going to get rabies?!"

    mc "Probably not that last one, but I think a bite from anything is enough to cause an infection, domesticated or not."

    show LI sad at character_cent
    
    mc "Besides, this is not exactly a clean bite, and it looks pretty deep. I think you might need stitches."

    show LI scared at character_cent
    
    li "Are you serious? I was just trying to be nice to the puppy and this is what I get in return..."

    mc "You're gonna be fine, I promise."

    show LI neutral at character_cent

    mc "But we should really go get you to a doctor to get this cleaned up and looked at. There isn't exactly a good place to get this clean out here."

    n "The napkins I've been using to dab the blood out of the way are getting pretty soaked, but I don't want to point that out. [LIName] is panicking enough as it is."
    n "I grab new ones and press them onto each side of [LIName]'s hand, folding their fingers over their palm to hold one and pulling their other hand onto the back of their hand to hold the other."

    mc "Here, just keep holding these here and apply pressure. I'll get our picnic cleaned up and then we can go, okay?"

    show LI sad at character_cent

    li "Okay. Thank you."

    $ memory_state = ""

    jump hospital_path


label mer_path:
    n "[LIName] pulls up the exact directions to the lake on their phone, and we fall into step beside each other as we walk. The lights from the parking lot are drifting farther behind us, allowing the few stars we {i}can{/i} see from beneath the canopy of leaves to shine even brighter."

    li  "We might be able to still see the meteor shower after all."
    
    n "I gesture to the cooler bag on my shoulder."

    mc "And we still get our picnic, too."

    n "[LIName] smiles, and releases a dry huff of amusement."

    show LI happy at character_cent 

    li "We get to have our picnic and eat it too."

    n "They're looking at me expectantly, so I smile and nod."

    show LI scared at character_cent

    n "[LIName] looks at the ground suddenly."

    li "Like cake? You can have your cake and eat it - actually, ignore that."

    n "This time, my laugh is genuine."

    mc "No, it's cute! It just took me a minute."

    show LI neutral at character_cent

    n "They smile, their eyes finding mine when their head turns back towards me just the slightest bit."

    show LI happy at character_cent

    n "When they see my smile, their face turns back fully towards me, flashing me a big, mischevious grin."

    li "Okay thank God, I was worried I'd already blown my cover as an incredibly cool, interesting individual."

    n "I shrug my shoulders."

    mc "If we're being honest, cool was up for debate anyway."

    show LI neutral at character_cent

    mc "But interesting? We're walking to a lake in the forest at night for a picnic. I think you're good on {i}interesting{/i}"

    show LI happy at character_cent

    li "Interesting, or anxiety inducing?"

    mc "I mean, two things can be true at the same time. Like how if I end up a cautionary tale on some True Crime podcast somewhere, my story will be both interesting and axiety inducing."

    show LI scared at character_cent with hpunch

    n "My foot catches on a tree root on the path, and I stumble sideways, grabbing onto [LIName]'s arm for stability."
    
    play sound sfx_fall

    n "Their other arm grabs onto me too, holding me up before I completely hit the ground."

    n "[LIName] helps me right myself and I can feel my cheeks heating up, but I try to play it cool."

    show LI happy at character_cent

    mc "Like I said, interesting {i}and{/i} anxiety inducing."

    pause 0.5

    
    window hide
    scene lake at background_fill with dissolve
    pause 0.7
    window auto

    n "It's quiet by the lake."

    n "No one else is around, and [LIName] places the blanket I brought on the grassy bank next to the lake's shore."

    show LI happy at character_cent

    li "Okay so maybe the stars aren't exactly clear here, but still..."

    n "They're right; we have a pretty limited view of the sky, but it's not entirely obscured."
    n "Off in the distance I can hear the sounds of some sort of critter shuffling around in the brush, and there is the distinct smell of campfire in the air."
    n "But other than that, there aren't any other signs of people. Just me and [LIName] and the soft waves of the lake."
    n "I sit down next to [LIName] on the blanket, lean back on one hand with the other draped dramatically over my forehead and sigh."

    mc "However will we survive."

    show LI neutral at character_cent

    n "[LIName] closes their eyes and shakes their head."
    n "They take a deep, exaggerated breath in and hold it for a moment, before placing one hand on my shoulder."

    show LI sad at character_cent

    li "It is a tragedy that has befallen us on this night, but we are strong. We shall prevail."

    n "Neither of us can hold our feigned sadness for very long, and we both crack up laughing."

    show LI happy at character_cent

    li "But seriously, this is nice. I'm really glad we -"

    show LI scared at character_cent

    n "[LIName] stares at their own hand still holding onto my shoulder."
    n "For the smallest of seconds, their grip tightens before releasing completely, and they pull their hand back."

    show LI neutral at character_cent

    li "I um... {w=2}I was just gonna say that I'm uh -"
    li "{w=2} I'm really glad you agreed to meet up. I know this isn't exactly a conventional first date."

    mc "It's not, but I'm sure there have been weirder. Besides, technically it was my idea."

    show LI happy at character_cent
    li "Okay true."
    
    n "[LIName] stares out at the water as I start rummaging through the picnic basket, setting plastic containers onto the blanket."

    show LI scared at character_cent
    li "Wait, before we eat, can I make a suggestion that could potentially backfire horrifically on me?"

    show LI neutral at character_cent

    mc "Is this the part where you show me you've brought ropes and duct tape just in case the night goes well, and definitely not for anything sinister?"

    show LI happy at character_cent
    li "First of all, those don't come out until {i}the end{/i} of the date, when I have a better idea of if they're needed for fun or to make sure my dirty secrets never get out."

    n "[LIName] winks at me, then stands up and offers me their hand."

    li "Secondly, I was going to throw out the idea of .... should we say {i}taking advantage{/i} of being alone here?"

    show LI scared at character_cent

    li "Wait, that sounded super sexual too."

    li "Swimming. I meant swimming. We could go swimming. Not skinny dipping or anything."
    li "And only if you want to. I mean, it sounds weird now that I've already said it and I feel kind of like an idiot or-"

    n "[LIName]'s eyes look frantic, like they're half expecting me to run away in horror at the verbal vomit and lack of a brain-to-mouth filter."
    n "I laugh, from both the adorable breakdown happening in front of me on on top of the wash of relief that I didn't make a complete fool of myself first."

    show LI neutral at character_cent
    n "I push myself to my feet, and grab their hand before they can twist their fingers apart from anxiety."    

    mc "What happened to waiting to see how the night goes before making any decisions? Don't say no for me, you never know."

    show LI scared at character_cent

    n "I lead them closer to the rocky shore, before slipping off my shoes and dropping my jacket on top."
    n "I'm standing in front of [LIName] in my underwear before they take the hint and start following my lead." 

    show LI happy at character_cent

    li "We're actually doing this."

    n "I nod as they repeat the phrase to themselves quietly while they strip."

    mc "Okay {i}this{/i} was your idea, you can't be {i}that{/i} scaredd that I said yes, right?"

    show LI scared at character_cent

    li "I'm gonna be honest, it was one of those moments where the bravery kicked in before the logical part of my brain could rethink it. I'm almost more scared I said it in the first place."

    show LI happy at character_cent

    li "But I have always wanted to do this."

    n "I book it towards the water."

    mc "Then let's go!"
    
    play sound sfx_splash1

    hide LI

    n "It's freezing cold, so I plunge myself up to my shoulders the moment the water is deep enough."
    n "I can hear [LIName] splashing in close behind me, and they dive in fully to acclimate."
    play sound sfx_splash2

    show LI scared at character_cent
    li "Oh my god it's so cold!"

    n "They swing their hair to get it out of their own eyes, sending the water droplets fling directly into mine."

    show LI happy at character_cent
    li "Oops. Sorry!"

    mc "Yep, I'm sure you are."

    hide LI

    n "I splash water back at them, but they dodge it by diving past me, heading deeper into the lake."
    n "They surface a few feet behind me and splash me the moment I turn towards them."

    play sound sfx_wet

    show LI happy at character_cent

    li "You've gotta be faster than that. I won bronze in my seventh grade swimming championship."

    mc "Ooh, bronze. Not gold?"

    show LI sad at character_cent

    li "No, but it was a super close race."

    n "I raise an eyebrow."

    show LI neutral at character_cent

    li "Besides, the two people who beat me were brothers, and I'm pretty sure they were half fish anyway. No 12 year olds should be able to swim as fast as they did."

    mc "The only exception of course would have been you if you'd won instead?"

    show LI happy at character_cent

    li "Exactly. You get it!"

    n "I tread my way towards [LIName], but they paddle backwards out of my reach."

    li "See, great swimmer. I was made to be in the -"

    show LI scared at character_cent

    stop music fadeout 0.5
    li "Shit, something bit me!"

    n "I stop moving towards them instinctively."
    n "[LIName] reaches under the water and screams."

    li "I think it's a leech!"
    play sound sfx_horror

    mc "Don't rip it-"

    n "I can't speak fast enough and [LIName] pulls, hard."
    n "Their hand shoots out of the water, but the only evidence of the creature left is watery blood and slightly grey slime coating their palm."
    n "Tiny bits of what look like the same slime float to the surface of the water."
    n "My stomach turns at the sight."

    mc "Oh god, you popped it."

    n "[LIName] gags."

    li "It still feels like it's biting me, we need to get out of here."

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

    li "This is so gross."

    n "I kneel next to them, leaning over slightly to make sure they also have no other extra new friends."

    mc "It is, but at least it's gone."

    show LI neutral at character_cent

    n "I take the shirt from them and bat their hands out of the way."

    mc "Let me see, I'm pretty sure you're not supposed to just rip them off like that."

    show LI sad at character_cent

    li "Technically I exploded it off of me."

    mc "I'm fairly certain that's not better."

    hide LI

    n "I move the shirt out of my way and take a better look at the damage."
    n "There's a small but noticable chunk of skin missing from [LIName]'s thigh, and the skin around it looks jagged, almost as if it had been ripped open."
    n "Which, to be fair, I suppose it was."
    n "It also looks like it's not planning on clotting any time soon, and I have to keep dabbing around it with the shirt to be able to actually look at it."

    show LI scared at character_cent

    li "What's my prognosis, doc? Please tell me it didn't like, leave a piece of it's head in my leg or something."

    n "I don't know much about leeches, but I'm pretty sure that's a thing tics can do, so it wouldn't surprise me."
    n "Especially with such an.... {w=2}unexpected ending to it's meal."
    n "I'm definitely not going to say that bit out loud though."

    mc "I think we need to get you checked out. At least so they can get it cleaned up, maybe see if it needs a stitch or something. It's not exactly a clean cut."

    show LI sad at character_cent

    n "I gesture for them to take my shirt and keep pressure on it."
    n "[LIName]'s hand closes over mine for a second, and I look up at them."
    n "They're just staring at my hand under theirs, and my bloody tee underneath them both."

    li "This was not the way this night was supposed to end."

    n "I reach over and grab their clothes, handing them their own shirt."
    n "Realizing mine is otherwise occupied, I pull on my jacket and zip it up."

    mc "Maybe we just stick to the rope and duct tape next time."

    jump hospital_path

label vamp_path:
    n "[LIName] takes the lead, and we follow a path leading up the hill."

    show LI neutral at character_cent

    li "I'm kind of glad we went with something outside. Don't get me wrong, dinner and movie dates are fun, but something about being in nature is just so.... exhilarating."

    mc "I agree, but I think for me, it's more grounding than anything. I just feel calmer outside. I'll take any chance to out among the trees."

    show LI happy at character_cent

    li "Oh 100 percent. I feel like anything can be made better just by moving it outside."
    li "The first time I went to an outdoor music festival, I was like {i}why is this not the regular version{/i}? It was so much more fun."
    
    mc "As long as you get the sound system right, I'd be so down for only outdoor shows!"
    mc "The fresh air helps when the crowds get to be too much too, instead of dealing with being overwhelmed in a stadium full of screaming people and fog machines and strobe lights."

    show LI neutral at character_cent 

    li "Absolutely. We could all use a little more fresh air, you know?"
    li "And for me, I think the higher I can get to get it, the better."
    li "But then, I think I just like being up high above everything, instead of all of this."

    n "[LIName] gestures to the the surrounding area."
    n "We stop to take in the scenery, but in the dim lighting it's hard to make out much other than what's right in front of us and a few extra dark blobs."

    show LI happy at character_cent
    
    li "I suppose that's why I like a lot of the newer RPGs. Like riding around in Red Dead 2, with those insane graphics?"
    li "I mean, right now, with this lighting, the game might even be better. At least you can see everything."

    mc "The downside though is you can't actually smell all that nature-y goodness around you when it's in pixel form."

    li "This is true. Have you played it?"

    menu:
        "I got so into it the first time I played, that I spent like a week bedrotting and just running around the world.":
            show LI happy at character_cent
            li "Honestly, same. And that ending! Oh my god, I actually cried, it was so good."

        "I haven't yet. It's in my library, but I know I'm gonna need a huge chunk of time for it.":
            show LI sad at character_cent
            li "You will. It's so worth it though, I highly recommend it moves to the top of your backlog."

    show LI neutral at character_cent

    mc "So, if you like fresh air and being outdoors and actually seeing everything, why take a job that makes you work nights?"

    show LI sad at character_cent

    li "The original plan was to be a pilot, but my bills didn't want to wait while I chased my dreams."
    
    show LI neutral at character_cent

    li "This job was the best one I could get at the time, and I can't afford a paycut anywhere else. Shit's too expensive these days."

    mc "I feel that."
    mc "My dream life is less 'working' and more 'being rich enough to go have as many experiences as possible'."

    show LI happy at character_cent

    li "What kinds of experiences?"

    mc "I've always wanted to try bungee jumping.{p} Or maybe paragliding? {p} Ooh, and swim the English Channel!"
    mc "There's also things like backpacking across Europe, and I've always wanted to see the Svalbard Seed Vault!"

    show LI neutral at character_cent

    li "A seed vault?"

    mc "Yeah! It's cool, they store duplicates of all of the world's seeds as a sort of backup in case we need it."
    mc "I don't think you can even go in, but I don't know, I think it would just be neat to see, even if it's just the outside."

    show LI happy at character_cent

    li "Okay, that is kind of cool."

    mc "Right? I guess I just want to be able to have the time and resources to do whatever makes me happy."
    mc "Even if in that moment, it's just reading a book, you know?"

    show LI sad at character_cent 

    li "I totally get it. I wish it were easier to do those things we dream about, no matter how outlandish."
    li "Instead I just feel like the only thing I'm doing lately is getting too old."

    mc "Hey now, none of that! We're young!"
    show LI happy at character_cent
    mc "It might not happen as quickly as we'd like, but we still have time."

    window hide
    scene hill at background_fill with dissolve
    pause 0.7
    window auto

    n "We've reached the top of the hill, and there's bit of a bank to get to the top, as if some of the path has been eroded away."
    n "[LIName] climbs up first, then offers me their hand to help me up."

    show LI blush at character_cent

    n "As I climb up next to them, neither of us let go of the other's hand."

    hide LI

    n "Together we set down the blanket and sit down next to one another."

    mc "Oh my god, the view here is beautiful."

    show LI happy at character_cent

    li "Yeah, it is."

    n "I turn towards [LIName], and realize that they're looking directly at me instead of the meteor shower overhead."

    show LI blush at character_cent

    n "I laugh, and before I've even realized I'm moving, I'm leaning forward, my face inches from theirs."
    n "They meet my eyes, and lean in too..."

    show LI scared at character_cent with hpunch

    stop music fadeout 0.3
    play sound sfx_bat
    
    n "Something big and black soars directly into [LIName]."
    
    li "What the fuck?!"

    n "It's gone a moment later, the bat flying away as if it didn't careen directly into the side of my date's face and ruin what could have possibly been the most romantic first kiss of my life."

    show LI angry at character_cent

    n "[LIName]'s hand clasps onto their neck."

    li "I think it bit me!"
    
    play sound sfx_horror

    n "When [LIName] pulls their hand away to look at it, I can see the small trails of blood already trailing down the side of their neck."

    n "[LIName] is staring at their hand and the two little streaks of blood present on it."

    show LI scared at character_cent
    
    li "Oh my god it {i}did{/i}, it bit me!"

    mc "Hey, hey it's gonna be okay."

    n "I pull up the sleeve of their shirt to hold against the bite, hoping it'll staunch the blood a little bit."

    mc "We've gotta get you to a hospital, you might need a rabies vaccine."

    show LI sad at character_cent

    li "What if it's worse?"

    mc "It won't be! You're going to be okay!"

    li "I was bitten by a bat!"

    show LI scared at character_cent

    li "I hate glitter, I CANNOT be a Cullen!"

    jump hospital_path

label hospital_path:

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Facey General Hospital{/size}\n\n{size=40}October 31, 2026{/size}\n{size=32}23:42{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    
    scene hospital at background_fill with dissolve
    play music music_hospital fadein 2.0

    hide LI

    n "After a longer wait than I'd hoped for, a nurse finally comes into the waiting room and calls [LIName]'s name."

    show LI scared at character_cent
    n "They hold out their hand for me to take so that I can follow them into the room, and I find myself rubbing small circles on the back of their hand as we walk."

    hide LI

    n "In the room, I sit down in a small plastic chair beside the door while [LIName] hops up onto the bed."
    n "The doctor is in and out in a matter of minutes, but the nurse comes back with a small metal cart and supplies to clean the wound and suture it."

    if route == "vamp":
        n "There is also a very unpleasant looking needle on the tray, right next to the slightly less imposing syringe I assume is to freeze [LIName] for the stitches."
        show LI scared at character_cent
        li "Um, what is that?"
        n "They gesture towards the bigger syringe, and the nurse offers them the least comforting smile I've ever seen."
        n "The nurse explains that [LIName] needs a rabies vaccine, and promises to be gentle."
        show LI sad at character_cent
        n "[LIName] does not look convinced."

    n "The nurse begins working, promising [LIName] that they'll be as quick as possible."
    n "[LIName] avoids looking at the nurse and what he's doing, and instead keeps their eyes locked on me."

    if route == "vamp":
        n "As the nurse picks up the vaccine syringe, [LIName]'s eyes go wide, and they reach out for my hand."
        show LI scared at character_cent
        n "Their grip is crushing, but I keep their eye contact while trying to not show any reaction in my own face."

    mc "I'm so sorry. This is not the way I imagined this date ending."

    show LI neutral at character_cent

    li "It's not your fault."

    show LI happy at character_cent
    
    li "Besides, I'm choosing to believe this is my superhero origin story. Like Spiderman!"

    if route == "wolf":
        li "Now I just need a good hero name. How do we feel about {i}The Majestic Doggo{/i}"

    elif route == "vamp":
        li "I was thinking I could call myself {i}The Great Batsby{/i}. Thoughts?"

    elif route == "mer":
        li "What do we think my hero name should be? I thought of {i}Leecholas{/i} on the way here, maybe it was fate."
        mc "{i}Leecholas?{/i}"
        li "Yeah. Like Legolas, you know? The badass elf archer dude from Lord of the Rings? Except.... leech."

    n "I stare at them for a moment, conflicted."
    n "On one hand, I'm glad they're feeling better."
    n "On the other..."

    mc "Absolutely not."

    show LI sad at character_cent

    li "Awww come on! I thought it was genius!"

    n "Even the nurse is having difficulties keeping his laugh under wraps."

    mc "The name needs some work, but I love the optimism."

    show LI happy at character_cent 
    
    li "Well, if my alternative is panicking, I figure planning my crimefighting future - plausible or not - is probably a bit better."

    mc "I agree."

    show LI neutral 

    n "The nurse finishes the stitches and covers the wound in gauze, then tells us we're good to go home."
    n "He hands [LIName] some discharge papers, and I hold out my hand to help them off the bed."

    show LI scared at character_cent
    li "Oh god, my car is still at the park."

    n "I shake my head before they can even suggest we go back for it."

    mc "Nope, you're going home. I'll drive you. We can get your car tomorrow."

    show LI neutral at character_cent

    n "[LIName] looks like they're about to argue, but they stop themselves."
    li "Yeah, okay. That sounds good, thank you."

    jump acttwo_path

label acttwo_path:

    stop music fadeout 2.0
    window auto

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 1, 2026{/size}\n{size=32}11:35{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    play music bg_music fadein 2.0
    
    window hide
    scene expression ("images/phone/texts/%s.png" % LIFolder)

    $ Msgs = [
    ["","How are you feeling?"],
    ["im okay. a bit sore but i guess that's normal after surviving a wild animal attack.",""],
    ["","I suppose so. It seems like we got you looked after soon enough though!"],
    ["","It will heal quickly, you'll see!"],
    ["yeah... I suppose",""],
    ["","Are you sure you're okay?"],
    ["ya... i did wanna ask tho, how are you feeling?",""],
    ["","I'm okay, just worried about you."],
    ["awww, thanks <3",""],
    ["but I guess i mean more like...",""],
    ["are you by any chance having any weird symptoms?",""],
    ["Stomach upset, headaches...?",""],
    ["","No... are you? It might just be the adrenaline crash after everything, maybe?"],
    ["","Or maybe some of the food was off?"],
    ["","Oh god if I gave you food poisoning too..."],
    ["No! i'm sure it's just the adrenaline like you said :D",""],
    ["i'm just tired, i feel a bit like my muscles are protesting a lot today",""],
    ["And my head hurts but that makes sense after everything i guess",""],
    ["","I think so too... but please don't ignore them if they don't get better, ok?"],
    ["i wont' XD i'm not letting a silly bite ruin everything tho",""],
    ["especially not a chance to see you again <3",""],
    ["","Awww... are you asking me out on a second date?"],
    ["if you're saying yes, then yes!",""],
    ["but this time, maybe we do something indoors?",""]
    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "acttwo_message"
    jump textConversation
    

label acttwo_message:
    window auto
    scene apartmentday at background_fill with dissolve

    n "I laugh as I read their text, and find myself nodding in agreement even though [LIName] can't see me."

    mc "Yeah, that's probably for the best lol"

    n "I move to switch from my messages to my notes app so that I can make a list of snacks to grab before the movie night we just planned."
    n "Except... as I swipe my thumb across the phone screen, I notice a scabbed over cut across the back of my hand, right between my thumb and index finger."
    n "A very uncomfortable memory flashes through my head."
    n "[LIName] bleeding in the park. My own view of my hands trying to help check over their wound."
    n "Their blood on my hands, directly over where the cut now sits."
    n "I can't remember getting it, but it looks recent enough that I can't convince myself that the black hole of anxiety that has bloomed in my gut is unwarranted."
    n "My stomach turns."
    n "Wasn't that one of the things [LIName] mentioned?"
    mc "Okay, calm down. You're just freaking yourself out."
    n "I turn on my computer and throw in as many keywords as I can think of."

    if route == "vamp":
        n "bat + bite + infection"
        n "can blood from someone who was bit by a bat make me sick too?"
        n "are the bats in blueberry acres national park dangerous?"

    elif route == "wolf":
        n "wild dog + bite + infection"
        n "can blood from someone who was bit by a wild dog make me sick too?"
        n "are there wild dogs in blueberry acres national park?"

    elif route == "mer":
        n "leech + bite + infection"
        n "can blood from someone who was bitten by a leech make me sick too?"
        n "can leeches in blueberry acres national park lake cause contagious infection through bodily fluid transmission?"

    n "The last one brings up the least amount of results, but a very specific one stands out at the top of the list."
    n "It's an article from the local news from about a year ago:"
    n "{i}Saint Sylvie Cathedral Priest Claims Cryptids Living In Blueberry Acres National Park{/i}"
   
    if route == "vamp":
        n "I am fairly certain it was just a normal bat, but curiosity gets the better of me."

    elif route == "wolf":
        n "I am fairly certain it was just a normal dog, but curiosity gets the better of me."

    elif route == "mer":
        n "I am fairly certain it was just a normal leech, but curiosity gets the better of me."

    n "I click the link and read through the article."
    n "Father Mitchell Camden of Saint Sylvie Cathedral claims a cryptid creature is loose in Blueberry Acres National Park, causing inhuman transformations in individuals who come into contact with it."
    n "Father Camden states the infection is transmitted by bite, and the first signs are often gastrointestinal distress and temporal pain."

    n "The article ends with a link to the cathedral's website."
    mc "I mean, I've come this far already. Might as well."
    n "I click the link, but the page it brings me to feels like a normal webpage for a church."
    n "As I scroll through though, I do notice that it seems despite his outlandish claims, Father Camden is still the priest there, and the email link on their contact page seems like it's his personal email."
    n "While I don't believe that [LIName] is about to turn into a creature of some kind, I am kind of intrigued about this mysterious priest."
    n "Was he bitten? Did the infection cause some sort of paranoia?"
    n "Before I can talk myself out of it, I type a quick email asking to talk about an animal bite that happened in Blueberry Acres and press send."
    jump datetwo_path

label datetwo_path:

    if route == "vamp":
        $ LIStage = "vampire"
    
    elif route == "wolf":
        $ LIStage = "wolf"

    elif route == "mer":
        $ LIStage = "merm"


    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 1, 2026{/size}\n{size=32}19:15{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene apartmentnight at background_fill with dissolve

    play sound sfx_knock_normal
    n "There's a knock at my apartment door, and I take one last look at myself in the mirror before I answer."

    show LI happy at character_cent
    n "The moment I open the door and see [LIName], I start to suspect they may have downplayed their symptoms a little bit."
    mc "Hey!"
    show LI neutral at character_cent
    n "I try to smile, but when their own smile falls, I know I'm doing an awful job."
    mc "I'm sorry, I am happy to see you. I just.... are you sure you're okay?"
    
    show LI happy at character_cent
    li "And hello to you too. You look great by the way."

    mc "I'm sorry, you're right, that was awful. I just worry about you is all."
    mc "Please, come in. Did you find the place okay?"
    
    show LI neutral at character_cent

    li "Yeah... "

    if route == "vamp":
        li "I got here okay, but I don't know if my stitches opened or something... I don't think they did, but I could smell blood the whole walk over, it was weird."
        n "The bite on [LIName]'s neck is still covered by a piece of gauze, but there's nothing other than that that looks concerning."
        mc "It looks okay to me. Does it feel like it's opened?"
        li "Not at all."
        show LI happy at character_cent
        li "It's probably nothing, I'm sure it's fine."
        mc "As long as you're sure."
    
    elif route == "wolf":
        li "I did, yeah. But I guess I should ask... you're not allergic to dogs, are you?"
        mc "No?"
        show LI happy at character_cent
        li "Okay perfect. I think someone in my apartment building must have thrown a dog bed or something into the washing machine."
        show LI sad at character_cent
        li "I did laundry this morning and now everything smells like wet dog."
        n "I take an exaggerated {i}sniff{/i} of the air around them and shrug."
        mc "If it makes you feel any better, I can't smell it!"

    elif route == "mer":
        show LI happy at character_cent
        li "I did! It started raining when I left, and I was kind of bummed because I didn't have an umbrella and I didn't want to show up looking like a wet rat. But then I started feeling kind of amazing?"
        li "I actually think maybe I needed the rain, some sort of refreshing cleanse from nature itself after all the bad energy of the last little bit."
        mc "I'm glad! Let's hope the bad vibes are officially gone, because I definitely think that was enough."

    show LI neutral at character_cent

    n "[LIName] sits down on the couch and I bring over some drinks and snacks."
    mc "What are we in the mood for?"
    n "I turn on the TV and pass them a controller, turning on the console wtih the other."

    n "They watch the screen as I scroll through the games I have installed."

    show LI happy at character_cent

    li "Should we go spooky? Two player Until Dawn could be fun!"
    n "I grin as I click on the game."
    mc "Absolutely!"
    
    hide LI

    n "I turn on movie night mode in the game."
    n "My name comes up first for character selection, and I immediately add Mike to my lineup."

    if route == "wolf":
        mc "I hope you're okay with me taking him, I cannot trust the wolf to -"
        show LI scared at character_cent
        n "My stomach clenches as I realize what I said."
        mc "I mean, I just really like playing Mike."
        show LI neutral at character_cent
        li "It's fine. I guess I just have a bit of trauma around that word."
        mc "I'm sorry. I really wasn't thinking."
        n "I wait a beat, trying to figure out how to fill in this little hole I seem to have dug for myself."
        li "Really, it's okay."
        show LI happy at character_cent
        li "But if you get to be Mike, I'm taking Sam."
        li "You get to meet the wolf, but I get to take a really sick, relaxing bath."
    elif route == "vamp":
        mc "I hope you're okay with me taking him, I need my little wolf friend."
        show LI happy at character_cent
        li "That's fine. But if you get to be Mike, I get to be Sam."
        li "You get the wolf - who is without question the best character in the game, let's be real - but {i}I{/i} get to take a bath."
    elif route == "mer":
        mc "I hope you're okay with me taking him, Wolfie is my favourite part of the game and I can't not be Mike when he's there."
        show LI happy at character_cent
        li "That's fine. But if you get to be Mike, I get to be Sam."
        li "You get the wolf - who is without question the best character in the game, let's be real - but {i}I{/i} get to take a bath, since water is apparently my new bestie and apparently the solution to all of my problems."
  
        n "I can't help the laugh that bursts out of me."
        mc "Okay, fair. I get a wicked puppy companion, and you get hydrated."
        li "Exactly! Obviously those are the best parts of the characters."
        n "I grin."
        mc "I mean, obviously. What other character traits could be more important? I get a dog, you get fluids."
        show LI scared at character_cent
        li "Fluids, hey?"
        n "[LIName] raises an eyebrow at my choice of words and I can feel my skin crawling at myself."
        mc "Oh my god not like that. Water! H2O! Not having dry, flaky, ashy skin!"
        show LI happy at character_cent
        li "Yep, mm-hmm. Suuuuurreeeee that's what you meant."
        mc "Okay we need to just start playing before I embarrass myself any more."
        li "Oh, don't worry. There'll be plenty of time for that, the night is young."
        n "I groan. They're right, and I know it."
        mc "In that case, let's get this horror show going so I can get as many of my embarrassments out of the way as fast as possible."
        li "Deal."
        jump datetwop2_path


label datetwop2_path:

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 1, 2026{/size}\n{size=32}21:45{/size}{/color}" at truecenter with dissolve
    pause 2.5

    hide text with dissolve
    scene apartmentnight at background_fill with dissolve

    play sound sfx_horror fadein 0.5 fadeout 0.2

    n "I knew the jumpscare was coming, but I still jumped when the window smashed."
    n "As I fall back onto the couch, it dawns on me just how rigidly I was sitting before, and I melt into the cushions as I laugh at myself."
    mc "That one gets me every time."
    n "I look over to [LIName]."

    show LI neutral at character_cent

    n "I'm not sure, but I think the circles under their eyes have gotten bigger."
    show LI happy at character_cent
    li "Honestly, me too. I'm more of a freeze response though, I just lock down."
    n "I want to believe [LIName]."
    n "My memories from the park flash in my head."
    if route == "vamp":
        n "[LIName] jumping away from me after the bat bit them flashes in my head, but I push the image away."
    elif route == "wolf":
        n "[LIName] jumping away from me after the dog lunged at them flashes in my head, but I push the image away."
    elif route == "mer":
        n "[LIName] jumping away from me after we saw the leech that bit them flashes in my head, but I push the image away."

    show LI neutral at character_cent
    n "A small part of me wants to call them out on it, but I choose to trust them instead."
    n "[LIName] knows themself better than I do. If they say they're okay, I'll believe them."

    show LI scared at character_cent
    li "I know I'm gorgeous but you really gotta look at the screen, lives depend on it!"
    mc "Oh shit!"

    n "I throw myself into the chase sequence, doing my best to hit the QTEs."
    n "But at the same time, I try to make sure I keep [LIName] in my peripheral vision, just to be sure they don't pass out on me."
    jump datetwop3_path

label datetwop3_path:
    
    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 1, 2026{/size}\n{size=32}23:20{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve
    
    scene apartmentnight at background_fill with dissolve
    show LI neutral at character_cent
    n "[LIName] fumbles the QTE, and we lose our second character."
    show LI scared at character_cent
    li "Fuck, I'm sorry. I don't know what's wrong, I feel like I'm losing the ability to push buttons."
    mc "I think that's our sign to call it a night."
    n "[LIName] is looking even worse now, and I can't in good conscience let them walk home alone at midnight in their current state."

    menu:
        "Why don't I drive you home?":
            show LI neutral at character_cent
            n "They look like they're about to argue, before thinking better of it."
            n "[LIName] nods their head."
            show LI happy at character_cent
            li "Yeah, that's probably a good idea. Thank you."
            jump drivehome_path
        "Why don't you just stay here tonight, so you can go to bed right away?":
            show LI scared at character_cent
            li "Are you sure? I feel like you've already had to help me so much, I don't want to impose..."
            mc "Not an imposition at all. It'll make me feel better knowing you're safe, and I can help you with anything if you need it tonight."
            n "[LIName] opens their mouth to protest, but I hold up my hand to stop them."
            mc "I mean it. I don't mind."
            jump stayover_path

label drivehome_path:
    scene apartmentnight at background_fill with dissolve
    hide LI
    n "I turn off the console and TV and help [LIName] gather their things."
    n "I catch a glimpse of my PC as I walk towards the door, and make a mental note to check my inbox when I get back."
    n "Looking at [LIName] as we walk out the door makes one thing glaringly obvious:"
    n "This is more than just a normal bite."
    jump actthree_path


label stayover_path:

    scene apartmentnight at background_fill with dissolve
    show LI neutral at character_cent

    mc "Why don't you take the bed? You're not feeling well, sleeping on a couch probably isn't going to help with that."
    show LI scared at character_cent

    li "No way. You took me to the hospital, you checked up on me, and now you're letting me stay here instead of stumbling home."
    li "I'm not also making you sleep on the couch in your own apartment for me."
    mc "I really don't mind, it's fi-"

    show LI angry at character_cent
    li "No."

    show LI neutral at character_cent
    li "I'll be fine on the couch. I promise."
    n "I debate if it's worth arguing, but [LIName] seems determined."
    mc "Okay."
    
    show LI happy at character_cent
    mc "I'll go grab some pillows and blankets."
    n "I turn off the console and hand them the remote for the TV."
    mc "You get comfy. I'm grabbing you a glass of water and maybe some ibuprofin too."
    n "Before they can protest, I add"
    mc "Not because I'm taking care of you. Because I don't want you rifling through my medicine cabinet later tongiht and finding all of my dirty secrets."
    n "They laugh."
    li "Okay, fair."
    n "As I pull out a spare blanket from the closet, I catch a glimpse of my PC."
    n "I make a mental note to check my inbox for any replies."
    n "This is definitely more than just a normal bite."

label actthree_path:

    scene frame with fade
    pause 0.5 
    show text "{color=#fff3dc}{size=64}Saint Sylvie Cathedral{/size}\n\n{size=40}November 3, 2026{/size}\n{size=32}11:50{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene church  at background_fill with dissolve
    play music music_church fadeout 1.5 fadein 2.0

    n "Father Camden refused to give me much information over email, and insisted I come to the church in person."
    n "It seems relatively normal at first glance - though they've chosen an... interesting orientation for the crosses on their banners."
    n "They look less like the crucifixes I've seen at other churches or in media, tilted slightly on their sides instead of straight up."
    n "There's also a slightly concerning lack of imagery of a certain religious figure, but maybe they're just trying to be more inclusive?"
    n "A voice booms from behind me and I jump."

    show priest neutral at character_cent with dissolve

    p "My apologies, I didn't mean to frighten you."
    p "Thank you for coming to speak to me in person. I prefer to have these conversations here, where I can offer more personalized guidance."
    n "The way he's examining my face makes me feel like there's more to the story, but I don't press... for now, at least."
    mc "Thank you for meeting with me. Do you have these conversations a lot?"
    p "More than I would care to, unfortunately."
    n "He leads me down the aisles, towards the pulpit."
    p "I was unfortunate enough to encounter the creature years ago in the park, and have devoted all I can to ensuring the .... {i}influence{/i} doesn't spread."
    mc "I'm sorry, I don't understand. Influence?"
    n "He looks me up and down again."
    n "My skin crawls, and I get the unnerving sensation of being underneath a microscope."
    p "I will explain, but like I mentioned, I prefer to give more personalized guidance on these matters."
    p "Your email only mentioned the contact and the symptoms, but you didn't mention if you were the one attacked?"
    mc "No, not me. My-"
    n "I hesitate."

    menu:
        "My friend.":
            p "And your friend... have you known them long?"
            mc "Not really, but that doesn't mean I don't care about them."
            p "In that case, I'm sorry for what I must tell you next."
        "My partner.":
            p "In that case, I'm sorry for what I must tell you next."
        "My .... casual trauma acquaintance? It's a long story.":
            p "Well then, that might make what I'm about to say a little easier to digest."

    mc "What do you mean? It's just an animal bite, right?"
    n "He stares at me, and for a moment I wonder if he has blinked at all in the time since I've arrived."
    p "Not quite. I assume they have since seen a doctor, either for the initial bite or the symptoms following?"
    mc "Yeah, I took them to the hospital that night."

    if route == "vamp":
        mc "They got a few stitches and a rabies vaccine, and the hospital said they'd be okay."
    else:
        mc "They got cleaned up and a few stitches. But the hospital said they were going to be okay."

    p "They would. Modern medicine is not particularly equipped to deal with this particular type of infection. Truthfully they're not even aware of it's existence."
    mc "What do you mean? What kind of infection?"
    p "Perhaps infection isn't quite the correct term. An infection can typically be cured with the correct treatment."
    p "This ... {i}affliction{/i} cannot."
    n "My stomach drops. My entire body feels like it's gone numb, except for a stinging pins and needles sensation in my hands and feet."
    mc "No, it's just an infection. They're going to be fine."
    p "I'm very sorry, but no. They're not."

    if route == "vamp":
        mc "Is it rabies? They got a rabies vaccine, they're already covered for that."
    else:
        mc "No, the hospital would have known if it was serious. They said [LIName] didn't need a rabies vaccine or anything like that."

    mc "The hospital said [LIName] is going to be okay."
    p "The hospital was wrong."
    mc "Then what the fuck is it?"
    n "Father Camden takes a deep breath and places a hand on my shoulder."
    n "I think he meant it to be comforting, but goosebumps break out over my skin as if it's trying to crawl away from his touch."
    p "They will continue to deteriorate until the transformation is complete."
    n "I take a step back, pulling my shoulder out of his grip."
    mc "Can you please just explain what the fuck is going on?"
    n "He walks away, towards the stand at the front of the room."
    n "He looks like he's about to give me a sermon, and I feel my hands starting to shake in frustration."
    mc "Please, I just need to know."
    p "The creature that bit [LIName] was not an ordinary animal."
    p "And now, [LIName] is not an ordinary human."
    n "I hold my hands up, taking a few small steps backwards."
    n "This guy is completley out of it."
    mc "This was a mistake. I need to go."

    show priest angry at character_cent
    p "NO!" with vpunch

    show priest neutral at character_cent
    p "I know that this sounds impossible, I do. But you {i}must{/i} trust me."
    p "I've seen this before, more times than I care to admit."
    p "If [LIName] has already begun to display the symptoms you mentioned in your email, it's already too late."
    p "The transformation has already begun."
    mc "No, they're just having a stress resposne to a traumatic event. It's normal."
    p "No, not this time."
    p "A normal human would be healing physically by now."
    p "Therein lies the issue. [LIName] will never be {i}normal{/i} again."
    mc "You're crazy, dude."
    p "I understand why you think that but I need you to listen to me. Staying near them is dangerous."
    mc "I can't just leave them!"
    p "You have to. Not just for your own sake, but the entire town."
    p "Letting them roam free is putting everyone in danger."
    n "He looks pointedly at me."
    p "Including [LIName]."
    mc "I can't..... I'm not just going to abandon them. They need me."
    p "No. You cannot help them."
    mc "But I-"
    p "No. I've watched this before. People who have been bitten by the creatures in Blueberry Acres..."
    p "It always ends the same."
    p "People die."
    p "Good people, like yourself, who just want to help those they love."
    n "His voice softens slightly."
    p "Do you think [LIName] wants to hurt you? I know you want to stay to help, but how will they react when they become the cause of your destruction?"
    mc "What.... what am I supposed to do then?"
    p "Let {i}me{/i} help them instead. Just let me know where they are, and I will take them somewhere safe. I'll make sure they cannot harm anyone, including themselves."

    menu:
        "Maybe this really is too much for me to handle on my own.":
            mc "Okay."
            n "Father Camden nods his head and readies himself"
            show priest angry at character_cent
            p "Good, child"
            n "I give him my address."
            p "Why don't you go have a bit of lunch, take some time away from home to relax. Maybe go see a film?"
            p "In three hours, you can return home and everything will be taken care of, and you can move on from this stressful period."
            jump firstbad_ending
        "There is no way I'm letting this guy anywhere near [LIName].":
            mc "No, this was a mistake. I'm sorry to have wasted your time."
            n "Father Camden reaches out to stop me, but I turn and start walking."
            show priest angry at character_cent
            p "You can't save them, you're only ensuring that this kills both of you."
            p "If you refuse to save yourself, then at least lock them up and make sure no one else pays the price for your recklessness!"

            hide priest with dissolve
            n "I rush out of the church to my car, and lock the doors immediately."
            mc "I'm not giving up on them. No way."
            n "But still, whatever is happening to [LIName] is far from normal."
            n "Maybe keeping them close isn't a bad idea, if only so I can make sure that they don't get sicker while they're home alone."
    jump postchurchmessage_path

label postchurchmessage_path:
    
    play music bg_music fadeout 1.5 fadein 2.0

    window hide
    scene expression ("images/phone/texts/%s.png" % LIFolder)

    $ Msgs = [["","So I've been thinking..."],
    ["thats terrifying",""],
    ["","HAHAHA You're so funny"],
    ["","But seriously."],
    ["","Since you've been staying at my place anyway, do you want to just make it official?"],
    ["are you asking me to move in w/ you? So soon?",""],
    ["are you sure?",""],
    ["","It doesn't have to be permanent if you don't want to!"],
    ["","But I'm not opposed if you do"],
    ["","And if you don't it could just be temporary while we figure out what's going on."],
    ["youre really sure?",""],
    ["","Yeah, I am."],
    ["then Id love to",""]
    ]

    $ counter = -1
    $ end = len(Msgs) - 4
    $ jumpto = "actthreemontage_path"

    jump textConversation

label actthreemontage_path:

    window auto
    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 6, 2026{/size}\n{size=32}10:30{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene apartmentday at background_fill with dissolve

    n "We finish unpacking the last of [LIName]'s belongings."
    n "There was a lot of shuffling things around and packing some things up, but I think we've finally managed to find a place for everything."
    n "[LIName] flops down onto the couch, laying their head back on the cushions."
    show LI happy at character_cent
    li "Pop quiz time!"
    mc "Um, no one said anything about a quiz."
    li "Yeah, that's kinda the point of a pop quiz. You don't know it's coming."
    mc "Okay... I can't really argue with that one. Shoot."
    li "You could have just walked away after I got bit, so there is {i}clearly{/i} some sort of intense appeal to me that I'm tragically unaware of."
    li "So care to enlighten me? What makes me worth sticking around for?"

    menu:
        "You're funny.":
            show LI scared at character_cent
            n "[LIName] sighs dramatically."
            li "{i}Funny{/i} they say. And yet I've never seen them at my stand-up shows."
            mc "You do stand-up? Since when?"
            show LI happy at character_cent
            li "No.... but it would be fun to try. Maybe we should give it a shot."
        "Have you seen you? You're gorgeous and agreed to go out with me, why would I let you go?":
            show LI scared at character_cent
            li "Am I now?"
            show LI happy at character_cent
            li "Dang, apparently I gotta work on my self-confidence."
            mc "I mean, I'm totally down to help remind you!"
        "I don't know what it is exactly, but I feel drawn to you.":
            show LI happy at character_cent
            li "I feel it too."

    li "But regardless, I'm really glad you did stay."
    mc "I'm glad I did, too."
    n "[LIName] smiles at me before closing their eyes, apparently content to bask in the moment."
    mc "Hold on a second, what about me?"
    li "What do you mean?"
    mc "What do you like about me? I mean, if we're giving out compliments, I want some too!"
    li "You're right, that was rude of me. Where do I even start?"

    hide LI
    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 12, 2026{/size}\n{size=32}8:47{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene apartmentday at background_fill with dissolve
    show LI happy at character_cent

    n "I'm still getting used to seeing [LIName] every morning, but I'm finding I really like it."
    n "They're in the kitchen when I leave the bedroom, pushing eggs around in a pan."
    li "Morning! Are you okay with scrambled eggs and bacon for breakfast?"

    menu:
        "Of course! It's a classic for a reason, right?":
            li "Absolutely it is. I'm just gonna finish these up. Could you grab the bacon?"
            mc "Sure thing!"
        "Eggs yes, but I'll pass on the bacon.":
            mc "I'll make some toast instead to go with mine, do you want some too?"
            li "No thank you. I think I'm not getting enough protein or something, I've been craving this so badly lately."
        "I'm gonna pass, but thank you. I don't eat meat, remember?":
            show LI scared at character_cent
            li "Oh my god I completely forgot. I'm so sorry."
            mc "It's really okay. You make your breakfast, I'll have some oatmeal."
            show LI happy at character_cent
            li "That's cool! I'm sorry I probably should have just asked you first and made what you wanted to, but I've been craving this so much lately. I'm starting to think all this stress is making me burn through protein or something, it's all I seem to want lately!"

    n "We settle down to eat, and [LIName] places their plate down in front of them."
    n "They dig in, bringing three strips of bacon to their mouth at once."
    show LI scared at character_cent
    mc "Careful, you wouldn't want to taste your food or anything."
    show LI neutral at character_cent
    li "You're right, this is gross."
    n "[LIName] makes a point of slowing down, carefully picking one piece of bacon and taking a slow bite."
    mc "It's fine, I'm teasing."
    show LI happy at character_cent
    mc "Besides, you're kinda cute with your cheeks all puffed out like that. Like a rabid little hamster."
    show LI scared at character_cent
    n "They puff out their cheeks and scrunch their nose in what I assume is their best hamster impression."
    show LI happy at character_cent
    li "But like, a cute rabid hamster, right?"
    mc "The cutest."

    menu:
        "Kiss them":
            li "Oh... oh wow."
            li "Note to self: embrace the hamster life."
            li "It seems to have perks."
            n "I shake my head and laugh."
            mc "Don't ruin the moment!"
            $ mcturned = True
        "Boop their nose":
            li "... Did you just...?"
            n "I smile as wide as I possibly can."
            mc "Sure did."
            li "Well, in that case..."
            n "[LIName] boops my nose back."
            li "Back at you."


    hide LI
    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}November 29, 2026{/size}\n{size=32}22:22{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    scene apartmentnight at background_fill with dissolve
    show LI scared at character_cent

    li "I can't believe I slept the day away."
    mc "It's okay. Clearly you needed it, you were struggling to even keep your eyes open."
    show LI neutral at character_cent
    li "Still, I feel bad."
    mc "Really, it's okay."
    mc "Oh, and dinner's in the fridge. I made a sort of veggie taco skillet thing."
    show LI sad at character_cent
    li "Thank you, but I think I'm okay for right now."
    mc "Are you sure? You haven't really been eating, that might be why you're so tired."
    li "I've been eating!"
    mc "Okay, technically correct. Maybe I should have said you haven't really been eating {i}properly{/i}."
    show LI scared at character_cent
    li "Hey, I'm still eating three meals a day, just not necessarily at the traditional times."
    mc "Yes, and when was the last time you ate a vegetable?"
    show LI neutral at character_cent
    n "[LIName] stares blankly at me."
    li "Good point."
    li "But I don't know, I just haven't been feeling it lately. Maybe I should go get some bloodowork done or something. All I want is like a giant rare steak."
    mc "What about a compromise? Maybe we get some steakhouse takeout tomorrow -"
    show LI happy at character_cent
    li "Oh my god yes-"
    mc "- As long as you also eat a veggie as a side. Corn. Peas. Just something. You need some fibre with all of that protein."
    li "Deal!"
    jump datethree_path

label datethree_path:

    scene frame with fade
    pause 0.5
    show text "{color=#fff3dc}{size=64}Home{/size}\n\n{size=40}December 3, 2026{/size}\n{size=32}18:30{/size}{/color}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    if route == "vamp":
        $ LIStage = "svampire"
    
    elif route == "wolf":
        $ LIStage = "swolf"

    elif route == "mer":
        $ LIStage = "fish"

    scene apartmentnight at background_fill with dissolve

    n "A lot has changed over the last few days."
    n "[LIName] has been... changing. Even more than before."
    n "I can no longer deny that there may have been some truth to what Father Camden said about this being incurable."
    n "But the danger part?"
    n "That's where I know he was wrong."
    n "[LIName] is still the same person I went on that first date with."
    n "They're still sweet and caring, and they still worry too much about me taking care of them."
    n "As they lead me into the bedroom, ready to show me the surprise they've been working on all afternoon, I feel completely..."
    n "Safe."

    li "Okay, ready?"
    mc "Absolutely."

    scene lastdate at background_fill with dissolve
    play music music_third_date fadeout 1.5 fadein 2.0

    li "I know it's not exactly the same, but I wanted to get a redo of our first date."
    li "But without the possibility of wild animals this time."
    n "The grin on my face is so wide it practically hurts."

    show LI neutral at character_cent

    li "At least, not any unfamiliar wild animals."
    mc "I love it. Thank you."
    li "No, thank you."
    li "You've done a lot more than so many people would have. You could have walked away and let me figure this out on my own, it wasn't your problem to fix."
    li "But you didn't. You stayed."

    menu:
        "And I'd do it again.":
            li "I don't know what I did to deserve you, but I'm glad I found you."
        "Let's see how this food tastes before I decide how sappy to get.":
            li "Given my recent penchant for raw meat, that seems reasonable."

    n "[LIName] has the food separated - raw meats for them, and a mini charcuterie spread for me."
    n "We eat underneath the glow-in-the-dark stars they've placed all over the walls and ceilings, sitting side by side by side on the bed."

    if route == "vamp":
        show LI sad at character_cent
        li "I wish I could kiss you right now."
        mc "I wouldn't be opposed to it, you know."
        li "I know. But I'm worried about these fangs."
        li "What if they cut you? I'm scared you'd turn into this too."
        if mcturned:
                mc "We've kissed before while you were infected, it might already be too late for that anyway."
        show LI neutral at character_cent
    
    else:
        li "I wish I could kiss you right now."
        mc "I wouldn't be opposed to it, you know."
        li "Looking like this?"
        mc "You're still you."
        li "I know. But I'd be worried... "
        li "We don't know if this is transmittable. I got bit and turned, what if we kiss and my saliva gets into your mouth and then you turn too?"
        if mcturned:
                mc "We've kissed before while you were infected, it might already be too late for that anyway."

    menu:
        "Would me being the same really be the worst thing?":
            li "I... I don't know."
        "Then we'll just have to find some sort of workaround.":
            li "That would be amazing, thank you."
            mc "Give me one second."
            n "I run to the kitchen and quickly grab a sheet of plastic wrap."
            n "I hold flop down beside [LIName] again and hold it in between us."
          

    n "I lean in, and [LIName] begins to close the distance to meet me in the middle."

    scene black
    stop music fadeout 0.3
    pause 0.5

    play sound sfx_knock_frantic
    scene apartmentnight at background_fill with hpunch

    n "Something bangs on the front door of the apartment."

    li "What the fuck?"
    mc "You stay here, I'll go see who it is."

    n "[LIName] stays in the bedroom, but makes sure to hide themself behind the door, out of view from the hallway."
    n "I open the door to find Father Camden there, fist raised as if he was about to bang on the door again."

    show priest angry at character_cent with dissolve

    mc "What are you doing here?"
    p "I cannot allow a monster to continue threatening this community."
    p "I was hoping you would come to your senses, but if you refuse to act, then you leave me no choice."
    n "I try to close the door on him, but he shoves his way into the apartment."
    mc "How did you even find me?"
    p "I've been keeping an eye on the situation since you came to my church."
    mc "You mean you've been stalking me."
    p "No. I've been monitoring a threat."
    p "And I'm no longer content to allow that threat to remain here." with hpunch
    
    play sound sfx_impact
    n "I try to push him back towards the door, but he shoves me away. I catch myself on the wall before I fall completely."
    mc "No. You need to leave. You're not welcome here."

    show priest furious at character_cent
    p "I'm not leaving without that {i}thing{/i}!"

    n "[LIName] leaves the room, and Father Camden freezes when he sees them."

    show priest furious at character_right
    show LI neutral at character_left with dissolve

    p "Monster! Stay back!"
    n "He pulls out a crossbow and aims it at [LIName]."
    
    play music music_cinematic_battle fadein 1.0

    n "I throw myself in front of it, protecting them."
    mc "What the fuck do you think you're doing?!?!"
    p "Saving this town!"

label finalconfrontation:   
    menu:
        "Look, we can talk this out." if talkpathopen:
            n "Father Camden laughs, but it's bitter."
            p "Talk about what? For all I know, it's already spread the infection to you as well."
            mc "There has been no spreading of any infections, I promise."
            li "Really, there hasn't been anything."
            p "It doesn't matter. Even if it hasn't happened yet, I'm not letting the risk get any worse. This ends now."
            $ talkpathopen = False
            jump finalconfrontation
        "I can't do this, I'm done.":
            li "What?!"
            mc "I'm so sorry. This is just... it's too much."
            mc "Having a cryptid partner is one thing. I was trying to make it work, I really was."
            mc "But being stalked by a crossbow-wielding priest on top of that?"
            mc "I'm sorry. I just want a normal life back."
            jump walkaway_ending
        "Maybe the real threat is you. [LIName], you with me?":
            li "Absolutely."
            n "[LIName] moves faster than I've ever seen them, an they're at Father Camden's side in a blink."
            p "Aaaaaghgh!!"
            li "They gave you an out, you should have taken it."

            play sound sfx_fall
            n "The crossbow shoots, but [LIName] has already knocked Father Camden onto his back."

            hide priest
            n "[LIName] draws their arm back, ready to strike, but I stop them."
            mc "Wait!"
            li "Please don't tell me you want to save him?"
            mc "No, not at all."
            p "Thank you-"
            mc "No death is too easy. He told me he's done this before. He should pay for all of the lives he's taken."
            n "[LIName] looks down at Father Camden, then lowers their arm."
            li "You know what, you're right."
            li "We're not the monsters you think we are. The only monster here is you."

            play sound sfx_thud
            n "[LIName] grabs Father Camden's head and slams it down into the floor, knocking him unconcious."
            li "I hope that wasn't too hard. He should wake up from that, right?"
            n "I look at the priest passed out cold. He's still visibly breathing at least."
            mc "I hope so."
            jump fight_ending
        "About that..." if mcturned:
            n "I'm moving before my brain even registers the decision."
            n "My hands clamp around Father Camden's arm, wrenching it - and the crossbow - towards the wall."
            play sound sfx_impact
            n "He pulls the trigger, but the arrow lodges safely into the wall."
            li "Damn."

            play sound sfx_fall
            n "[LIName] lunges towards us, knocking all three of us to the floor."
            
            hide priest
            hide LI

            p "Let me go!"
            li "No."
            n "[LIName] presses their hand over Father Camden's mouth to shut him up, then turns to me."

            show LI neutral at character_right with hpunch

            li "You've been letting me believe I was a risk to you this whole time without telling me you were already turning?"
            mc "I genuinely didn't know. Your symptoms were so obvious."
            mc "I barely noticed any changes at all."
            li "You did spend a lot of time worrying about me, maybe you just overlooked them?"
            mc "Or it just affected us differently."
            mc "Either way, we can figure it out later. We've got more pressing issues to deal with right now!"
            n "We both look back towards the man struggling underneath us."
            li "Right. What's the plan?"
            mc "He told me he's done this before. I don't know how many times, but we can't just let him go."
            mc "He'll just come after us, or he'll find someone else to torment and kill."
            mc "I don't think we have a choice."
            n "[LIName] nods."
            n "Without breaking eye contact with me, [LIName] lifts Father Camden's head off of the floor and twists."
            n "The priest falls limp onto the floor."
            li "It was my turn to save you."
            mc "Oh, [LIName]..."

            jump turn_ending






#FOR PHONE MESSAGES TEMPLATE:
    #scene expression ("images/phone/texts/%s.png" % LIFolder)

    #$ Msgs = [["","MC DIALOGUE HERE"],
    #["LI DIALOGUE HERE",""],
    #]

    #$ counter = -1
    #$ end = len(Msgs) - 4
    #$ jumpto = "NEW SCENE"

    #jump textConversation
    




# ==== ENDINGS ARE OLD SCHOOL STYLE FADE IN PER LINE


label walkaway_ending:

    window hide
    $ quick_menu = False

    stop music fadeout 1.0
    scene frame with fade
    play music music_sad fadein 1.0

    show text "I haven't gone back to the apartment yet. I'm too afraid of what I'll find." as ending_line_1:
        xalign 0.5
        yalign 0.25
    with dissolve
    pause

    show text "No cops have come looking for me at the hotel though, and I haven't seen anything about a disturbance of any kind at the apartment complex." as ending_line_2:
        xalign 0.5
        yalign 0.50
    with dissolve
    pause

    show text "As I close the browser on my phone for the millionth time today, I notice the dating app logo tucked neatly inside of a folder on my home screen." as ending_line_3:
        xalign 0.5
        yalign 0.75
    with dissolve
    pause

    hide ending_line_1
    hide ending_line_2
    hide ending_line_3
    with dissolve

    show text "I guess I never deleted it." as ending_line_4:
        xalign 0.5
        yalign 0.25
    with dissolve
    pause

    show text "I fix that mistake immediately, and breathe a sigh of relief as the app uninstalls." as ending_line_5:
        xalign 0.5
        yalign 0.50
    with dissolve
    pause

    show text "Maybe being single is for the best." as ending_line_6:
        xalign 0.5
        yalign 0.75
    with dissolve
    pause

    hide ending_line_4
    hide ending_line_5
    hide ending_line_6
    with dissolve

    show text "At the very least, I'm never trying the app route again." as ending_line_7:
        xalign 0.5
        yalign 0.40
    with dissolve
    pause

    show text Text("THE END", size=50, color="#fff3dc", xmaximum=1100, text_align=0.5) as ending_line_8:
        xalign 0.5
        yalign 0.65
    with dissolve
    pause

    stop music fadeout 1.0
    scene black with fade

    $ quick_menu = True
    return


label fight_ending:

    window hide
    $ quick_menu = False

    stop music fadeout 1.0
    scene frame with fade
    play music music_happy_end fadein 1.0

    show text "We saw from a distance the police arriving after a few hours, but [LIName] were already gone..." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "We heard Father Camden died that night, and a rumour began spreading after that..." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "'Creatures in Blueberry Acres Park maul and devour a local priest'" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "[LIName] would never, but people would believe anything they are told." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "Blueberry Acres Park seems like the perfect place to start our new life, tho..." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "And at least, we are together..." at truecenter with dissolve
    pause
    hide text with dissolve

    show text Text("THE END", size=50, color="#fff3dc", xmaximum=1100, text_align=0.5) at truecenter with dissolve
    pause
    hide text with dissolve

    stop music fadeout 1.0
    scene black with fade

    $ quick_menu = True
    return

label firstbad_ending:

    window hide
    $ quick_menu = False

    stop music fadeout 1.0
    scene frame with fade
    play music music_sad fadein 1.0

    show text "I end up wandering around the mall for the next three hours, anxiety eating away at me." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "I tell myself it's almost over. That [LIName] will be taken care of, and they will be able to get the help that they need." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "The help that I couldn't give them." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "But.... that's not true, is it?" at truecenter with dissolve
    pause
    hide text with dissolve

    show text "It can't be cured." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "Father Camden is going to make sure they can't hurt anyone." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "I try to tell myself that he's going to hurt them first, but I know that's not entirely true either." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "{i}I{/i} hurt them first." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "It was {i}my{/i} suggestion that put them in that creature's path in the first place." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "And then I sold them out." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "My apartment is clean when I arrive." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "Too clean." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "There's no sign that anyone was here at all." at truecenter with dissolve
    pause
    hide text with dissolve

    show text "Well, aside from the small business card sitting on my coffee table, a picture of the same cross from the church on it." at truecenter with dissolve
    pause
    hide text with dissolve

    show text Text("THE END", size=50, color="#fff3dc", xmaximum=1100, text_align=0.5) at truecenter with dissolve
    pause
    hide text with dissolve

    stop music fadeout 1.0
    scene black with fade

    $ quick_menu = True
    return


label turn_ending:

    window hide
    $ quick_menu = False

    stop music fadeout 1.0
    scene frame with fade
    play music music_mysterious fadein 1.0

    show text "Neither [LIName] or I can pass as human anymore." as ending_line_1:
        xalign 0.5
        yalign 0.25
    with dissolve
    pause

    show text "Worrying about the body in the apartment is the least of our concerns now that the physical aspects of my transformation have started." as ending_line_2:
        xalign 0.5
        yalign 0.50
    with dissolve
    pause

    show text "We just... leave him there." as ending_line_3:
        xalign 0.5
        yalign 0.75
    with dissolve
    pause

    hide ending_line_1
    hide ending_line_2
    hide ending_line_3
    with dissolve

    show text "We end up back where we started." as ending_line_4:
        xalign 0.5
        yalign 0.25
    with dissolve
    pause

    show text "Blueberry Acres National Park." as ending_line_5:
        xalign 0.5
        yalign 0.50
    with dissolve
    pause

    show text "There's a cave system underneath the park that's been the subject of urban legends for years, and it seems like the perfect place to start our new life." as ending_line_6:
        xalign 0.5
        yalign 0.75
    with dissolve
    pause

    hide ending_line_4
    hide ending_line_5
    hide ending_line_6
    with dissolve

    show text "There's evidence of other beings here too... just like us..." as ending_line_7:
        xalign 0.5
        yalign 0.25
    with dissolve
    pause

    show text "There's weird markings on the walls, old clothes, and a very crude carving in one of the walls of a creature that looks suspiciously like we look now." as ending_line_8:
        xalign 0.5
        yalign 0.50
    with dissolve
    pause

    show text "Who knows. Maybe we'll find our own little community of other quote unquote {i}monsters{/i}." as ending_line_9:
        xalign 0.5
        yalign 0.75
    with dissolve
    pause

    hide ending_line_7
    hide ending_line_8
    hide ending_line_9
    with dissolve
    
    show text "But even if we don't, we still have each other." as ending_line_10:
        xalign 0.5
        yalign 0.40
    with dissolve
    pause

    show text Text("THE END", size=50, color="#fff3dc", xmaximum=1100, text_align=0.5) as ending_line_11:
        xalign 0.5
        yalign 0.65
    with dissolve
    pause

    stop music fadeout 1.0
    scene black with fade

    $ quick_menu = True
    return
