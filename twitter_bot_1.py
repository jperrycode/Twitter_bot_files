#
#       Twitter Bot Innitial File __MAIN__
#       Shat My Jeans and J Boogawitz
#
#       Goal:  Build a twitter bot to scrape news sources on the web for 
#               the point of trolling corrupt politicians/men in power
#
#
#
#

import tweepy
import json





def welcome():
    initialize_1 = input("Please connect to twitter API-- Y/N \n >>")
    if initialize_1 == 'y':
        print('you will now connect to the API')
    elif initialize_1 == 'n':
        print('Okay bye felicia')
    else:
        print('Try again you fucking mooch')
        welcome()


if __name__ == "__main__":
    welcome()