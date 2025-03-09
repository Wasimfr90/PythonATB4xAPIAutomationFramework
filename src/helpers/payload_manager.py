# payloads

def payload_create_booking():
    payload = {
        "firstname": "Wasim",
        "lastname": "Rahaman",
        "totalprice": 65995,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-01",
            "checkout": "2025-03-10"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Firoj",
        "lastname": "Rahaman",
        "totalprice": 65995,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-01",
            "checkout": "2025-03-10"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
