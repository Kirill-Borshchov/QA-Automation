import json
import pytest
import requests
from hamcrest import *

headers = {
    'content-type': 'application/json'
}

x_value = [1, 4, 9, 16, 25]
y_value = [-1, -4, 9, 0, 25]


class TestCalc:


    @pytest.mark.parametrize("x", x_value)
    @pytest.mark.parametrize("y", y_value)
    def test_sum(self, x, y):
        request_data = {"expr": str(x) + " + " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(result["result"], equal_to(str(x + y)), 'Sum is invalid')

    @pytest.mark.parametrize("x", x_value)
    @pytest.mark.parametrize("y", y_value)
    def test_subtract(self, x, y):
        request_data = {"expr": str(x) + " - " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(result["result"], equal_to(str(x - y)), 'Subtract is invalid')

    @pytest.mark.parametrize("x", x_value)
    @pytest.mark.parametrize("y", y_value)
    def test_multiply(self, x, y):
        request_data = {"expr": str(x) + " * " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(result["result"], equal_to(str(x * y)), 'Multiply is invalid')