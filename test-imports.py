from lib.regexes import regexes
from lib.Pastebin import Pastebin, PastebinPaste
from lib.Slexy import Slexy, SlexyPaste
from lib.Pastie import Pastie, PastiePaste
from lib.helper import log
from time import sleep
from twitter import Twitter, OAuth
from lib.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, log_file
import threading
import logging