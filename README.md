# Project2

Through json, the tweets will parse into the text and then go through the sentiment analysis. More detailed keyword information or more complete tweet author and publication time will allow users to index tweets in less time and with more accurate results.

The process of Twitter APIs code is create a compliance job. In this file I can upload a dataset with Tweet IDs or User IDs. The responsed is:

{
    "data": {
        "resumable": false,
        "upload_url": "",
        "download_expires_at": "",
        "download_url": "",
        "status": "",
        "name": "",
        "upload_expires_at": "",
        "id": "",
        "created_at": "",
        "type": ""
    }
}

And then Upload the Tweet IDs or User IDs to check for compliance. After that check the status of the compliance job. Finally, download your results.

Output: I searched for two tweets

Tweet 1 Save EDG Groups schedule as your wallpaper!https://mobile.twitter.com/EDG_Edward/status/1575806764624535553 Overall Sentiment: score of 0.400 with magnitude of 1.799Tweet 2 Thank you for your support, let's fight together.https://mobile.twitter.com/EDG_Edward/status/1577529490838024194 Overall Sentiment: score of 0.6 with magnitude of 1.2

The two most recent tweets both have positive sentiments.

Disclaimer:I refer the code from 'sample code', I only use it for learning and will not use it for any commercial purposes.



______________________________________________________________________________________________________________________________________________________________________

Phase 2

The premise of this part is to build your own social media sentiment analyzer which based on the premise of applying sentiment analysis.

The MVP is determining whether a tweet's subject line or hashtag is negative or positive.

User: 1. As a topic maker, I want to know if Twitter's users have a positive or negative attitude towards the topic
     
2. As a Twitter user, I want to let Twitter techs know about my attitude and opinion about tweets， so that twitter can send me more tweets that I like.
      
I will go through the program of phase1 as a tool. This social media analyzer is used to measure the sentiment change of a hashtag at any point in time. Since the program cannot analyze a large number of tweets at once, at the command line, the user must type something like "phase_1.py --twitter_hashtag--num_tweets 2". The user will enter a twitter handle and the number of tweets in 10 tweets for analysis

The outcome is:
Tweets1 @JaychouupdatesJay Chou's Bedtime Stories 6.6 first single release6.8 pre-order 6.24 release album Sentiment: score of 0.5 with magnitude of 1.0 for this hashtag.Tweet2:https://twitter.com/EDG_Edward/status/158.....@Edward_Gaming.Overall Sentiment: score of 0.3 with magnitude of 0.9 for this hashtag

At this point of time, Jay Chou has just announced the release of his new album, so people's hashtags on the topic are positive. And the EDG club announced that the players were infected with the new crown, so people were not so positive on the topic.
