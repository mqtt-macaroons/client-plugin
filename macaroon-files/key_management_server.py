#! /usr/bin/env python
from pymacaroons import Macaroon, Verifier
import time
from memory_profiler import profile
import csv
import paho.mqtt.client as mqtt

"""

"""

keys = {
    'dartmouth': 'asdfasdfas-a-very-secret-signing-key',
    'samsung': 'asdfasdfas-a-very-secret-signing-key',
    'apple': 'asdfasdfas-a-very-secret-signing-key'
}

# CSV structure: device, validity, serialized macaroon, channels

# devicename, manufacturername, channels is an array
def generate_macaroons(device, manufacturer, channels):
    # Check if we have key for the existing device
    # If so, revoke it and add the new one
    if check_macaroon(device):
        revoke_macaroon_by_device(device)

    m = Macaroon(
    location='localhost',
    identifier=manufacturer,
    key=keys[manufacturer]
    )
    m.add_first_party_caveat(device)
    validity = "Valid till: " + str(time.time() + 31556952)
    m.add_first_party_caveat(validity)
    for channel in channels:
        m.add_first_party_caveat(channel)
    # Add to a file for blacklisting and whitelisting
    with open('whitelist.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([device, validity, m.serialize()] + channels)
    return m

def check_macaroon(device):
    with open('whitelist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == device:
                return True
    return False
    

def revoke_macaroon_by_device(device):
    # remove from whitelist
    read_lines = []
    with open('whitelist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] != device:
                read_lines.append(row)
    with open('whitelist.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in read_lines:
            writer.writerow(row)

def revoke_macaroon_by_macaroon(macaroon):
    # remove from whitelist
    m = Macaroon.deserialize(macaroon)
    read_lines = []
    with open('whitelist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[2] != m.serialize():
                read_lines.append(row)
    with open('whitelist.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in read_lines:
            writer.writerow(row)

def login_device(macaroon, manufacturer, channel_id):
    m = Macaroon(
    location='localhost',
    identifier=manufacturer,
    key=keys[manufacturer]
    )
    m1 = Macaroon.deserialize(macaroon)
    channels = []
    for caveat in m1.caveats:
        m.add_first_party_caveat(caveat.to_dict()['cid'])
        channels.append(caveat.to_dict()['cid'])
    return m1.signature == m.signature and channel_id in channels[2:]

m1 = generate_macaroons("device1", "samsung", ["device1"])
m2 = generate_macaroons("device2", "samsung", ["device2"])
m1 = generate_macaroons("device1", "samsung", ["device1"])

manufacturer = "samsung"
import csv
with open('whitelist.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print login_device(row[2], manufacturer, "device1")
client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.publish("/device1", "abcd", qos=0, retain=False)
