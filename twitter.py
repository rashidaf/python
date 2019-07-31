
'''

In this project, you will visualize the feelings and language used in a set of

Tweets. This starter code loads the appropriate libraries and the Twitter data you'll

need!

'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt



#Get the JSON data

tweetFile = open("tweet_smalls.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()



# Continue your program below!

pol = []
sub = []

for x in range(len(tweetData)):
    tweet_text = tweetData[x]["text"]
    tb = TextBlob(tweet_text)
    # print(tb.polarity)
    pol.append(tb.polarity)
    # print(tb.subjectivity)
    sub.append(tb.subjectivity)

total = 0

for i in range(len(pol)):
    total = total + pol[i]

avg = total/(len(pol))
print(avg)

total = 0

for i in range(len(sub)):
    total = total + sub[i]

avg = total/(len(sub))
print(avg)


plt.hist(pol,5, histtype='bar',
align='mid', color='c', label='Polarity',edgecolor='black')
plt.legend()
plt.title('Polarity Graph')
plt.show()

plt.hist(sub,5, histtype='bar',
align='mid', color='c', label='Subjectivity',edgecolor='black')
plt.legend()
plt.title('Subjectivity Graph')
plt.show()
