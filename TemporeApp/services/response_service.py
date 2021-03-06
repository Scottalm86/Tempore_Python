from .location import get_coordinates_for_location
from .Slrequest import get_trip_from_coordinates
from .database_inserter import dose_user_exist_in_db, add_user_if_it_dosent_exist_in_db,\
    getting_user_info_by_email, upsert_user_info
import datetime
from TemporeApp import views
import logging

log = logging.getLogger(__file__)
tday = datetime.date.today()


def main_response_handler(data):
    log.info(f"{data}")
    travel_response = _travel_response_handler(data)
    return travel_response



# str(tday.isoweekday())
def _travel_response_handler(data):
    if dose_user_exist_in_db(data) is True:
        upsert_user_info(data)
        travel_plan = getting_user_info_by_email(data)
        return {'TravelPlan': travel_plan}
    log.info("User doesnt exist")
    add_user_if_it_dosent_exist_in_db(data)
    location = get_coordinates_for_location(data['address'])
    person_schedule = data[str(tday.isoweekday())]
    commute_travel_plan = get_trip_from_coordinates(location, person_schedule)
    return {'TravelPlan': commute_travel_plan}


def _school_break_handler(data):
    weekNumber=datetime.date.isocalendar()[1]
    weekBreak=[1, 9, 16, 44,]

