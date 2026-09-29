
define playerMsgBox = Frame("images/phone/texts/bubble_mc.png",35,25)
define LIMsgBox = Frame("images/phone/texts/bubble_li.png", 35, 25)
define Msgs = [["","hello hi its me\nmeow"], [".",""],["","howdy"], ["uwu",""]]
define counter = -1
define end = 3
define jumpto = "start"

transform middle:
    zoom 0.9
    xalign 0.5
    yalign 0.2

screen showTextLI(msg, msgs):
    vbox:
        xsize 500
        ysize 300
        at middle
        spacing 10
        yfill False
        vbox:
            spacing 10
            yfill False
            fixed:
                yfill True
            hbox:
                spacing 20
                if msgs[msg][0] == "":
                    xalign 1.0
                    fixed:
                        xfit True
                    frame:
                        background playerMsgBox
                        top_padding 20
                        bottom_padding 25
                        left_padding 20
                        right_padding 20
                        text msgs[msg][1]
                else:
                    xalign 0.0
                    frame:
                        background LIMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg][0]
                    text msgs[msg][1]
            hbox:
                spacing 20
                if msgs[msg+1][0] == "":
                    xalign 1.0
                    fixed:
                        xfit True
                    frame:
                        background playerMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+1][1]
                else:
                    xalign 0.0
                    frame:
                        background LIMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+1][0]
                    text msgs[msg+1][1]
            hbox:
                spacing 20
                if msgs[msg+2][0] == "":
                    xalign 1.0
                    fixed:
                        xfit True
                    frame:
                        background playerMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+2][1]
                else:
                    xalign 0.0
                    frame:
                        background LIMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+2][0]
                    text msgs[msg+2][1]
            hbox:
                spacing 20
                if msgs[msg+3][0] == "":
                    xalign 1.0
                    fixed:
                        xfit True
                    frame:
                        background playerMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+3][1]
                else:
                    xalign 0.0
                    frame:
                        background LIMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+3][0]
                    text msgs[msg+3][1]
            hbox:
                spacing 20
                if msgs[msg+4][0] == "":
                    xalign 1.0
                    fixed:
                        xfit True
                    frame:
                        background playerMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+4][1]
                else:
                    xalign 0.0
                    frame:
                        background LIMsgBox
                        top_padding 20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text msgs[msg+4][0]
                    text msgs[msg+4][1]
        hbox:
            fixed:
                    xfill True
            imagebutton:
                idle "images/phone/profiles/arrow.png"
                hover "images/phone/profiles/arrow_hover.png"
                action [ToggleScreen("showTextLI"),Jump("textConversation")]


label textConversation:
    $ counter = counter + 1
    if counter == end:
        jump expression jumpto
    else:
        call screen showTextLI(counter,Msgs)




