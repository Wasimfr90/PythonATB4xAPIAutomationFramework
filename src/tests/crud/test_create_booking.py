# API Testcase
from http.client import responses

# URL -> api_constants.py
# headers -> utils.py
# payload -> payload_manager.py
# HTTP POST -> api_request_wrapper.py
# verification -> common_verification.py

import allure
import pytest
import requests
from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that create booking status and Booking ID shouldn't be")
    @allure.description("Create booking from the payload and verify that the booking id should not be")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase - TC1 - positive")
        response = post_request(
            url = APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        LOGGER.info(response.json()["bookingid"])
        LOGGER.info("End of the testcase TC1 - positive")

    @pytest.mark.negative
    @allure.title("Verify that create booking doesn't work with no payload")
    @allure.description("Create booking with no payload and verify that the booking id should not be generated")
    def test_create_booking_negative(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase - TC2 - negative")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)
        # verify_json_key_for_not_null_token(response.json()["bookingid"])
        # LOGGER.info(response.json()["bookingid"])
        LOGGER.info("End of the testcase TC2 - negative")
