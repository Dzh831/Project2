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
