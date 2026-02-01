import requests

def test_root_endpoint():
    response = requests.get("http://host.docker.internal:5000")
    assert response.status_code == 200
    assert "Hello" in response.text  
