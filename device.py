#! /usr/bin/env python
from pymacaroons import Macaroon, Verifier
import paho.mqtt.client as mqtt

"""

"""

def on_connect(client, userdata, flags, rc):
    client.subscribe("#")
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def login(macaroon):
    pass

def logout(macaroon):
    pass

def encrypt_communication(macaroon, channel_id):
    pass

def get_channels(macaroon):
    channels = []
    for caveat in macaroon.caveats:
        channels.append(caveat.to_dict()['cid'])
    return channels[2:] 

hardcoded_macaroon = "MDAxN2xvY2F0aW9uIGxvY2FsaG9zdAowMDE3aWRlbnRpZmllciBzYW1zdW5nCjAwMTBjaWQgZGV2aWNlMQowMDIyY2lkIFZhbGlkIHRpbGw6IDE2MjY5Mzc0NzUuNjcKMDAxMGNpZCBkZXZpY2UxCjAwMmZzaWduYXR1cmUgO3ichQlQO8XHqzJJzy4lke8SwJMuwFX8gW7RWeb4WeYK"
device_id = "device1"

m = Macaroon.deserialize(hardcoded_macaroon)
print m.signature
print get_channels(m)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
