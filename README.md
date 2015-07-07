# Website Stalker
Schedule watching a website and notify someone when something changes. You could probably use this for any number of things.

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


To load python virtualenv plugin (not neccisary for this but I want to document it somewhere) 
```Import-Module virtualenvwrapper```