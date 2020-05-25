# DisPybot
![Avatar](https://github.com/Jade9ja/AspiritusDiscord/blob/master/img/projecticon.jpg?raw=true)

[![Python3](https://img.shields.io/badge/python-3.7-blue.svg)](https://github.com/Jade9ja/AspiritusDiscord)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Jade9ja/AspiritusDiscord/blob/master/LICENSE)

This bot uses the new version of [discord.py v1.0+](https://github.com/Rapptz/discord.py/tree/rewrite).  The docs are available [here](https://discordpy.readthedocs.io/en/latest/)
More features will be added in time.

Using `pip install discord.py` will install the latest discord.py version.

# Installation:
1) Clone the repo to your machine and get your bot token (after creating one [here](https://discordapp.com/developers/applications/me)) , you can refer to [this](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) tutorial here.
2) Edit the "token" value in config.json to your own bot token which you got in step 1.
3) In a shell/terminal (as an administrator/sudo) run `pip install -r requirements.txt` or `python -m pip install -r requirements.txt`
4) Start the bot by running the main.py script. `python main.py`
5) Give yourself a pat on the back! :P

# Admin 

Command and Aliases | Description | Example
----------------|--------------|-------
`/purge <x>` | Deletes <x> amount of messages. | `/purge 100`
`/kick <usertag> <reason>` | Kicks the user in question.(Optional reason can be specified) | `/kick @kickmeuwu`, `/kick @kickmeuwu Spammer`
`/ban <usertag> <reason>` | Bans the user in question. (Optional reason can be specified)| `/ban @banmeuwu`, `/ban @banmeuwu Spammer`
`/unban <username#discriptor>` | Unbans the user in question. | `/unban unbanmeuwu#1234`
`/setrank <usertag> <role>`| Sets a role for the user. | `/setrole @Gimmerole Member`
`/rmrank <usertag> <role>`| Removes a role from a user. | `/rmrole @takemyrole Member`
  
 # Anime
  Command and Aliases | Description | Example
----------------|--------------|-------
`/anime <x>` | Search for the anime x. | `/anime naruto`
`/manga <x>` | Search for the manga x. | `/manga mushishi`
`/character <x>` | Search for the character x.| `/character nepgear`
`/upcoming` | Top upcoming anime this season. | `/upcoming`

# Sauce
  Command and Aliases | Description | Example
----------------|--------------|-------
`/sauce <image url>` | Try to find the anime to which the image in question belongs to.(jpg,png,gif supported) | `/sauce https://somerubbish.com/naruto.jpg`

# Translate
  Command and Aliases | Description | Example
----------------|--------------|-------
`/tlate <language code (iso639-1)> <query>` | Translate query to the required language. | `/tlate en 안녕하세요`
`/dtect <query>` | Detect the language of the query. | `/dtect 안녕하세요`

# Has more features,I need to update this readme.
  Also has a fun module,bot management commands and utility commands.


License
-------------
    MIT License

    Copyright (c) 2016 Eduard Nikoleisen

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
# Thanks to
[Rapptz(Danny)](https://github.com/Rapptz) for discord.py wrapper,[abhinavk99](https://github.com/abhinavk99) for Jikan.py wrapper,Trace.moe API (used in sauce module),Google for google translate and everyone else whom I forgot to mention here.
