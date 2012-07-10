This is a bit of code that bot makers using Python (myself included) can fork off to use as a template for making bots for [turntable.](http://turntable.fm)

## Instructions

### Step 1

The first thing you will need is a new bot account (unless you plan to bot yourself in which case, you cannot be logged into both at the same time). Go ahead and make one right now and continue to Step 2 when you're done.

### Step 2

Now, go to the page for [this bookmarklet](http://alaingilbert.github.com/Turntable-API/bookmarklet.html) and drag that nice little green button to your bookmarks toolbar (or alternatively copy the javascript code and paste it later). (Don't worry, you can delete the bookmarklet later. Now log in as your bot (or yourself if you chose to bot yourself) and browse to the room that the bot will reside in. Click that bookmarklet in your toolbar and you should see a little window pop up. Copy down everything in that window. Click the toolbar link again to close it.

### Step 3

After you have cloned or downloaded the git, edit your code and paste the values that you copied down earlier. 

Your code should now look like this:

```python
bot_auth       = 'auth+livexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # LINE 14
bot_userid     = '4fxxxxxxxxxxxxxxxxxxxxxx'

lsk_userid     = '4e7c70bc4fe7d052ef034402' #The userid in here is in control of the bot. Rename the variable name if you wish.

AUTH   = bot_auth
USERID = bot_userid
ROOM   = 'xxxxxxxxxxxxxxxxxxxxxxxx'

bot = Bot(AUTH,USERID,ROOM)
```

### Step 4

Customize the code to your liking and run!