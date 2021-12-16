import tweepy
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("","")
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="username")

def stringAlt(text):
    new = []
    for x in range(0,len(text)-1):
        if x%2 == 0:
            new.append(text[x].lower())
        new.append(text[x].upper())    
    return ''.join(new)

print(stringAlt(tweets[3].text))
