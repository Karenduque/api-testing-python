from asserter import assert_equal
from session import Endpoints, HTTPSession, RequestTypes, StatusCodes
from test_utils import decorate_test, RequestParams

ENDPOINT = Endpoints.LOGIN

params = {'username': RequestParams.username,
          'password': RequestParams.password
        }

class TestLogin:

    @staticmethod
    @decorate_test
    def test_station_api_status_code():
        status_code, _ = HTTPSession.send_request(RequestTypes.POST, ENDPOINT, params)
        assert_equal(status_code, StatusCodes.STATUS_200, f'Status code of {ENDPOINT} enpoint')

    
