__author__ = 'mbrown'


class PrintNotifier():
    def __init__(self, cfg):
        self.cfg = cfg

    def notify(self, msg):
        print("THIS IS A NOTIFICATION: %s. \n\tI have cfg %s" % (msg, self.cfg))

    @staticmethod
    def name():
        return "print"


def get_notifier(cfg):
    name = cfg['name']
    if name == PrintNotifier.name():
        return PrintNotifier(cfg)
    else:
        return PrintNotifier(cfg)