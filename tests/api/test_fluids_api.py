from copy import deepcopy

REQUEST_BODY = {
    "fluid_id": "0fc84f34-ce7b-4b76-af9c-acfc6bc8c4fb",
    "fluid_name": "Water",
    "fluid_temperature": 45.0,
    "fluid_pressure": 101.325,
}
EACH_FLUID_ON_RESPONSE = REQUEST_BODY


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


def test_get_n_fluids(client):
    NUMBER_OF_FLUIDS = 5

    response_expected = []
    for _ in range(NUMBER_OF_FLUIDS):
        client.post("/fluid", json=REQUEST_BODY).json()
        response_expected.append(EACH_FLUID_ON_RESPONSE)

    response = client.get("/fluids")

    print(response_expected)
    assert response.status_code == 200
    assert response.json() == response_expected


def test_create_fluid(client):
    response = client.post("fluid", json=REQUEST_BODY)
    assert response.status_code == 200
    assert response.json() == EACH_FLUID_ON_RESPONSE


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
