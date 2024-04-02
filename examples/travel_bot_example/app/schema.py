from serpapi import GoogleSearch
from config import SerpAPI
import random
import string
import json

fight_booking = [
    {
        "type": "function",
        "function": {
            "name": "book_flight",
            "description": "Books a flight and returns a booking ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure_id": {
                        "description": "The ID or code of the departure airport.",
                        "type": "string",
                    },
                    "arrival_id": {
                        "description": "The ID or code of the arrival airport.",
                        "type": "string",
                    },
                    "outbound_date": {
                        "description": "Date of outbound flight in the format 'YYYY-MM-DD'.",
                        "type": "string",
                    },
                    "return_date": {
                        "description": "Date of return flight in the format 'YYYY-MM-DD'.",
                        "type": "string",
                    },
                    "currency": {
                        "description": "Currency for the prices, e.g., 'USD'.",
                        "type": "string",
                    },
                    "passenger_name": {
                        "description": "Name of the passenger.",
                        "type": "string",
                    },
                    "email": {
                        "description": "Email of the passenger.",
                        "type": "string",
                    },
                },
            },
            "required": [
                "departure_id",
                "arrival_id",
                "outbound_date",
                "return_date",
                "currency",
                "passenger_name",
                "email",
            ],
        },
    },
    {
        "type": "function",
        "function": {
            "name": "flight_search",
            "description": "Fetches flight results from Google Flights API.",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure_id": {
                        "description": "The ID or code of the departure airport.",
                        "type": "string",
                    },
                    "arrival_id": {
                        "description": "The ID or code of the arrival airport.",
                        "type": "string",
                    },
                    "outbound_date": {
                        "description": "Date of outbound flight in the format 'YYYY-MM-DD'.",
                        "type": "string",
                    },
                    "return_date": {
                        "description": "Date of return flight in the format 'YYYY-MM-DD'.",
                        "type": "string",
                    },
                    "currency": {
                        "description": "Currency for the prices, e.g., 'USD'.",
                        "type": "string",
                    },
                    "max_price": {
                        "description": "maximum ticket price.",
                        "type": "integer",
                    },
                    "adults": {
                        "description": "Number of adults. Defaults to '1'.",
                        "type": "string",
                    },
                    "type": {
                        "description": "Type of flight. Defaults to '1'. Available options: 1 - Round trip (default), 2 - One way.",
                        "type": "string",
                    },
                    "show_hidden": {
                        "description": "Whether to show hidden flights. Defaults to 'true'.",
                        "type": "string",
                    },
                    "travel_class": {
                        "description": "Travel class. Defaults to '1'. Available options: 1 - Economy (default), 2 - Premium economy, 3 - Business, 4 - First",
                        "type": "string",
                    },
                    "stops": {
                        "description": "Number of stops. Defaults to '0'.",
                        "type": "string",
                    },
                    "bags": {
                        "description": "Number of bags. Defaults to '1'.",
                        "type": "string",
                    },
                },
            },
            "required": [
                "departure_id",
                "arrival_id",
                "outbound_date",
                "return_date",
                "currency",
                "max_price",
            ],
        },
    },
]


def get_flight_results(
    departure_id: str,
    arrival_id: str,
    outbound_date: str,
    currency: str,
    max_price: int,
    adults: str = "1",
    type: str = "2",
    show_hidden: str = "true",
    travel_class: str = "1",
    stops: str = "0",
    bags: str = "1",
    return_date=None,
) -> dict[str, any]:
    """
    Give a budget or max price, fetches flight results from Google Flights API.

    Args:
        departure_id (str): The ID or code of the departure airport.
        arrival_id (str): The ID or code of the arrival airport.
        outbound_date (str): Date of outbound flight in the format 'YYYY-MM-DD'.
        return_date (str): Date of return flight in the format 'YYYY-MM-DD'.
        currency (str): Currency for the prices, e.g., 'USD'.
        max_price(int): maximum ticket price.
        adults (str, optional): Number of adults. Defaults to '1'.
        type (str, optional): Type of flight. Defaults to '1'. Available options: 1 - Round trip (default), 2 - One way.
        show_hidden (str, optional): Whether to show hidden flights. Defaults to 'true'.
        travel_class (str, optional): Travel class. Defaults to '1'. Available options: 1 - Economy (default), 2 - Premium economy, 3 - Business, 4 - First.
        stops (str, optional): Number of stops. Defaults to '0'.
        bags (str, optional): Number of bags. Defaults to '1'.

    Returns:
        dict[str, any]: Flight results in a dictionary format.
    """
    results = {}
    if return_date:
        type = "1"

    params = {
        "api_key": SerpAPI,
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": currency,
        "adults": adults,
        "type": type,
        "show_hidden": show_hidden,
        "travel_class": travel_class,
        "stops": stops,
        "bags": bags,
        "max_price": max_price,
    }

    search = GoogleSearch(params)
    flight_results = search.get_dict()
    if flight_results["error"]:
        return flight_results["error"]
    results["price"] = flight_results["best_flights"][0]["price"]
    results["layover"] = flight_results["best_flights"][0]["layovers"]
    results["total_duration"] = flight_results["best_flights"][0]["total_duration"]
    results["trip_type"] = flight_results["best_flights"][0]["type"]
    results["airplane"] = flight_results["best_flights"][0]["flights"][0]["airplane"]
    return results


def book_flight(
    departure_id: str,
    arrival_id: str,
    outbound_date: str,
    return_date: str,
    currency: str,
    passenger_name: str,
    email: str,
) -> dict[str, any]:
    """
    Books a flight and returns a booking ID.

    Args:
        departure_id (str): The ID or code of the departure airport.
        arrival_id (str): The ID or code of the arrival airport.
        outbound_date (str): Date of outbound flight in the format 'YYYY-MM-DD'.
        return_date (str): Date of return flight in the format 'YYYY-MM-DD'.
        currency (str): Currency for the prices, e.g., 'USD'.
        passenger_name (str): Name of the passenger.
        email (str): Email of the passenger.

    Returns:
        dict[str, any]: Booking information with a booking ID.
    """
    # Generate a random booking ID
    booking_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Construct booking information
    booking_info = {
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": currency,
        "passenger_name": passenger_name,
        "email": email,
        "booking_id": booking_id,
    }

    return json.dumps(booking_info)
