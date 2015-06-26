__author__ = 'mbrown'

import yaml
from twilio.rest import TwilioRestClient


class PrintNotifier():
    def __init__(self, cfg):
        self.cfg = cfg

    def notify(self, msg):
        print("THIS IS A NOTIFICATION: %s. \n\tI have cfg %s" % (msg, self.cfg))

    @staticmethod
    def name():
        return "print"


class TwilioNotifier():
    def __init__(self, cfg):
        self.cfg = cfg
        self.client = TwilioRestClient(cfg['account_sid'], cfg['auth_token'])
        self.to_num = cfg['to_num']
        self.from_num = cfg['from_num']

    def notify(self, msg):
        print "\t About to text message: %s" % msg
        self.client.messages.create(
            to=self.to_num,
            from_=self.from_num,
            body=str(msg)
        )

    @staticmethod
    def name():
        return "twilio"


def get_notifier(cfg):
    name = cfg['name']
    if name == PrintNotifier.name():
        return PrintNotifier(cfg)
    if name == TwilioNotifier.name():
        return TwilioNotifier(cfg)
    else:
        return PrintNotifier(cfg)

if __name__ == "__main__":
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    notifier_cfg = cfg['notifier']
    notifier = TwilioNotifier(notifier_cfg)

    notifier.notify("bippity boppity boo")
