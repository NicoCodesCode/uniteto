from app import app


def test_get_length_page_returns_200():
    client = app.test_client()
    response = client.get("/length", follow_redirects=True)
    assert response.status_code == 200


def test_invalid_input_shows_error():
    client = app.test_client()
    response = client.post(
        "/length", data={"length": "abc", "convert-from": "inch", "convert-to": "meter"}
    )
    assert response.status_code == 200
    assert b"Invalid value" in response.data


def test_same_unit_conversion_returns_same_value():
    client = app.test_client()
    response = client.post(
        "/length",
        data={"length": "10", "convert-from": "inch", "convert-to": "inch"},
    )
    assert response.status_code == 200
    assert b"10" in response.data


def test_convert_inch_to_meter_via_route():
    client = app.test_client()
    response = client.post(
        "/length",
        data={"length": "39.37", "convert-from": "inch", "convert-to": "meter"},
    )
    assert response.status_code == 200
