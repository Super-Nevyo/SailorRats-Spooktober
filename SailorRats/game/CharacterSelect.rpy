

transform button_cent:
    zoom 0.2
    xalign 0.5
    yalign 0.5

transform button_right:
    zoom 0.2
    xalign 0.75
    yalign 0.5

transform button_left:
    zoom 0.2
    xalign 0.25
    yalign 0.5

screen chooseAmarok():
    imagebutton:
        idle "images/characters/amarok/normal/neutral.png"
        hover "images/characters/amarok/normal/happy.png"
        action [ToggleScreen("chooseAmarok"), Jump("amarokChosen")]
        at button_cent
    
    imagebutton:
        idle "images/characters/saja/normal/neutral.png"
        hover "images/characters/saja/normal/happy.png"
        action [ToggleScreen("chooseAmarok"), ToggleScreen("chooseSaja")]
        at button_right

    imagebutton:
        idle "images/characters/saja/chihuahua/angry.png"
        hover "images/characters/saja/chihuahua/happy.png"
        action [ToggleScreen("chooseAmarok"), ToggleScreen("choosePuppy")]
        at button_left

label amarokChosen:
    $ LoveInterest = a
    $ LIName = "Amarok"
    $ LIStage = "normal"
    jump startDate1

screen chooseSaja():
    imagebutton:
        idle "images/characters/saja/normal/neutral.png"
        hover "images/characters/saja/normal/happy.png"
        action [ToggleScreen("chooseSaja"), Jump("sajaChosen")]
        at button_cent
    
    imagebutton:
        idle "images/characters/saja/chihuahua/angry.png"
        hover "images/characters/saja/chihuahua/happy.png"
        action [ToggleScreen("chooseSaja"), ToggleScreen("choosePuppy")]
        at button_right

    imagebutton:
        idle "images/characters/amarok/normal/neutral.png"
        hover "images/characters/amarok/normal/happy.png"
        action [ToggleScreen("chooseSaja"), ToggleScreen("chooseAmarok")]
        at button_left
        
label sajaChosen:
    $ LoveInterest = s
    $ LIName = "Saja"
    $ LIStage = "normal"
    jump startDate1

screen choosePuppy():
    imagebutton:
        idle "images/characters/saja/chihuahua/angry.png"
        hover "images/characters/saja/chihuahua/happy.png"
        action [ToggleScreen("choosePuppy"), Jump("chihuahuaChosen")]
        at button_cent
    
    imagebutton:
        idle "images/characters/amarok/normal/neutral.png"
        hover "images/characters/amarok/normal/happy.png"
        action [ToggleScreen("choosePuppy"), ToggleScreen("chooseAmarok")]
        at button_right
    
    imagebutton:
        idle "images/characters/saja/normal/neutral.png"
        hover "images/characters/saja/normal/happy.png"
        action [ToggleScreen("choosePuppy"), ToggleScreen("chooseSaja")]
        at button_left

label chihuahuaChosen:
    $ LoveInterest = s
    $ LIName = "saja"
    $ LIStage = "chihuahua"
    jump startDate1
