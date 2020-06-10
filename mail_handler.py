from webbot import Browser
import requests
import json
import re
import random


class MailHandler:
    URL_REG = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+"
                         + r"|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)"
                         + r"|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")

    EMAIL_API = "https://www.1secmail.com/api/v1/?action=%s&login=%s&domain=1secmail.com%s"

    EMAIL_FROM = "guerrillamail"

    EMAIL_DOMAIN = "@1secmail.com"

    def __init__(self, forename: str, last_name: str):
        self.forename = forename
        self.last_name = last_name
        self.mail = self.create_mail()

    def get_mail(self):
        return self.mail

    def create_mail(self):
        rand_number = ""
        for i in range(random.randint(5, 10)):
            rand_number = rand_number + str(random.randint(0, 9))
        return self.forename[:random.randint(0, len(self.forename))] \
               + self.last_name[:random.randint(0, len(self.last_name))] \
               + rand_number + MailHandler.EMAIL_DOMAIN

    def check_inbox(self, sent_from: str):
        local = self.mail[:self.mail.index("@")]
        response = requests.get(self.EMAIL_API % ("getMessages", local, ""))
        inbox = json.loads(response.content.decode("utf-8"))
        searched_id = -1
        for i in range(len(inbox)):
            print(inbox[i]["from"])
            if sent_from in inbox[i]["from"]:
                searched_id = inbox[i]["id"]
                break
        print(searched_id)
        return searched_id
        #if searched_id is not -1:
        #    print(self.get_auth_link(self.get_message_content(searched_id)))

    def get_message_content(self, message_id: int):
        local = self.mail[:self.mail.index("@")]
        response = requests.get(self.EMAIL_API % ("readMessage", local, "&id=" + str(message_id)))
        message_data = json.loads(response.content.decode("utf-8"))
        return message_data["body"]

    def get_auth_link(self, sent_from: str):
        message_id = self.check_inbox(sent_from)
        if message_id > -1:
            message = self.get_message_content(message_id)
            return re.search(self.URL_REG, message).group()

    def to_string(self):
        return self.forename + ", " + self.last_name + "\nEmail: " + self.mail + "\n\n"


mh = MailHandler("bernd", "huber")
print(mh.to_string())
