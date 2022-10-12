import tweepy
 
# API keyws that yous saved earlier
api_key = "QIVXV9UanwmGCRSHnXeIpi5ai"
api_secrets = "ALxjtBaITyu4opjfZU5daBnn977dqRjIXG5Bh84LNBqyY3MKXA"
access_token = "1348308906347438082-tgIyI0sNdj3bK7baOZDxTLL2DeQb3U"
access_secret = "p2VNbdxWsMpJnlrLM2YS0y3fXHEBpQIWEGT6w5LVVOeyX"
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')