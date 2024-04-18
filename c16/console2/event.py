import datetime
import uuid
import json

class EventManager():
    """ the event manager class"""
    def __init__(self):
        self.events = {}

    def create_event(self, event_name, event_date, *notes, **kwargs):
        """creates an event"""
        event_id = str(uuid.uuid4())
        event_datetime = datetime.datetime.strptime(event_date, '%Y-%m-%d %H:%M')
        event_details = {
                "name": event_name,
                "date": event_datetime.strftime('%Y-%m-%d %H:%M'),
                "notes": notes,
                **kwargs
                }

        self.events[event_id] = event_details
        return event_id

    def update_event(self, event_id, **kwargs):
        """updates an event"""
        if event_id in self.events:
            event_details = self.events[event_id]
            event_details.update(kwargs)

    def list_events(self):
        for event_id, event_details in self.events.items():
            print(f"Event ID is {event_id}")
            print(f"Name of event is {event_details['name']}")
            print(f"Date of event is {event_details['date']}")
            if event_details['notes']:
                print("Notes:")
                for note in event_details['notes']:
                    print(f" - {note}")
            print("AOB:")
            for key, value in event_details.items():
                if key not in ['name', 'date', 'notes']:
                    print(f" - {key}: {value}")
            print()

    def delete_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False

    def save_events(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.events, f)

    def load_events(self, filename):
        try:
            with open(filename, 'r') as f:
                self.events = json.load(f)
        except FileNotFoundError:
            self.events = {}


if __name__ == '__main__':
    event_manager = EventManager()

    event_manager.create_event(
            "C16 Live Learning Session",
            "2023-11-08 15:00",
            "We'll be talking about the AirBnB project!!!!!",
            location="Via Zoom",
            invitees="Cohort 16 SEs",
            recorded=True
            )
    event_manager.create_event(
            "PLD",
            "2023-11-09 17:30",
            "We'll be talking about OOP",
            location="ALX Hub",
            invitees="Cohort 17 SEs"
            )
    
    event_manager.save_events("events.json")

    event_manager.events = {}

    event_manager.load_events("events.json")

    event_manager.list_events()

    event_manager.update_event(list(event_manager.events.keys())[0], notes=["The AirBnB project and more"])

    event_manager.delete_event(list(event_manager.events.keys())[1])

    print("\nUpdated Events:")
    event_manager.list_events()
