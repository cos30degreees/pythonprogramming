import urllib.request, urllib.parse, urllib.error


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print(counts)
print(((10 >= 5*2) and (10 <= 5*2)))


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[even.machine] = set()
        if event.type == 'login':
            machines[event.type].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].remove(event.user)
     return machines

def generate_report(machines):
    for machine, user in machine.items():
        if len(users) > 0:
            user_list = ','.join(users)
            print('{} is {}'.format(machine,user_list))
