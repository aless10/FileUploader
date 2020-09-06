from unittest import mock
from django.test import Client

import pytest


@pytest.fixture
def client():
    return Client()


@mock.patch("health_app.views.request_time")
def test_status_view(date_now, client):
    mock_date = "2020-06-21 13:59:02.818368"
    date_now.return_value = mock_date
    response = client.get('/health/app-health')
    assert response.status_code == 200
    assert response.data == {"status": "ok", "date": mock_date}


