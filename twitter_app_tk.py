import tweepy
import tweepy as tw
#import os module for dotenv
from dotenv import load_dotenv
import tkinter as tk
from tkinter import *
import os
from os import *


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


class ParentWindow(Frame): # parent class
    # initialize the frame with the dunder, referencing the class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # set title of the GUI frame
        self.master.title('Twitter app')
        # set size of the gui window
        self.master.geometry('500x500')

        # variables


        #opening message
        self.lbl_copy_from = tk.Label(self.master, text='What would you like to do?')
        self.lbl_copy_from.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        #choice buttons
            #get tweets button
        self.btn_get_tweets = tk.Button(self.master, text='Get tweets')
        self.btn_get_tweets.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        #self.btn_get_tweets.configure(command=self.choose_copy_from_direct)

            #follow user button
        self.btn_follow_user = tk.Button(self.master, text='Follow user')
        self.btn_follow_user.grid(row=2, column=0, padx=5, pady=5, sticky='we')
        #self.btn_follow_user.configure(command=self.choose_copy_from_direct)
            
            #Post tweet button
        self.btn_post_tweet = tk.Button(self.master, text='Post tweet')
        self.btn_post_tweet.grid(row=3, column=0, padx=5, pady=5, sticky='we')
        #self.btn_choose_copy_from.configure(command=self.choose_copy_from_direct)

            #close button
        self.btn_cancel = tk.Button(self.master, text='Exit')
        self.btn_cancel.grid(row=4, column=0, padx=5, pady=5, sticky='we')
        self.btn_cancel.configure(command=self.cancel)


#close app function
    def cancel(self):
        self.master.destroy()



if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    # create a loop so the window can stay open while using
    # once loop is canceled, window will go away
    root.mainloop()

