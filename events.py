import csv
import sys

REGISTERED_LABEL = 'Registered'
ATTENDEE_LABEL = 'Attendee'


def ReadMembers(filename):
    rows = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows[row['Email Address']] = row
    return {'rows': rows, 'fieldnames': reader.fieldnames}


def WriteMembers(members, filename):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=members['fieldnames'])

        writer.writeheader()
        for member_email in members['rows']:
            writer.writerow(members['rows'][member_email])


def AddEvent(otc_members, event_members, event_name, rsvp_header,
             attended_header=None):
    for event_email in event_members['rows']:
        event_member = event_members['rows'][event_email]
        if event_email in otc_members['rows']:
            otc_member = otc_members['rows'][event_email]
            member_events = filter(None, otc_member['Events'].split(','))
            member_events.append(event_name)
            if event_member.get(rsvp_header, 'No') == 'Yes':
                member_events.append(' '.join([event_name, REGISTERED_LABEL]))
            if (attended_header and
                    event_member.get(attended_header, 'No') == 'Yes'):
                member_events.append(' '.join([event_name, ATTENDEE_LABEL]))
            otc_member['Events'] = ','.join(member_events)


def process(otc_members_filename, event_members_filename, output_filename,
            event_name, rsvp_header, attended_header=None):
    otc_members = ReadMembers(otc_members_filename)
    event_members = ReadMembers(event_members_filename)
    AddEvent(otc_members, event_members, event_name, rsvp_header,
             attended_header)
    WriteMembers(otc_members, output_filename)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 6:
        args.append(None)
    process(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],
            sys.argv[6])
