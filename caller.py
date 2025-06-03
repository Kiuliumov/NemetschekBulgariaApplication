import os
import django
import json
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject5.settings")
django.setup()

from QuerySort.models import Event

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def create_events_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            try:
                event = Event(
                    name=item['name'],
                    town=item['town'],
                    date=parse_date(item['date']),
                    type=item['type'],
                    lectors=item['lectors']
                )
                event.full_clean()
                event.save()
                print(f"Event {event.name} successfully loaded.")
            except Exception as e:
                print(f"There was an error! " + str(e))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python caller.py file.json")
        print("Make sure the json looks like this {name: name, town: town, date: date}")
    else:
        create_events_from_json(sys.argv[1])
