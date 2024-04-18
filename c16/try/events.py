import datetime
import uuid
import json

class EventManager:
    def __init__(self):
        self.events = {}

    def create_event(self, event_name, event_date, *notes, **kwargs):
        event_id = str(uuid.uuid4())
        event_datetime = datetime.datetime.strptime(event_date, '%Y-%m-%d %H:%M')

        event_details = {
            "name": event_name,
            "date": event_datetime.strftime('%Y-%m-%d %H:%M'),
            "notes": notes,
            **kwargs  # Any additional keyword arguments
        }

        self.events[event_id] = event_details
        return event_id

    def update_event(self, event_id, **kwargs):
        if event_id in self.events:
            event_details = self.events[event_id]
            event_details.update(kwargs)

    def delete_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False

    def list_events(self):
        for event_id, event_details in self.events.items():
            print(f"Event ID: {event_id}")
            print(f"Name: {event_details['name']}")
            print(f"Date: {event_details['date']}")
            if event_details['notes']:
                print("Notes:")
                for note in event_details['notes']:
                    print(f"  - {note}")
            print("Additional Details:")
            for key, value in event_details.items():
                if key not in ['name', 'date', 'notes']:
                    print(f"  - {key}: {value}")
            print()

    def save_events(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.events, file)

    def load_events(self, filename):
        try:
            with open(filename, 'r') as file:
                self.events = json.load(file)
        except FileNotFoundError:
            self.events = {}

if __name__ == "__main__":
    event_manager = EventManager()

    event_manager.create_event(
        "Birthday Party",
        "2023-12-31 20:00",
        "Don't forget the cake!",
        location="My House",
        organizer="John Doe"
    )

    event_manager.create_event(
        "Team Meeting",
        "2023-11-15 14:30",
        "Agenda: Project update",
        room="Meeting Room 2",
        organizer="Alice Smith"
    )

    event_manager.save_events("events.json")

    # Clear the current events
    event_manager.events = {}

    # Load events from file
    event_manager.load_events("events.json")

    event_manager.list_events()

    # Update an event
    event_manager.update_event(list(event_manager.events.keys())[0], notes=["Bring a gift!"])

    # Delete an event
    event_manager.delete_event(list(event_manager.events.keys())[1])

    print("\nUpdated Events:")
    event_manager.list_events()

