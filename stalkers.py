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


class DisneyRestaurantsStalker():
    """
    Stalk a list of restaurants for a particular date. Notify if there's a NEW value since the last check.

    Has the name "disney_restaurant"
    """
    def __init__(self, stalk_cfg):
        self.cfg = stalk_cfg
        self.urls = self.cfg['urls']

    def stalk(self):
        """
        Stalk should return a message if there is something to notify, otherwise it will return None
        """
        return "testing notifications"

    @staticmethod
    def name():
        return "disney_restaurant"


def get_stalker(stalk_cfg):
    name = stalk_cfg['name']
    if name == SimpleStalker.name():
        return SimpleStalker(stalk_cfg)
    else:
        return SimpleStalker(stalk_cfg)