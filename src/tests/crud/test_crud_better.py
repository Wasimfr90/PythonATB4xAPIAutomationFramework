# Conftest
#from conftest import get_booking_id, create_token
# Create Token
# Create Booking id
# Update the Booking(Put) - BookingID, Token
# Delete the booking


# Verify that create booking id when we update we are able to update it and delete it also.

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

import allure
import pytest
import requests


class TestCRUDBooking(object):

    @allure.title("Test CRUD operation update(PUT).")
    @allure.description("Verify that Full update with the booking ID and Token is working.")

    def test_update_booking_id_token(self, create_token, get_booking_id):          # getting the value of create_token and get_booking_id is from conftest.py
        # final_booking_id = get_booking_id
        token = create_token
        # print(final_booking_id)
        print(token)
        print(get_booking_id)

        put_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
        print(put_url)
        response = put_request(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )

        # Verification here & more
        verify_response_key(response.json()["firstname"], expected_data="Firoj")
        verify_response_key(response.json()["lastname"], expected_data="Rahaman")
        verify_http_status_code(response_data=response, expected_data=200)

    def test_delete_booking_id(self, create_token, get_booking_id):
        print(get_booking_id)
        print(create_token)
        delete_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
        response = delete_request(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
            auth=None,
            in_json=False
        )
        print("Delete result=",response)
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)



