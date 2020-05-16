# Beatrice-Chan
![Avatar](https://static.myfigurecollection.net/pics/figure/big/436644.jpg)


[![Python3](https://img.shields.io/badge/python-3.7-blue.svg)](https://github.com/Jade9ja/AspiritusDiscord)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Jade9ja/AspiritusDiscord/blob/master/LICENSE)

This bot uses the new version of [discord.py v1.0+](https://github.com/Rapptz/discord.py/tree/rewrite)
Will add more features as I discover stuff.Basic functionality (kick,ban,unban etc.) and an anime function for getting info about anime is currently added.

# Using `pip install discord.py` will install the latest discord.py version. 
Install all requirements and run the main.py script on the server of your choice.

Full list of requirements
-------------

    python>=3.6.0
    discord.py>=1.3.0
    aiohttp
    websockets
    chardet
    pytz

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
