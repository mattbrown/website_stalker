__author__ = 'mbrown'

import sched
import time
import notification
import stalkers
import yaml
from pprint import pprint


class StalkScheduler():
    """
    This is a wrapper for the stalking activity. It will schedule scans and hold
    the notification object.
    """
    def __init__(self, cfg, notifier, stalker):
        self.cfg = cfg
        self.notifier = notifier
        self.stalker = stalker

    def start(self):
        print "Scheduler cfg: %s" % self.cfg


def main():
    """
    Pulls a config file called "config.yml" from the current directory. An example:
    scheduler:
      seconds_between_stalks: 10
    stalker:
        name: simple
        #Stalker specific config. Login info and urls go here
    notifier:
        name: print
        #Notifier specific config. Things like emails, credentials, etc go here.
    """
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    notifier_cfg = cfg['notifier']
    stalker_cfg = cfg['stalker']
    scheduler_cfg = cfg['scheduler']

    notifier = notification.get_notifier(notifier_cfg)
    stalker = stalkers.get_stalker(stalker_cfg)
    scheduler = StalkScheduler(scheduler_cfg, notifier, stalker)

    notifier.notify("Starting %s stalking" % stalker.name())
    scheduler.start()



if __name__ == "__main__":
    main()