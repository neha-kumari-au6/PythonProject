==========Bitcoin Price Notifier========>

#   Bitcoin 

Bitcoin is a digital currency created in January 2009 following the housing market crash. It follows the ideas set out in a whitepaper by the mysterious and pseudonymous Satoshi Nakamoto. The identity of the person or persons who created the technology is still a mystery. Bitcoin offers the promise of lower transaction fees than traditional online payment mechanisms and is operated by a decentralized authority, unlike government-issued currencies.

There are no physical bitcoins, only balances kept on a public ledger than everyone has transparent access to, that – along with all Bitcoin transactions – is verified by a massive amount of computing power. Bitcoins are not issued or backed by any banks or governments, nor are individual bitcoins valuable as a commodity. Despite it not being legal tender, Bitcoin charts high on popularity, and has triggered the launch of hundreds of other virtual currencies collectively referred to as Altcoins.

#   IFTTT


IFTTT is both a website and a mobile app. The free service launched in 2010 with the following slogan: "Put the Internet to work for you". It's changed a lot in recent years, however. Currently, with IFTTT, you can connect all your "services" together so that tasks are automatically completed. There are numerous ways you can connect all your services - and the resulting combinations are called "Applets".

Applets essentially automate your daily workflow, whether it's managing smart home devices or apps and websites. So, for instance, if you own the Philips Hue smart lighting system, you could use IFTTT to automatically turn on a light every time you're tagged in a Facebook photo. In another example, you could use IFTTT to automatically email readers when they comment on your WordPress blog.


#   Bitcoin Notifier
As we all know, the Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, let’s make a Python app that runs as a command-line tool to do the work for you.

Although many alternatives exist such as Firebase/Custom Web Sockets, we recommend using the popular automation website IFTTT. IFTTT (“if this, then that”) is a web service that bridges the gap between different apps and devices.

#   Prerequisite

  - Python3 or above installed in your system
  - Install the IFTTT App 
  - An email account for emergency price notification alert 
  - Telegram App --follow us on this channel : https://t.me/bitcoinnotifier0  
  - Twitter account and follow us on :  https://twitter.com/bitcoinpriceno1
  
   
#  Installation

    Bitcoin notifier need to use requests for fetching the data from the api so we need to insatll that 
    first from pip. 
    Use the command below to inatall requests

    ============================================================
    pip install requests
    ============================================================

#   Modules used

    os
    requests
    argparse
    smtplib
    MIMEMultipart
    datetime
    time
    re


#   Description

    Bitcoin notifier is a script made in python which will end regualar and alert notification
    to the user.
    Webhooks are used for the sending regualar notification on twitter, telegram and IFTTT.

    By default the regualar notifications will be sent to IFTTT.

#   Bitcoin notifier have two workings:

    Regular notifications:

        In this the user will get regular notification in one minute interval on his IFTTT App.
        User can customize is regular notification medium from telegram, twitter and IFTTT.
        User can change his destination for notification by entering below written line:

    =========================================================
       -d (choose one :  IFTTT,twitter,telegram)  
    =========================================================

    Alert Notifications:

        Alert notification will be sent to the email provided by the user whenever the threshold falls
        below 710000.
        
        User can change is alert notification price by entering below written line:

    ==============================================================
        -a (alert price: eg. 700000)
    ==============================================================

    Time-Interval:
        By default the user will receive one notification per minute but user can cutomize that by entering a time interval in minutes

    ==========================================================
       -t (time interval in min: eg. 2))
    ==========================================================

#   Working

    -For using this notifier user should install all the above mentioned modules if not installed.

    - Run this progaram 

    - Will prompt an input for email

    - If email is valid user will be notified about the bitcoin price on his IFTTT app
        according to default interval, destionation and threshold if not specified
        and price alert will be sent to provided email address.

    -For customization user can enter below written code on command line:

    ======================================================================
    bitcoinNotifier.py -t 2 -a 600000 -d telegram
    ======================================================================

    The variables used above are as follows:
    bitcoinNotifier.py is name of the file
    t - time interval in minutes
    a - alert threshold in INR
    d - where to send regular notificaton(twitter,telegram,IFTTT)






 


