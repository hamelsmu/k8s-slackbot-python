import os, slack

def send_message(msg, channel):
    "Send a message to slack.  Setup bot with https://www.pragnakalp.com/create-slack-bot-using-python-tutorial-with-examples/"
    token = os.getenv('SLACK_TOKEN')
    if token and msg and channel:
        try:
            client = slack.WebClient(token=token)
            client.chat_postMessage(channel=channel,text=msg)
        except Exception as e:
            print(f'Error sending slack message: {e}')

if __name__ == '__main__':
    send_message(msg="Hello World", channel="#mlatwork")
