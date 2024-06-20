import requests

def test_poem_random():
    url = "https://poetrydb.org/random"
    response = requests.get(url)
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    assert "title" in json_response[0]
    assert "author" in json_response[0]

def test_poem_author():
    author = "Emily Dickinson"
    url = f"https://poetrydb.org/author/{author}"
    response = requests.get(url)
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    for poem in json_response:
        assert poem["author"] == author
