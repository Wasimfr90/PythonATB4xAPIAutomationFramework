# APIConstants - Class which contain all the endpoints.
# Keep all the urls

class APIConstants():
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update -> PUT, PATCH, DELETE - bookingid

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)