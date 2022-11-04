import requests


BASEURL = "http://ec2-18-132-169-179.eu-west-2.compute.amazonaws.com:8084"
available_routes = [
    "/",
    "/getweightparams",
    "/health",
    "/session",
    "/unknown",
    "/batch_weight",
    "/item",
]


for route in available_routes:
    response = requests.get(BASEURL + route)
    assert response.status_code == 200
