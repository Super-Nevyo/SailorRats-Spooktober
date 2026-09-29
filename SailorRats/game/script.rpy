# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(" Jeoseung Saja ")
define a = Character(" Amarok ")
define mc = Character (" You ")
define l = Character (" Lily ")
define m = Character (" Morrigan ")
define n = Character (None)
define notif = Character (" Notifications ",what_color="#FFA500" )

default LIName = "Character"
default LIFolder = "character"
default LIStage = "normal"
default route = "none"

define li = Character(" [LIName] ")

image LI neutral = "images/characters/[LIFolder]/[LIStage]/neutral.png"
image LI happy = "images/characters/[LIFolder]/[LIStage]/happy.png"
image LI angry = "images/characters/[LIFolder]/[LIStage]/angry.png"
image LI sad = "images/characters/[LIFolder]/[LIStage]/sad.png"
image LI scared = "images/characters/[LIFolder]/[LIStage]/scared.png"
image LI blush = "images/characters/[LIFolder]/[LIStage]/blush.png"


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

    $ Msgs = [["","hello hi its me\nmeow"], ["Thankfully.",""],["","howdy"], ["uwu",""],["","im really looking forward to our date"],["me too uwu",""],["","yay yippee yay :3"],["meow meow :3",""]]
    $ counter = -1
    $ end = 3
    jump textConversation

    play music haunted_bg fadein 2.0
    scene black with fade
    pause 0.5 
    show text "Home {p}October 19, 2026 {p}19:30" with dissolve
    pause 2.5
    hide text with dissolve

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

        "Hey.":
            n "Sending the first message is the hardest part, so I keep it simple. A little basic, sure, and yet, somehow, still effective."
            jump generic_path


        "Do you actually play all those games or just collect them?":
            jump gamer_path


label generic_path:
    mc "Hey."

    li "Hey, how's it going?"

    mc "Not too shabby, you?"

    li "It's going okay. I picked up a coworkers shift so I'm working a double tonight which sucks tho"

    mc "Damn, that sucks. More money though at least?"

    li "Thankfully. The only thing getting me thru is thinking of how I might be able to treat myself to a brand name mac and cheese box next week."

    mc "Mmmmm .... delicious brand name cardboard pasta."

    li "See, you get it! i only have the best after a hard days work XD"
    jump genericsecondchat_path

label gamer_path:
    mc "So... are you ACTUALLY gonna play those games or is it just to have them? xd"

    li "wow, attacking me already 😭"
    li "please tell me your library is worse"

    mc "I mean... everyone has a bunch of games in their library, but..."

    menu:
        "Of course I play everything I get!":
            li "haha at least one of us has their life together xd."

        "We are not discussing my library!! xdd":
            li "THAT bad huh? haha xd"

    li "Anyway, what are you up to today?"

    mc "Not much, I'm trying to pick something to play!! I'm between Silksong and Blue Prince..."
    mc "I think its gonna be Blue Prince."

    li "oh nice! that's an awesome game"
    li "Should I leave you to it? :D"

    mc "What? Of course not! It's a puzzle game haha you gotta help me!"

    li "maybe we could play it together sometime! I dont want to distract you now haha"

    mc "But... you are a good distraction (ᗒᗣᗕ)՞"

    li "haha you are cute uwu"
    li "we should definitely do that!" 
    li "What else do you do for fun?"

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

    mc "oh yeah?  that sounds like fun actually!"
    mc "I think we will get along pretty well haha"

    li "yeah i think so too..."
    li "we should hangout some time soon!! uwu"    

    mc "I would really like that uwu - okay! I gotta go now, I've got work in the morning, but chat later?"

    li "Absolutely! Night!" 
    
    jump gamersecondchat_path

    
label genericsecondchat_path:

    scene black with fade
    pause 0.5
    show text "Home {p}October 26, 2026 {p}18:00" with dissolve
    pause 2.5
    hide text with dissolve


    scene bednight

    n "I'm about to get into bed when my phone buzzes from my nightstand, the dating app's logo visible on the pop-up banner."
    play sound sfx_phone_vibrate
    n "I grab it to check the notification, realizing after that I may have moved a little {i}too{/i} quickly to check a dating app message sent at 3 o'clock in the morning."

    notif "You have a new message from [LIName]!"
    li "I set my bag down for two seconds when I was leaving work and a trash panda stole my leftover mac (T.T)"

    mc "No, not the macaroni! But also it's 3am, are you super sad about the macaroni or just can't sleep?"

    li "2 things can be true, I can be super sad about my macaroni while I'm also just leaving work lol"

    mc "At 3am!?!?"

    li "Yeah, I work nights. It's kinda nice being up when everyone else is asleep... It makes work pretty easy but the trade off is that I spend all day sleeping and am basically nocturnal."

    mc "So what I'm hearing is our first date should be a romantic night out, so you can stay awake for it?"

    li "I mean... i'm not upset at that idea ^_^"
    jump dateone_path

