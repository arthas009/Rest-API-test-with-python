import requests

def test_random_cat_fact():
    url = "https://cat-fact.herokuapp.com/facts/random"
    response = requests.get(url)
    assert response.status_code == 200
    json_response = response.json()
    assert "text" in json_response
    assert "type" in json_response
    assert json_response["type"] == "cat"

def test_all_cat_facts():
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    for fact in json_response:
        assert "text" in fact
        assert "type" in fact
        assert fact["type"] == "cat"
