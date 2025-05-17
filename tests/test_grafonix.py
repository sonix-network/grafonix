import pytest
from grafonix import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fetch_data(client, requests_mock):
    # Mock the external API response
    requests_mock.get('https://ipinfo.io', json={'key': 'value'})

    response = client.get('/fetch-data')
    assert response.status_code == 200
    assert response.json == {
        'original': {'key': 'value'},
        'message': 'Data fetched and modified successfully'
    }

