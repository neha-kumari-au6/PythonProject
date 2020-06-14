# Importing Modules
import os
import requests
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import re

os.system("")

# Main function for command line inputs
def main():
    # Initializing argoarse module to get parser method
    parser = argparse.ArgumentParser(description="""
Bitcoin Price Notification Application.
""", epilog="Author - Neha Jamwal")
    # adding argument for time interval and setting default us 
    parser.add_argument("-t", "--time_interval", type=int, nargs=1,
                        default=[1], metavar="time_interval",
                        help="Time interval for updates, default is 1 min")
    # adding argument for alert threshold 
    parser.add_argument("-a", "--alert_threshold", type=int, nargs=1, default=[
                        710000], metavar="alert_threshold",
                        help="Threshold price, default is ₹ 7 lakhs")
    # adding argument for  notification destinaion selection  by default ifttt
    parser.add_argument("-d", "--destination", default="ifttt",
                        metavar="destination",
                        help="""Destination for price update :
-d telegram/twitter/IFTTT 
By default is IFTTT""")

    args = parser.parse_args()
#printing on command line
    print("""Bitcoin Notifier started\n""",
            'Time interval is ', args.time_interval[0],
            'min\n Threshold is ₹', args.alert_threshold[0],
            '\n Destination is ', args.destination, '\n\n')

    while True:
        # getting email of the user 
        email = input("Provide Your Email For Threshold Price Alert: \n")
        regex = r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
        # check if the email is valid or not
        if(re.search(regex, email, re.I)):
            break
        # if email not valid will ask for email again
        else:
            print("Invalid Email\n")
            continue

    print("Follow on Twitter : https://twitter.com/bitcoinpriceno1\n")
    print("Join on Telegram : https://t.me/bitcoinnotifier0\n")

    # calling the function bitcoinPriceNotification

    bitcoinPriceNotification(args.time_interval,
                             args.alert_threshold,
                             args.destination,
                             email)


# Saving api amd webhooks in variables for further use
bitcoinApiUrl = "https://api.coindesk.com/v1/bpi/currentprice/INR.json"

webhooksUrl = "https://maker.ifttt.com/trigger/"

webhooksKey = "/with/key/gDbWbKAe0gqUyvocP1FnoCG5vf3SPQ5e0VIqK-w6wYP"


# Function to get Current Bitcoin price in INR
def getBitcoinPrice():
    response = requests.get(bitcoinApiUrl)
    # storing data of api is json format
    response_json = response.json()
    # getting bitcoin price in INR
    rateFloat = round(float(response_json["bpi"]["INR"]["rate_float"]))
    print("Current Bitcoin Value: ", rateFloat)
    return rateFloat


# Function to send the notification of price on different platforms
def postNotification(data, dest):

    date = data["date"]
    price = data["bitcoinPrice"]
    # defining the data format 
    data = {"value1": date, "value2": price}

    # On choosing destination telegram
    if dest == "telegram":
        iftttUrl = webhooksUrl+"Bitcoin_Telegram_Notification"+webhooksKey
    # On choosing destination twitter
    elif dest == "twitter":
        iftttUrl = webhooksUrl+"Bitcoin_Twitter_Notification"+webhooksKey
    # By default notification destination
    else:
        iftttUrl = webhooksUrl+"Bitcoin_Phone_Notification"+webhooksKey

    # sending the notification to the user on choosen method
    requests.post(iftttUrl, json=data)
    print("Bitcoin Price Notification Sent\n")


# Function to send email for threshold price alert
def postAlertEmail(email, data):
    msg = MIMEMultipart()

    # Getting email and password from the the config file
    password = "bitcoinprice@2020"
    msg["From"] = "bitcoin.price.notification.neha@gmail.com"
    msg["To"] = email

    # emergancy message

    message = """From:bitcoin.price.notification.neha@gmail.com
To: {}
Subject: !! Alert !! Bitcoin Price Below Threshold
Bitcoin Price reached below the Threshold Price\n
Date/Time: {}
Current Bitcoin Price: ₹{} ,\n
""".format(email, data["date"], data["bitcoinPrice"])

    # adding gmail sever to send mails
    email_server = smtplib.SMTP('smtp.gmail.com: 587')

    email_server.starttls()

    # Login into gmail
    email_server.login(msg["From"], password)

    # Sending the mail alert email
    email_server.sendmail(msg["From"], msg["To"], message.encode("utf-8"))

    email_server.quit()

    #print if successfull

    print("Threshold Alert Email Sent\n")


# Function which collects price and send a notification to dest
def bitcoinPriceNotification(timeInterval, threshold, destination, email):
    timeInterval = int(timeInterval[0])
    threshold = float(threshold[0])
    destination = destination.lower()

    try:
        while True:
            # getting the bitcoin price
            bitcoinPrice = getBitcoinPrice()
            #storing date and time
            date = datetime.now().strftime("%d.%m.%Y %H:%M")
            bitcoinData = {
                "date": date,
                "bitcoinPrice": bitcoinPrice}

            # checking if the price is less than threshold
            if bitcoinPrice <= threshold:
                print("!! Alert !! Bitcoin Price Reached Threshold\n")
                # sending alert email to user
                postAlertEmail(email, bitcoinData)
                print(
                    "Further updated after {} minutes\n".format(timeInterval))
                time.sleep(timeInterval*60)
                continue
            # sending regular notification to user
            postNotification(bitcoinData, destination)

            print("Further updated after {} minutes\n".format(timeInterval))
            time.sleep(timeInterval*60)

    # Stopping the program
    except KeyboardInterrupt:
        print("\n__STOPPING THE PROGRAM___\n")
        return


if __name__ == '__main__':
    main()