from __future__ import print_function

import json
import os.path
import add_to_calendar

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        events = add_to_calendar.update()
        # convert events to json
        events_json = json.dumps(events)

        # pretty = json.dumps(events, indent=4, sort_keys=False)
        # print(events)
        # for event in events:
        #     # print(events[event])
        #     service.events().insert(calendarId='primary', body=events[event]).execute()
        print(json.dumps(events[1], indent=4, sort_keys=False))
        service.events().insert(calendarId='primary', body=events[1]).execute()

        # event = {
        #     'summary': 'Google I/O 2015',
        #     'location': '800 Howard St., San Francisco, CA 94103',
        #     'description': 'A chance to hear more about Google\'s developer products.',
        #     'start': {
        #         'dateTime': '2022-11-28T09:00:00-07:00',
        #         'timeZone': 'America/Los_Angeles',
        #     },
        #     'end': {
        #         'dateTime': '2022-11-28T17:00:00-07:00',
        #         'timeZone': 'America/Los_Angeles',
        #     },
        #     'recurrence': [
        #         'RRULE:FREQ=DAILY;COUNT=2'
        #     ],
        #     'attendees': [
        #         {'email': 'lpage@example.com'},
        #         {'email': 'sbrin@example.com'},
        #     ],
        #     'reminders': {
        #         'useDefault': False,
        #         'overrides': [
        #         {'method': 'email', 'minutes': 24 * 60},
        #         {'method': 'popup', 'minutes': 10},
        #         ],

        #     },
        # }

        # service.events().insert(calendarId='primary', body=event).execute()

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()