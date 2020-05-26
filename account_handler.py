# This class provides the implementation af "account handler", which reads the accounts out from a .txt file and splits
# them according for the given threads (in each a bot is running).
class AccountHandler:

    # Path of the file with the accounts
    FILE = "login.txt"

    # List of the splitted accounts for the bots/threads
    separate_acc_for_threads: []

    # Init the AccountHandler
    def __init__(self):
        self.separate_accounts_for_threads = []

    # Read the accounts from the file split them and return them
    def get_accounts(self, threads: int = 4):
        t = threads
        acc_file = open(self.FILE, "r")
        self.split_for_bots(acc_file.readlines(), threads)
        return self.separate_accounts_for_threads

    # Recursively split up the accounts according to threads/bots
    def split_for_bots(self, accounts: [], threads: int):
        if threads > 1:
            middle = len(accounts) // 2
            self.split_for_bots(accounts[:middle], threads // 2)
            self.split_for_bots(accounts[middle:], threads // 2)
        else:
            self.separate_accounts_for_threads.append(accounts)
