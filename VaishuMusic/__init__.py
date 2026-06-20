from VaishuMusic.core.bot import Vaishu
from VaishuMusic.core.dir import dirr
from VaishuMusic.core.git import git
from VaishuMusic.core.userbot import Userbot
from VaishuMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Vaishu()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
