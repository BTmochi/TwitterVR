#!usrbinenv python3
# -- coding utf-8 --

import codecs
import json
from os import path as ospath
import re
import subprocess
import tweepy

fpath = '{0}Config.json'.format(ospath.dirname(ospath.abspath(__file__)))
if ospath.exists(fpath)
    fp = codecs.open(fpath, 'r', 'utf-8')
    conf = json.load(fp)
    fp.close()
else
    # Initial setting
    PATH_VRX = input('Drag and Drop vrx.exe  ')
    PATH_VOICEROID = input('Drag and Drop VOICEROID.exe  ')
    CK = input(Input Consumer Key (API Key)  )
    CS = input(Input Consumer Secret (API Secret)  )
    AT = input(Input Access Token  )
    AS = input(Input Access Token Secret  )
    conf = {'path' {'vrx' PATH_VRX, 'voiceroid' PATH_VOICEROID},
            'api' {'ck' CK, 'cs' CS, 'at' AT, 'as' AS}}
    # Save to Config.json
    fp = codecs.open(fpath, 'w', 'utf-8')
    json.dump(conf, fp, indent=4)
    fp.close()

pvr = subprocess.Popen(conf['path']['voiceroid'])
pvrx = subprocess.Popen(conf['path']['vrx'])

auth = tweepy.OAuthHandler(conf['api']['ck'], conf['api']['cs'])
auth.set_access_token(conf['api']['at'], conf['api']['as'])
api = tweepy.API(auth)

class Listener(tweepy.StreamListener)

    def on_status(self, status)
        try
            for word in conf['NG']['word']
                if status.text.find(word) != -1
                    return True
        except KeyError
            pass
        try
            if status.source in conf['NG']['client']
                return True
        except KeyError
            pass
        try
            if status.user.id in conf['NG']['user_id']
                return True
        except KeyError
            pass
        try
            if status.user.screen_name in conf['NG']['user_screen_name']
                return True
        except KeyError
            pass
        try
            for retxt in conf['re']
                status.text = re.sub(retxt, conf['re'][retxt], status.text)
        except KeyError
            pass
        cmd = {0} {1}さんのつぶやき。{2}.format(
            conf['path']['vrx'], status.user.name, status.text)
        subprocess.call(cmd)
        return True

listener = Listener()
stream = tweepy.Stream(auth, listener)
try
    stream.userstream()
except
    pvr.kill()
    pvrx.kill()