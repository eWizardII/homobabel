import tweepy
import time
CONSUMER_KEY    = '3y1428CJNYI3uqgW8oFcEA'
CONSUMER_SECRET = 'GPpj8e6jOVkecaxfb5GmgIvI8ObnqYzo80oXt8v3c'

oauth_token = '125084643-wMo7a0iWfzlfD8jPkoroO2tvanGDKB2JvTb8E55K'
oauth_token_secret = 'lRZihmhxheqp9WiE3X1gxUOOyniIviTQdpMPRY0rI'

auth            = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(oauth_token, oauth_token_secret)
api             = tweepy.API(auth)

api_name = "1"
##for goat in range(0,11):
api.proxy_host  = 'twitter' + str(api_name) + '-ewizardii.apigee.com'
print api.rate_limit_status()['remaining_hits']
print api.rate_limit_status()['reset_time']

oauth_token = "223931724-7cxcQU2Y9yboX2FBfHubzJYO4K46BLYPldMcUnKO"
oauth_token_secret = "GIJumtp5sMRbSxaEBRAsaeBbPOHUXmmapurWsllALM"

auth            = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(oauth_token, oauth_token_secret)
api             = tweepy.API(auth)

api.proxy_host  = 'twitter' + str(api_name) + '-ewizardii.apigee.com'
print api.rate_limit_status()['remaining_hits']

oauth_token = "227198492-FAJ37zSH6DULRGG7KgXpplpHXQznMPWlLDAGaiNz"
oauth_token_secret = "Y0T3PMYIsRE1fo9kIYpQ3qNqT9kNxJ81xAfqkwUnro"

auth            = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(oauth_token, oauth_token_secret)
api             = tweepy.API(auth)

api.proxy_host  = 'twitter' + str(api_name) + '-ewizardii.apigee.com'
print api.rate_limit_status()['remaining_hits']


