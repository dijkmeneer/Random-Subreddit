import praw

reddit = praw.Reddit(
    client_id="your client id here",
    client_secret="your client secret here",
    user_agent="your user agent here"
)



start_loop = ("a")



input("to stop the script do ctrl+c, enter to continue")

erase = input('Do you want to erase the text files? y/n  ')

while erase == ('y'):
    open('original.txt', 'w').close()
    erase = ("n")
    print("erased")






loop = ('a')
while loop == ('a'):
    subreddit = reddit.random_subreddit(nsfw=False)
    subs = int(reddit.get('/r/'+str(subreddit)+'/about.json').subscribers)
    
    if start_loop == ("a"):
        print("started searching, this might take up to 15 minutes depending on what you maximum is")
        start_loop = ("b")
    if int(subs) < 20000000000000000000000:  #the maximum subscribers for a subreddit to have
        if int(subs) >20:                    #the minimum subscribers for a subreddit to have
            f = open("original.txt", "a")
            f.write('\n')
            f.write("reddit.com/r/" +str(subreddit))
            print("written")
            f.close()