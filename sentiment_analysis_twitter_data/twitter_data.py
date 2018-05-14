import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

# TODO: complete this as your requirements
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('first step')
    acct = input('Plese enter twitter account: ')
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {'screen_name' : acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:100])
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
