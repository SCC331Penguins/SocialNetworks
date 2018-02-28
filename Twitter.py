import twitter

# Populate the Twitter API keys below
consumer_key = '03IfePawFpKcqIpcGtYKIHV8m'
consumer_secret = 'ZPyQOXTw6V5T0YTdXvtGTkDahObGL5Mn54rMkC9ii1hNzf4k3b'
access_token_key = '967806995381346305-aUvaNrRB8Ad6KmoDDjOO1LfYO8r8p8R'
access_token_secret = '3Wft8NQqHe9nPsrUjoTUisGIJvw1yiXWVsru9Pac0jY5V'

previous = {
    'temperature': 0,
    'humidity': 0,
    'light': -100,
    'tilt_x': 0,
    'tilt_y': 0,
    'motion': 'false',
    'uv': 0,
    'ir': 0,
    'humidity': 0,
    'sound': 0,
}


api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret)

def send_direct_message(msg, twitter_handle):
    # Send Direct Message to official Twitter handle
    try:
        api.PostDirectMessage(msg, user_id=None, screen_name=twitter_handle)
    except Exception as e:
        print(e)
        tweet_at_user(msg + " \n\nFollow us so we can DM you.", twitter_handle)

def tweet_at_user(msg, twitter_handle):
    # Tweet at official Twitter handle
    try:
        api.PostUpdate(status='@' + twitter_handle+" " + msg)
    except Exception as e:
        print(e)

# ---------------- Notifications ------------------
def humidity_twitter_check(humidity, twitter_handle, photon_id = None):
    try:
        msg = ''
        if (is_not_close(humidity, previous['humidity'])):
            if (photon_id != None):
                msg += photon_id + ' says: '

            if (humidity > 60):
                msg += 'This room appears to be pretty humid. Consider purchasing a dehumidifier.' + \
                       ' Humidity at ' + str(humidity) + '%.'
                send_direct_message(msg, twitter_handle)
            elif (humidity < 30):
                msg += 'This room appears to be pretty dry.' + \
                       ' Humidity at ' + str(humidity) + '%.'
                send_direct_message(msg, twitter_handle)
            print(msg)
        previous['humidity'] = humidity
    except Exception as e:
        print(e)


def temperature_twitter_check(temperature, twitter_handle, photon_id=None):
    try:
        msg = ''
        if(is_not_close(temperature, previous['temperature'])):
            if (photon_id != None):
                msg += photon_id + ' says: '

            if (temperature > 40):
                msg += 'This room appears to be pretty hot. Could we interest you in a smart fan?' + \
                       ' Temperature at ' + str(temperature) + 'C.'
                send_direct_message(msg, twitter_handle)

            elif (temperature < 10):
                msg += 'This room appears to be pretty cold. Maybe a radiator could be of use to you.' + \
                       ' Temperature at ' + str(temperature) + 'C.'
                send_direct_message(msg, twitter_handle)

            print(msg)
        previous['temperature'] = temperature
    except Exception as e:
        print(e)

def light_twitter_check(light, twitter_handle, photon_id=None):
    try:
        msg = ''
        if(is_not_close(light, previous['light'])):
            if (photon_id != None):
                msg += photon_id + ' says: '

            if (light > 50):
                msg += 'Your room is quite bright right now. Consider turning a few lights off to conserve energy.' + \
                       ' Light levels at ' + str(light) + 'lux.'
                send_direct_message(msg, twitter_handle)

            elif (light < 0):
                msg += 'Your room is quite dark.' + \
                       ' Light levels at ' + str(light) + 'lux.'
                send_direct_message(msg, twitter_handle)

            print(msg)
        previous['light'] = light
    except Exception as e:
        print(e)

def motion_twitter_check(motion, twitter_handle, photon_id=None):
    try:
        msg = ''
        if(motion == previous['motion']):
            if (photon_id != None):
                msg += photon_id + ' says: '
            msg += 'Motion Detected in this room.'
            send_direct_message(msg, twitter_handle)
            print(msg)
        previous['motion'] = motion
    except Exception as e:
        print(e)



def is_not_close(new, old):
    # check range
    if(new < old-5 or new > old + 5):
        return True
    else:
        return False


if __name__ == '__main__':
    humidity_twitter_check(61, 'EduardSchlotter', 'Yeezy')
    humidity_twitter_check(20, 'EduardSchlotter', 'Yeezy')

    #send_direct_message("Test Message", 'EduardSchlotter')
    #tweet_at_user("Test Message", 'EduardSchlotter')