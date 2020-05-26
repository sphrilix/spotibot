from account_handler import AccountHandler
from spotibot import Spotibot
import sys
import pyinputplus as pyip

class Shell:
    threads = []

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

    def terminate(self):
        for thread in self.threads:
            thread.join()
        print("Thanks for using spotibot")
        sys.exit()

    def main(self):
        print("____Hello, i'm here to serve you with streams!____")
        threads = pyip.inputNum("Please enter how much bots should run (must be smaller then amount of accounts!): ")
        song_url = pyip.inputURL("Please enter the URL of your song: ")
        song_play_time = pyip.inputNum("Please enter the play time (must be smaller then the length of the song): ")
        song_play_tolerance = \
            pyip.inputNum("Please enter the tolerance of play time (must be smaller then play time): ")
        self.start_bots(song_play_time, song_play_tolerance, song_url, threads)
        if pyip.inputYesNo("End Program: ") is "yes":
            print("Yes")
            self.terminate()

        print(song_url)
        print(threads)
        print(song_play_time)
        print(song_play_tolerance)



shell = Shell()
shell.main()
