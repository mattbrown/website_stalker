__author__ = 'mbrown'


class SimpleStalker():
    """
    This class does nothing but layout the interface for the stalk classes (so I can test the scheduler)
    Furthermore it allows me to highlight how java-like I write my python code.

    Has the name "simple"
    """
    def __init__(self, stalk_cfg):
        self.cfg = stalk_cfg

    def stalk(self):
        """
        Stalk should return a message if there is something to notify, otherwise it will return None
        """
        return "testing notifications"

    @staticmethod
    def name():
        return "simple"


def get_stalker(stalk_cfg):
    name = stalk_cfg['name']
    if name == SimpleStalker.name():
        return SimpleStalker(stalk_cfg)
    else:
        return SimpleStalker(stalk_cfg)