#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

CLIENT_ID = '261794177530-vpubpn8dlird7v4tkvbv5g3ujueu6rh3.apps.googleusercontent.com'
CLIENT_SECRET = 'XplTCraljxSV0jA7ISzRbLod'

OAUTH_SCOPE='https://www.googleapis.com/auth/drive'

FILENAME='document.txt'

REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url=flow.step1_get_authorize_url()
print 'Go to the following link in your browser:'+authorize_url
code = raw_input('Enter verification code:').strip()
credentials = flow.step2_exchange(code)

http=httplib2.Http();
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http = http)

media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable = True)
body = {
    'title':'My document',
    'description':'A test document',
    'mimeType':'text/plain'
    }
file = drive_service.files().insert(body=body, media_body = media_body).execute()
pprint.pprint(file)
####list####
result = []
param = {}
files = drive_service.files().list(**param).execute()
result.extend(files['items'])
print result
