import requests

URL = f"http://api.sl.se/api2/TravelplannerV3/trip.json?key=aa704a5c893c433f9c0a38c00371a300\
&lang=sv&destExtId=1319&searchForArrival=1"


def get_trip_from_coordinates(position: str, schedule_start: str):
    coordinates_position_and_arrival_time = position + "&time=" + schedule_start
    r = requests.get(url=URL, params=coordinates_position_and_arrival_time)
    return {
        'legs': _get_legs_from_trip(r.json())
    }


def _get_legs_from_trip(data):
    trip = data['Trip'][-1]
    legs = [format_leg(l) for l in trip['LegList']['Leg']]
    return legs


def format_leg(leg):
    return {
        'origin': {
            'name': leg['Origin']['name'],
            'time': leg['Origin']['time'],
            'date': leg['Origin']['date']
        },
        'destination': {
            'name': leg['Destination']['name'],
            'time': leg['Destination']['time'],
            'date': leg['Destination']['date']
        },
        'name': leg['name'],
        'type': leg['type']
    }
