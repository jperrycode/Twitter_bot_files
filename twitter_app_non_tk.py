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
import tweepy as tw
#import os module for dotenv
from dotenv import load_dotenv
import os

#import dotenv module to call twitter creds

#from dotenv import load_dotenv


load_dotenv()

#call the credential variables from the dotenv file
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api_con = tw.API(auth)
except:
    print("Cannot connect to the server!")

saved_tweets = []
people_list = {"Mitch McConnel": "senatemajldr", 
                "Donald Trump": "realDonaldTrump", 
                "Don Trump Jr." : "DonaldJTrumpJr"}




def welcome():
    initialize_1 = input("What do you want to do? \n [1] - Post A tweet to your wall \n [2] - Check Latest 3 tweets of user \n [3] - Follow/Unfollow a user \n [4] - Exit the Application \n >>")
    if initialize_1 == "1":
        print('Post a Tweet function accessed!')
        post_tweet_func()
    elif initialize_1 == "2":
        print('User Tweet List Function Accesed!')
        get_user_tweets()
    elif initialize_1 == "3":
        print("User Follow Mode Function Accessed!")
        follow_user()
    elif initialize_1 == "4":
        print('Application SHUT DOWN!!!!')
        pass



def get_user_tweets():
    user_id = input('Please Enter User ID to get last 3 tweets \n >> ')
    tweets = api_con.user_timeline(screen_name=user_id, 
                           # 200 is the maximum allowed count
                           count=100,
                           include_rts = False,
                           # Necessary to keep full_text 
                           tweet_mode = 'extended'
                           )
    for data in tweets[:5]:
        print('{}'.format(data.id))
        print(data.full_text)
        #saved_tweets.append(data.full_text)
        saved_tweets.append(data.id)
        #print(saved_tweets)
    cont = input("What would you like to do? \n [1] - Reply to all three tweets  \n [2] - See tweets of another user \n [3] - Go back to main menu \n>> ")
    if cont == '1':
        reply_to_tweets()
    elif cont == '2':    
        get_user_tweets()
    else:
        welcome()

def follow_user():
    follow_choice = input("What would you like to do? \n [1] - See your Friends List \n [2] - Follow a user \n [3] - Unfriend Someone on your list \n [4] - GO back to Start \n >> ")
    if follow_choice == '1':
        for friend in api_con.friends("jayspurry"):
            print("User name: " + friend.screen_name + " Name: " + friend.name)
        follow_user()
    elif follow_choice == "2":
        user_name = input("Please enter the user you would like to follow \n >> ")
        api_con.create_friendship(user_name)
        print("You have succesfully followed the user {}".format(user_name))
        follow_user()
    elif follow_choice == "3":
        user_name = input("Please enter the user you would like to unfollow \n >> ")
        api_con.destroy_friendship(user_name)
        print("You have succesfully unfollowed the user {}".format(user_name))
        follow_user()
    else:
        print("Thank you, come again!")
        welcome()

def post_tweet_func():
    user_input = input('Please update your twitter status here \n >>')
    api_con.update_status(user_input)
    print('All updated!')
    cont = input("Do you want to post another Tweet?(Y/N) \n >> ")
    if cont == 'y':
        post_tweet_func()
    else:
        welcome()


#save and auto reply to last three tweets from a user

#define function
def reply_to_tweets():
    saved_tweets_length = len(saved_tweets)
    user_reply = input("What would you like to reply to these tweets? \n >> ")
    for i in range(saved_tweets_length):
        api_con.update_status(status = user_reply, in_reply_to_status_id = saved_tweets[i] , auto_populate_reply_metadata=True)
    print("You have succesfully replied to these tweets!")
    saved_tweets.clear()
    print(saved_tweets)
    welcome()



if __name__ == "__main__":
    welcome()



    # comment for code upload