import urllib2
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u", "--user", dest="username",
                  help="Your twitch.tv username.")
(options, args) = parser.parse_args()

url = 'https://api.twitch.tv/kraken/users/%s/follows/channels?limit=100' % \
      options.username
follows = json.load(urllib2.urlopen(url))
streamers = ''
for val in follows['follows']:
    streamers = streamers+val['channel']['name'] + ','
url = 'https://api.twitch.tv/kraken/streams?channel=%s' % streamers
live = json.load(urllib2.urlopen(url))
for val in live['streams']:
    print val['channel']['name'] + ' - ' + val['channel']['status']
