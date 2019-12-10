# [+]----------------------------------------[+]
# |            github.com/Inf3xted            |
# |              Inf3xted is BAE              |
# |           Credit me or you gay            |
# |   Will be making a script to auto install |
# [-]-----------------------------------------[-]



import os
import tweepy
from time import sleep
from os import system, name

if name == 'nt':
    os.system('cls')
else:
    os.system('clear')

auth = tweepy.OAuthHandler("PUT API KEY HERE","PUT SECRET API KEY HERE") # Key and private key in order of key > private
auth.set_access_token("PUT THE ACCESS TOKEN HERE AND INCLUDE THE -","PUT THE SECRET ACCESS TOKEN HERE") # Access token and secret access token in order of access token > secret access set_access_token
api = tweepy.API(auth)
print("Time to Tweet the message!")
print("Twitter for?")
tweet = input("Create the Tweet here:\n")
print("Sleeping for 5 seconds...")
sleep(5)
api.update_status(status=(tweet))
print("Done! Please refresh the page now!")
print("https://github.com/Inf3xted")
