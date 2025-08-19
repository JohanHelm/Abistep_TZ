import requests


def get_users():
    base_url = "http://127.0.0.1:8155"
    end_point = "/users"
    response = requests.get(f'{base_url}{end_point}')
    status = response.status_code
    print(status)
    print(response.text)