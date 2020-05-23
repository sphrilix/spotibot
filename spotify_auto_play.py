import sys
from webbot import Browser
from time import sleep

bots = list()
login = list()
song = "https://open.spotify.com/album/1BOGIX0KurYXzUNUKnAWDE"


def read_login():
    global login
    login_file = open("login.txt", "r")
    for x in login_file:
        print(x)
        login.append(x)
    login_file.close()


def create_bots():
    global bots
    global login
    for i in range(len(login)):
        bots.append(Browser())


def login_spotify():
    global bots
    global login
    for i, bot in enumerate(bots):
        login_helper(bot, login[i])


def login_helper(bot: Browser, login_data: str):
    bot.go_to(song)
    sleep(2)
    bot.click(text="ANMELDEN")
    temp = login_data.split(",")
    username = temp[0]
    password = temp[1]
    bot.click(text="ANMELDEN")
    sleep(1)
    bot.type(username, id="login-username")
    bot.type(password, id="login-password")
    bot.press(bot.Key.ENTER)
    sleep(2)


def terminate():
    global bots
    for bot in bots:
        bot.close_current_tab()


def play():
    global bots
    while True:
        for bot in bots:
            bot.click(classname="_11f5fc88e3dec7bfec55f7f49d581d78-scss")
        sleep(90)
        for bot in bots:
            bot.click(classname="spoticon-skip-forward-16")


try:
    read_login()
    create_bots()
    login_spotify()
    play()
except KeyboardInterrupt:
    terminate()
    sys.exit()