label gamersecondchat_path:
    scene black with fade
    pause 0.5
    show text "Home {p}October 26, 2026 {p}18:00" with dissolve
    pause 2.5
    hide text with dissolve


    scene bednight

    n "I'm about to get into bed when my phone buzzes from my nightstand, the dating app's logo visible on the pop-up banner."
    n "I grab it to check the notification, realizing after that I may have moved a little {i}too{/i} quickly to check a dating app message sent at 3 o'clock in the morning."

    notif "You have a new message from [LIName]!"
    
    li "hey hey heeeeyyyy! (:"
    li "how are you? Did you keep playing?"

    mc "Of course I did! And then I got stuck..."
    mc "This puzzle was taking me forever and then I blinked and it was 2am, like.....???"

    li "oh no :c yeah I heard it's a hard game. WE could maybe play it together soon, see if we can figure it out together XD"
    li "actually, I'm off on the 31st owo"
    li "Should we plan something?"

    mc "You have Halloween off?!? Heck yeah!"
    mc "Why don't we go on that night walk we talked about? That would be like the perfect ending to Halloween =D"

    li "oh that's right, it actually is Halloween, isn't it? I take it you like it? Do you dress up?"

    menu:
        "Are you kidding me? I love it! I'm always dressing up and planning next year's costume!":
            li "oh that's awesome! I love it too, i usually go to parties"
        "I think I  like it enough, but I prefer summer stuff more tbh!":
            li "haha its been a while since i've done things in the summer. imo winter is the best - unpopular opinion I know"
        "┐(￣～￣)┌  I guess it's okay, some people do go crazy about it tho":
            li "I know haha, but i'm a big believer in letting people like what they like ¯\_(ツ)_/¯ Halloween can be fun!"

    li "but back to our super spooky nighttime walk plans! There's some nice spots around the area, but we can choose where to go when we get there?"
    li "and maybe snacks? It's a good idea now but it'll be even better with snacks. Maybe some popcorn!!"

    mc "YAASS snacks make everything better!!"
    mc "I can bring something else too, make it a picnic!"

    menu:
        "Maybe some hot chocolate?":
            li "uh yeah, that'd be awesome!"
        "Something sweet? How do we feel about cookies?":
            li "!!!!"
            li "Cookies would go soooooo hard!!"
        "Or maybe you're just satisfied with being in my company? uwu":
            li "hahah yes, yes absolutely, oh queen of England XD"
            mc "hey now hahahaha =P"

    li "amazing, I'm loving this plan already. can't wait to meet you"
    mc "Me neither, I'm excited!"
    mc "Don't forget to bring a jacket too, it's cold out there!"
    li "awww look at you taking care of me already <3"
    mc "heyyy  (ᗒᗣᗕ)՞"
    mc "I can't have my date going hypothermic on me ... on a walk.... at night..."
    mc "that's suspicious AF"
    li "hahah fair"
    li "now go, I've distracted you from your game long enough. Go forth and get those achievements, soldier!"

label dateone_path:

    scene black with fade
    pause 0.5
    show text "Blueberry Acres National Park {p}October 31, 2026 {p}21:00" with dissolve
    pause 2.5
    hide text with dissolve

    scene forest
    play music music_first_date fadein 2.0

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

    scene clearing
    hide LI

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

    hide LI

    scene lake

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

    hide LI

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

    scene black with fade
    pause 0.5
    show text "Facey General Hospital {p}October 31, 2026 {p}23:42" with dissolve
    pause 2.5
    hide text with dissolve
    
    scene hospital with fade
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

    scene black with fade
    pause 0.5
    show text "Home {p}November 1, 2026 {p}11:35" with dissolve
    pause 2.5
    hide text with dissolve
    
    scene apartmentday

    #text exchange
    mc "How are you feeling?"

    li "im okay. a bit sore but i guess that's normal after surviving a wild animal attack."

    n "I roll my eyes and laugh as I read [LIName]'s message."
    mc "I suppose so. It seems like we got you looked after soon enough though, so hopefully it heals quickly!"

    n "The typing notification appears and disappears a few times."

    li "yeah it does."

    mc "Are you sure you're okay?"

    li "ya... i did wanna ask tho, how are you feeling?"

    mc "I'm okay, just worried about you."

    li "awww, thanks <3"
    li "but I guess i mean more like... are you by any chance having any weird symptoms? Stomach upset, headaches...?"

    mc "No... are you? It might just be the adrenaline crash after everything, maybe? Or maybe some of the food was off?"
    mc "Oh god if I gave you food poisoning too..."

    li "No! i'm sure it's just the adrenaline like you said :D i'm just tired, i feel a bit like my muscles are protesting a lot today, and my head hurts but that makes sense after everything i guess"

    mc "I think so too... but please don't ignore them if they don't get better, ok?"

    li "i wont' XD i'm not letting a silly bite ruin everything tho, especially not a chance to see you again if that's cool with you <3"

    mc "Awww... are you asking me out on a second date?"

    li "if you're saying yes, then yes!"
    li "but this time, maybe we do something indoors?"

    n "I laugh as I read their text, and find myself nodding in agreement even though [LIName] can't see me."

    mc "Yeah, that's probably for the best lol"

    n "I move to switch from my messages to my notes app so that I can make a list of snacks to grab before the movie night we just planned."
    n "Except... as I swipe my thumb across the phone screen, I notice a scabbed over cut across the back of my hand, right between my thumb and index finger."
    n "A very uncomfortable memory flashes through my head."
    n "[LIName] bleeding in the park. My own view of my hands trying to help check over their wound."
    n "Their blood on my hands, directly over where the cut now sits."
    n "I can't remember getting it, but it looks recent enough that I can't convince myself that the black hole of anxiety that has bloomed in my gut is unwarranted."
  
return