import json

tweetFile = open("tweet_smalls.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

print("tweet text:", tweetData[0]["text"])
