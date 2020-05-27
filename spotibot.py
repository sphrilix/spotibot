from webbot import Browser
from time import sleep
import random
import threading
import sys


# This class provides the implementation of a stream bot for Spotify, by implementing each bot in a separate thread (to
# increase efficiency). Each bot is given a list of accounts to use for streaming. The bot plays the given song for a
# given time, a bit randomly to pretend some human like behaviour, then switching the account and so on.
class Spotibot(threading.Thread):

    # List of accounts the bot can use
    accounts: []

    # URL of the song to be played
    song: str

    # The player which open a browser window
    player: Browser

    # Time how long the song should be played in average in seconds
    time_to_play: int

    # Time of the tolerance in seconds (needed for human like behaviour)
    tolerance: int

    # Id of the bot
    bot_id: int

    # Init of the bot by setting the parameters of the bot
    def __init__(self, accounts: [], song: str, bot_id: int, time_to_play: int, tolerance: int):
        threading.Thread.__init__(self)
        self.player = Browser()
        self.song = song
        self.accounts = accounts
        self.bot_id = bot_id
        self.time_to_play = time_to_play
        self.tolerance = tolerance
        self.daemon = True

    # Run method which executes if the Thread is getting started
    def run(self):
        self.play()

    # While bot is active concurrently login, play and logout with the given accounts
    def play(self):
        current_player = self.player
        while True:
            for acc in self.accounts:
                self.login(acc)

                # Press "play"
                #current_player.click(classname="_11f5fc88e3dec7bfec55f7f49d581d78-scss")

                # Play song for a calculated time
                sleep(self.play_like_a_human(self.time_to_play, self.tolerance))
                self.logout()

    # Login to a given Spotify account
    def login(self, login_data: str):
        username = login_data.split(",")[0]
        password = login_data.split(",")[1]
        current_player = self.player
        current_player.go_to(self.song)
        sleep(2)
        current_player.click(text="ANMELDEN")
        sleep(2)
        current_player.type(username, id="login-username")
        current_player.type(password, id="login-password")
        sleep(2)
        current_player.press(current_player.Key.ENTER)
        sleep(2)

    # Logout from the current account
    def logout(self):
        current_player = self.player
        current_player.click(classname="_34098cfd13d48e2910679f35aea2c377-scss")
        sleep(2)
        current_player.click(text="Abmelden")
        sleep(2)

    # Calculate a random time in seconds for a given time with a given tolerance
    def play_like_a_human(self, time_to_play: int, tolerance: int):
        return random.randint(time_to_play - tolerance, time_to_play + tolerance)

    # Close the current tab
    def terminate(self):
        self.player.close_current_tab()
