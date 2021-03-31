from twython import Twython
from bitcoin import price

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "#Bitcoin is currently $" + price
twitter.update_status(status=message)
print("Tweeted: {}".format(message))
