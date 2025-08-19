import requests


def create_user(user_data: dict):
        base_url = "http://127.0.0.1:8155"
        end_point = "/users"
        response = requests.post(f'{base_url}{end_point}', json=(user_data))
        status = response.status_code
        print(status)
        print(response.text)



