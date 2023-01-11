#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import os

# import json output from the designer tool
baseDir = os.path.dirname(__file__)
fileName = "card.json"

# Bot's access token
botToken = "<INSERT_AUTH_TOKEN_HERE>"

# ***********************************
# Function to send adaptivecards in Webex
# ***********************************
def sendCard(email, attachment):
    url = "https://webexapis.com/v1/messages"
    payload = json.dumps({
        "toPersonEmail": email,
        "text": "card",
        "attachments":[attachment]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + botToken
    }
    res = requests.post(url, headers=headers, data=payload)

# ===================================
# main processing
# ===================================
# Convert json files to Dictionary type for use in python
json_open = open(baseDir + "/" + fileName, 'r')
json_dict = json.load(json_open)

# Create attachment parameter when sending API.
attachment = {
    "contentType": "application/vnd.microsoft.card.adaptive",
    "content": json_dict
}

# send adaptivecards
res = sendCard("<INSERT_DESTINATION_ADDRESS_HERE>", attachment)