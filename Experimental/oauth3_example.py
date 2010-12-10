import oauth2 as oauth
import time

# Set the API endpoint 
url = "http://twitter1-ewizardii.apigee.com/1/statuses/public_timeline.json"
PROXY_DOMAIN = "twitter1-ewizardii.apigee.com"

# Set the base oauth_* parameters along with any other parameters required
# for the API call.
params = {
    'oauth_version': "1.0",
    'oauth_nonce': oauth.generate_nonce(),
    'oauth_timestamp': int(time.time())
##    'user': 'joestump',
##    'photoid': 555555555555
}

# Set up instances of our Token and Consumer. The Consumer.key and 
# Consumer.secret are given to you by the API provider. The Token.key and
# Token.secret is given to you after a three-legged authentication.
token = oauth.Token(key="TVjUUCHjcjRAQBzxNeqevQ", secret="uDs577RFeCePYEGnFSw0npvPuT6waStSO8UNz6L4")
consumer = oauth.Consumer(key="223931724-D3vxyHDuUKqphGIYT3roROzheQhFCvWPI3jnsyTX", secret="Mno2DPUBvVOJHwUna0j49p111sJSOgDzKCRZoQx3c")

# Set our token/key parameters
params['oauth_token'] = token.key
params['oauth_consumer_key'] = consumer.key

# Create our request. Change method, etc. accordingly.
req = oauth.Request(method="GET", url=url, parameters=params)

# Sign the request.
signature_method = oauth.SignatureMethod_HMAC_SHA1()
req.sign_request(signature_method, consumer, token)
##print req

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key="TVjUUCHjcjRAQBzxNeqevQ", 
    secret="uDs577RFeCePYEGnFSw0npvPuT6waStSO8UNz6L4")

# Request token URL for Twitter.
request_token_url = "http://twitter.com/oauth/request_token"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
# Optional use with a proxy:
resp, content = client.request(request_token_url, "GET", PROXY_DOMAIN)
#resp, content = client.request(request_token_url, "GET")
print resp
print content
