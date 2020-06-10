from spotibotPackage.account_handler import AccountHandler
from spotibotPackage.spotibot import Spotibot
import sys
import pyinputplus as pyip

# Implementation of Shell which interacts with the user
class Shell:

    # List of the bots/threads
    threads = []

    # Method which manage the account delivery to the correct bot and starts them
    def start_bots(self, time_to_play: int, tolerance: int, song: str, threads: int):
        acc_handler = AccountHandler()
        splited_acc_data = acc_handler.get_accounts(threads)
        print(splited_acc_data)
        counter = 0
        for acc_data in splited_acc_data:
            self.threads.append(Spotibot(acc_data, song, counter, time_to_play, tolerance))
            counter += 1
        for thread in self.threads:
            thread.start()

    # Main method of the program which collects the input from the user
    def main(self):
        print("____Hello, i'm here to serve you with streams!____")
        threads = pyip.inputNum("Please enter how much bots should run (must be smaller then amount of accounts!): ")
        song_url = pyip.inputURL("Please enter the URL of your song: ")
        song_play_time = pyip.inputNum("Please enter the play time (must be smaller then the length of the song): ")
        song_play_tolerance = \
            pyip.inputNum("Please enter the tolerance of play time (must be smaller then play time): ")
        self.start_bots(song_play_time, song_play_tolerance, song_url, threads)
        if pyip.inputYesNo("End Program: ") == "yes":
            self.terminate()

    # Method to terminate the bots
    def terminate(self):
        print("Thank you for using Spotibot!")
        for thread in self.threads:
            thread.terminate()
        sys.exit()


# Start the Spotibot by creating an instance of Shell
shell = Shell()
shell.main()
