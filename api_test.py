from api_commons import verify_status, get_value, is_email_exists
from api_config import ENDPOINTS, STATUSCODE
from api_requests import get_request_service


def test_api_get():
    response = get_request_service(url=ENDPOINTS.REGRES_API)
    verify_status(response, STATUSCODE.SUCCESS)

    assert get_value(response, 'total_pages') == 2

    assert is_email_exists(response, "byron.fields@reqres.in")
