# website_stalker
Watch a website to stalk its current status

To run:
``` python scheduler.py```

Requires a config file called "config.yml" in the root directory. An example:
```
scheduler:
    seconds_between_stalks: 10
stalker:
    name: simple
    #Stalker specific config. Login info and urls go here
notifier:
    name: print
    #Notifier specific config. Things like emails, credentials, etc go here.
```
