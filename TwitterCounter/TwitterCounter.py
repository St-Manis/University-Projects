import tweepy
import configparser
import sys


# Here is the function of the program. We count the words of the last 50
# tweets of any given account.
def countLetters(user):
    user = user.replace('@', '')
    # We use the API.user_timeline method to fetch the last 50 tweets.
    # We use the extended mode because the text will be limited to a
    # specific number of characters.
    response = API.user_timeline(user, tweet_mode='extended', count=50)

    total_tweets = ''
    # We add all the tweets to a string.
    for k in range(0, 50):
        try:
            total_tweets = total_tweets + \
                           response[k].retweeted_status.full_text
        except AttributeError:
            total_tweets = total_tweets + response[k].full_text

    k += 1

    # Then we count the length of the list, created when we spilt the string
    # containing the tweets into words.
    count = len(total_tweets.split())

    return(count)


print("*****************************************************************\n \
THIS IS A PYTHON PROGRAM THAT TAKES TWO TWITTER PROFILES, AND COUNTS \n\
 THE WORDS THAT ARE PRESENT IN THE LAST 50 POSTS OF EACH. THEN\n IT PRINTS\
 OUT THE PROFILE WITH THE MOST WORDS.\n************************\
***************************************** \n")

# Here we fetch the API keys from the configuration file.
parser = configparser.ConfigParser()
parser.read('config.ini')
public = parser.get('tweeter', 'public')
secret = parser.get('tweeter', 'secret')

if len(public) == 0 or len(secret) == 0:
    print('Consumer keys are not present. Please, proceed to enter your\
 consumer\n keys to the config.ini file and then restart the program.')
    sys.exit()

# We authorize the app using the keys we fetched, and then enstablish a
# connection to the twitter API.
auth = tweepy.OAuthHandler(public, secret)
API = tweepy.API(auth)

user = []
count = []

user.append(input('Give the 1st user name: '))

if user[0].lower == 'exit':
    sys.exit()

count.append(countLetters(user[0]))

user.append(input('Give the 2nd user name: '))

if user[1].lower == 'exit':
    sys.exit()

count.append(countLetters(user[1]))

# Simple if statement to print the account with the more words.
if count[0] > count[1]:
    print('The user with the most words in the last 50 tweets is: '+user[0])
else:
    print('The user with the most words in the last 50 tweets is: '+user[1])
