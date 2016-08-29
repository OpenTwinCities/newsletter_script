# newsletter_scripts

Simple scripts we use to help us manage the OTC newsletter

## events.py

Used to add subscribers to groups for events that they have registered for or attended.

```
python events.py 'otc_members.csv' 'event_members.csv' 'output.csv' 'EventName' 'RegisteredHeader' 'AttendedHeader'
```

AttendedHeader is optional. If not provided, then the script will not add members to an Attended group for the event.
