import urlparse
import oauth2 as oauth

PROXY_DOMAIN = "twitter1-ewizardii.apigee.com"
consumer_key = 'TVjUUCHjcjRAQBzxNeqevQ'
consumer_secret = 'uDs577RFeCePYEGnFSw0npvPuT6waStSO8UNz6L4'
consumer = oauth.Consumer(consumer_key, consumer_secret)

oauth_token = '125084643-t7NLHdd22fxrbQAqjZklaJIYkHhBadzIjhxPwHtp'
oauth_token_secret = '9Trtl2zu0Zxx320InBzwYSUlDoFAVZjy1TmhvwlhZQ'

'''homobabel1'''
##oauth_token = '223931724-D3vxyHDuUKqphGIYT3roROzheQhFCvWPI3jnsyTX'
##oauth_token_secret = 'Mno2DPUBvVOJHwUna0j49p111sJSOgDzKCRZoQx3c'

'''wandera89'''
##oauth_token = '120020249-8u2T0tzEXFuQeGOdZc3Yb0kFe3Oqxl901WFxczdj'
##oauth_token_secret = 'M9QoE6jtI63Y1Z9q0ix2OsqRLhdlJ9STzO6Pqnxjvc'

token = oauth.Token(oauth_token, oauth_token_secret)
client = oauth.Client(consumer, token)

request_token_url = "http://twitter2-ewizardii.apigee.com/1/account/rate_limit_status.json"
resp, content = client.request(request_token_url, "GET", PROXY_DOMAIN)
print resp
print content
