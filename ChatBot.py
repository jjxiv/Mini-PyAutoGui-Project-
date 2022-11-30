import pyautogui
import pyclip
import time
import random

time.sleep(3)
print(pyautogui.position())

"""
getMessage():
- gets the message from the browser and copies
to the clipboard to be processed during
the program
"""
def getMessage():
    # clicks the current message
    pyautogui.dragTo(485,904)
    pyautogui.tripleClick()

    # ctrl + c -> copy using keyboard shortcut
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

    # gets the latest copied text from chatbox
    message = pyclip.paste()
    message = str(message)
    message = message[2:-5].lower()

    #returns the string to be checked
    return message

def sendMessage():
    condition = True
    greet= ["hello","henlo","hi","hey","yo","hawu", "hello kuya!", "hello doi"]
    ask = ["sup","wassap","wyd","ano gawa mo",
           "nu gawa niyo", "ngm", "wachudo", "ano gawa"]
    reply = ["oke ","oki", "ah okeh", "ah okay", "okay", "k",
             "kay", "oks", "ocakes"]
    askResponse = ["eto lalaro lang valorant, hbu?",
                  "kumakain rn, taraa kainnn ",
                  "nakahiga inaantok na ako gRabEEE",
                  "mag-ggym kasi i feel fat damn",
                  "nagugutom and waiting for dinner",
                   "nag aaral and tambak sa gagawin", ]
    end = ["babye","bye","sige!","okay","ok","good night!",
           "sigi bye", "sige bye", "paalam!"]

    while condition:
        # checks if getMessage is blank or not
        if len(getMessage()) > 0:

            # replies a proper message if in greetings
            if getMessage() in greet:
                pyautogui.moveTo(480, 974)
                pyautogui.leftClick()
                pyautogui.write(greet[random.randint(0,len(greet)-1)])
                pyautogui.press('enter')

            # replies a proper message if someone is asking
            elif getMessage() in ask:
                pyautogui.moveTo(480, 974)
                pyautogui.leftClick()
                pyautogui.write(askResponse[random.randint(0,4)])
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.write("hbu?")
                pyautogui.press('enter')
                time.sleep(8)
                getMessage()
                if len(getMessage()) > 0:
                    pyautogui.moveTo(480, 974)
                    pyautogui.leftClick()
                    pyautogui.write(reply[random.randint(0,len(reply)-1)])
                    pyautogui.press('enter')


            # replies a proper message if someone is saying good bye
            elif getMessage() in end:
                pyautogui.moveTo(480, 974)
                pyautogui.leftClick()
                pyautogui.write(end[random.randint(0,len(end)-1)])
                pyautogui.press('enter')
                condition = False

            # replies a proper message if the chat bot does not understand
            else:
                pyautogui.moveTo(480, 974)
                pyautogui.leftClick()
                pyautogui.write("Im sorry I dont understand")
                pyautogui.press('enter')
            time.sleep(8)
            getMessage()

        #exits the program when there is no message
        else:
            condition = False

sendMessage()
