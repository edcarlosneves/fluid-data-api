from copy import deepcopy

REQUEST_BODY = {
    "fluid_name": "Water",
    "fluid_temperature": 45.0,
    "fluid_pressure": 101.325,
}


def get_create_fluid_without_argument_message(missing_argument):
    return {
        "detail": [
            {
                "loc": ["body"],
                "msg": f"Fluid.__init__() missing 1 required positional argument: '{missing_argument}'",
                "type": "type_error",
            }
        ]
    }


def test_get_zero_fluids(client):
    response = client.get("/fluids")
    assert response.status_code == 200
    assert response.json() == []


def test_get_fluids(client):
    post_response = client.post("fluid", json=REQUEST_BODY)
    post_response_json = post_response.json()
    expected_response = deepcopy(REQUEST_BODY)
    expected_response["fluid_id"] = post_response_json["fluid_id"]
    get_response = client.get("/fluids")
    get_response_json = get_response.json()

    assert get_response.status_code == 200
    assert get_response_json == [expected_response]


def test_create_fluid(client):
    response = client.post("fluid", json=REQUEST_BODY)
    reponse_json = response.json()
    expected_response = deepcopy(REQUEST_BODY)
    expected_response["fluid_id"] = reponse_json["fluid_id"]
    assert response.status_code == 200
    assert response.json() == expected_response


def test_create_fluid_without_name(client):
    missing_argument = "fluid_name"
    REQUEST_BODY_COPY = deepcopy(REQUEST_BODY)
    del REQUEST_BODY_COPY[missing_argument]
    response = client.post("fluid", json=REQUEST_BODY_COPY)
    assert response.status_code == 422

    assert response.json() == get_create_fluid_without_argument_message(
        missing_argument
    )


def test_create_fluid_without_temperature(client):
    missing_argument = "fluid_temperature"
    REQUEST_BODY_COPY = deepcopy(REQUEST_BODY)
    del REQUEST_BODY_COPY[missing_argument]
    response = client.post("fluid", json=REQUEST_BODY_COPY)
    assert response.status_code == 422

    assert response.json() == get_create_fluid_without_argument_message(
        missing_argument
    )


def test_create_fluid_without_pressure(client):
    missing_argument = "fluid_pressure"
    REQUEST_BODY_COPY = deepcopy(REQUEST_BODY)
    del REQUEST_BODY_COPY[missing_argument]
    response = client.post("fluid", json=REQUEST_BODY_COPY)
    assert response.status_code == 422

    assert response.json() == get_create_fluid_without_argument_message(
        missing_argument
    )


def test_get_a_fluid(client):
    REQUEST_BODY_COPY = deepcopy(REQUEST_BODY)
    REQUEST_BODY_COPY["fluid_id"] = "aaaaaa"
    post_response = client.post("/fluid", json=REQUEST_BODY_COPY).json()
    fluid_id = post_response["fluid_id"]
    get_response = client.get(f"/fluid/{fluid_id}")

    assert get_response.status_code == 200
    assert get_response.json() == [REQUEST_BODY_COPY]
