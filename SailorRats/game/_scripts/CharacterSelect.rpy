

transform button_cent:
    zoom 1
    xalign 0.5
    yalign 0.5

transform button_right:
    zoom 1
    xalign 0.75
    yalign 0.5

transform button_left:
    zoom 1
    xalign 0.25
    yalign 0.5

screen chooseAmarok():
    imagebutton:
        idle "images/phone/profiles/amarok.png"
        hover "images/phone/profiles/amarok.png"
        action [ToggleScreen("chooseAmarok"), Jump("amarokChosen")]
        at button_cent
    
    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseAmarok"), ToggleScreen("chooseSaja")]
        at button_right
        at transform:
            xzoom -1.0

    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseAmarok"), ToggleScreen("chooseLily")]
        at button_left



label amarokChosen:
    $ LoveInterest = a
    $ LIName = "Amarok"
    $ LIStage = "normal"
    jump startDate1

screen chooseSaja():
    imagebutton:
        idle "images/phone/profiles/saja.png"
        hover "images/phone/profiles/saja.png"
        action [ToggleScreen("chooseSaja"), Jump("sajaChosen")]
        at button_cent
    
    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseSaja"), ToggleScreen("chooseMorrigan")]
        at button_right
        at transform:
            xzoom -1.0

    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseSaja"), ToggleScreen("chooseAmarok")]
        at button_left
        
label sajaChosen:
    $ LoveInterest = s
    $ LIName = "Saja"
    $ LIStage = "normal"
    jump startDate1

screen chooseMorrigan():
    imagebutton:
        idle "images/phone/profiles/morrigan.png"
        hover "images/phone/profiles/morrigan.png"
        action [ToggleScreen("chooseMorrigan"), Jump("morriganChosen")]
        at button_cent
    
    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseMorrigan"), ToggleScreen("chooseLily")]
        at button_right
        at transform:
            xzoom -1.0
    
    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseMorrigan"), ToggleScreen("chooseSaja")]
        at button_left

label morriganChosen:
    $ LoveInterest = m
    $ LIName = "Morrigan"
    $ LIStage = "normal"
    jump startDate1

screen chooseLily():
    imagebutton:
        idle "images/phone/profiles/lily.png"
        hover "images/phone/profiles/lily.png"
        action [ToggleScreen("chooseLily"), Jump("lilyChosen")]
        at button_cent
    
    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseLily"), ToggleScreen("chooseMorrigan")]
        at button_right
        at transform:
            xzoom -1.0
    
    imagebutton:
        idle "images/phone/profiles/arrow.png"
        hover "images/phone/profiles/arrow_hover.png"
        action [ToggleScreen("chooseLily"), ToggleScreen("chooseAmarok")]
        at button_left

label lilyChosen:
    $ LoveInterest = l
    $ LIName = "Lily"
    $ LIStage = "normal"
    jump startDate1
