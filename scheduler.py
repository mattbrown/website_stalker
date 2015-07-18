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

        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.time = self.cfg['seconds_between_stalks']

    def schedule_stalk(self, in_n_seconds):
        self.scheduler.enter(in_n_seconds, 0, self.do_stalk, ())

    def do_stalk(self):
        result = self.stalker.stalk()
        print "Result of stalk: %s " % result
        if result is not None:
            self.notifier.notify(result)
        self.schedule_stalk(self.time)

    def start(self):
        self.schedule_stalk(0)
        self.scheduler.run()


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