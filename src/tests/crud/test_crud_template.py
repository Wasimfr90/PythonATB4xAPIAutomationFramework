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

    def test_update_booking_id_token(self):
        pass

    def test_delete_booking_id(self):
        pass
