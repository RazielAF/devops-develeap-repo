from cgi import test
import unittest
import requests

local = 'http://172.20.0.3:5000/'
BASEURL = "http://ec2-18-132-169-179.eu-west-2.compute.amazonaws.com:8084/"


def test_posting_on_server():
    response = requests.post(
        BASEURL,
        data={
            "direction": "in",
            "truck": "KPR N9",
            "containers_id": "1,2",
            "truck_weight": 3000,
            "force": "true",
            "produce": "apples",
        }
    )
    assert response.status_code == 200


test_posting_on_server()
