'''
In this program, we will generate a word cloud from tweet data.
For students who finish this part of the program quickly,
they might try it on the larger JSON file to see what clouds they can get.
'''
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


tweetSearch = "automation"

tweetFile = open("tweet_smalls.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
tweetText = ""

for x in tweetData:
    tweetText += x["text"]
print(tweetText)

tweetblob = TextBlob(tweetText)
print(dir(tweetblob))

wordsToFilter = ["about", "https", tweetSearch]
filteredDictionary = dict()

for word in tweetblob.words:
    filteredDictionary[word.lower()] = tweetblob.word_counts[word.lower()]

wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
